from datasets import load_dataset
import numpy as np
import re
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import tqdm
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.lancedb import LanceDBVectorStore
from llama_index.core import StorageContext


def load_data(sample_size=100):
    data = load_dataset(
        "EleutherAI/wikitext_document_level",
        "wikitext-103-raw-v1",
        trust_remote_code=False,
    )
    data = data["train"][:sample_size]
    return data


# Data enrichment
def extract_metadata(data):
    title_pattern = re.compile(r"\s=\s([^=]{1,50})\s=\s")
    title = [item for item in re.findall(title_pattern, data)]
    # The regex above isn't perfect so we take the first match as the title
    if len(title) > 0:
        title = title[0]
    else:
        title = "Unknown Title"
    return {"title": title}


# Data cleaning
def clean_data(data):
    # Pattern to find
    pattern = re.compile(r" @(.)@ ")

    # Run this across the entire dataset
    for i, page in enumerate(data["page"]):
        data["page"][i] = re.sub(pattern, r"\1", page)
    return data


# Load as LlamaIndex documents
def preprocess_data(data):
    data = clean_data(data)
    documents = []
    for i in tqdm.tqdm(range(len(data["page"]))):
        documents.append(
            Document(
                text=data["page"][i],
                metadata=extract_metadata(data["page"][i]),
            )
        )
    return documents


# Chunk documents and return nodes
def chunk_documents(documents):
    chunker = SentenceSplitter(chunk_size=512, chunk_overlap=20)
    nodes = chunker.get_nodes_from_documents(documents, show_progress=True)
    print(f"Documents before chunking: {len(documents)}")
    print(f"Documents after chunking: {len(nodes)}")
    return nodes


# Load embedding model
def get_embedding_model(model_name="BAAI/bge-small-en-v1.5"):
    return HuggingFaceEmbedding(model_name=model_name, embed_batch_size=32)


def nodes2local_index(nodes, embedding_model):
    index = VectorStoreIndex(nodes, embed_model=embedding_model, show_progress=True)
    return index
    
def nodes2vector_store(nodes, embedding_model):
    # Create your DB locally
    vector_store = LanceDBVectorStore(
        uri="./lancedb", table_name="test"
    )
    # Link to the collection on llamaindex
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    # Embed and index
    index = VectorStoreIndex(nodes, embed_model=embedding_model, storage_context=storage_context, show_progress=True)
    return index