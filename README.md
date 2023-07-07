![Georgian](assets/georgian-logo.png)

# Georgian GenAI Bootcamp (June 2023)

Welcome to the official repository for the Georgian GenAI bootcamp. This repository contains all demos used during the bootcamp to help you get started with your own projects!

## Table of Contents

* [Goals](#goals)
* [Agenda](#agenda)
* [API Access](#api-access)
* [Setup & Installation](#setup--installation)
* [Repository Info](#repository-info)
* [Resources](#resources)

---
## Goals
At the end of the hackathon our goal is for participants to have:
- A deeper understanding of the opportunities generative unlocks for them and their companies
- A good theoretical understanding of the latest Generative AI technologies
- A solid practical understanding of the latest Generative AI technologies
- Implemented at least one end-to-end application using generative AI

[[Back to top]](#)

---
## Agenda

### Day 1: 

#### Introduction to LLMs (David Emerson from Vector)
* LLM Trends
* Foundation models
* Working with LLMs
* Intro to Prompt Engineering

#### Customizing LLMs (David Emerson from Vector)
* Prompt Engineering
* Fine-tuning Approaches

#### Hands-on Session (Georgian & Google)
* Setup and example notebooks - Akash Saravanan (Georgian)
* Prompt engineering best practices - Royal Sequeira (Georgian)
* Google demo - Erik Saarenvirta (Google)

### Day 2:
#### Tools & platforms (Rodrigo Ceballos from Georgian)
* Concepts with Langchain
* Memory and Search
* Interfaces with Streamlit
* Evaluation with LabelStudio
* Deployment with HuggingFace

#### Fine-tuning, RLHF, and Deployment
* Fine-tuning - Rohit Saha (Georgian)
* RLHF - Akash Saravanan (Georgian)
* Deploying LLMs - Rodrigo Ceballos (Georgian)

#### LLM Privacy and Security 
* Introduction - Alex Manea (Georgian)
* Robustness and Mitigating Bias - Angeline Yasodhara (Georgian)
* PrivateGPT - Michael Young and Kory Fong (PrivateAI)

[[Back to top]](#)

---
## API Access
To be able to run the notebooks here, you'll need access to API keys for all these services. Fear not! We've provided you with all the API keys you need! Just download the files we've sent to you and place them in the root of this directory. 

Note: If you are visiting this page after the bootcamp/ou were not a part of the bootcamp, you likely don't have the files necessary. Read on for instructions on how to set up each of the APIs that you need. Note that the OpenAI and Google APIs will charge you based on usage, so you will need to have billing setup for it to work.

Note that to run the examples, you only need to have one API key setup. So if you already have access to an OpenAI key, you could run all the notebooks with it (excluding the Google/HuggingFace examples). The PrivateAI API key is used only for the PrivateAI demos (in `notebooks/day-1/04-example-summarization.ipynb` and `notebooks/extra_resources/PrivateAI Demo.ipynb`). 

1. Create a `.env` file. In the root directory of this repo (I.E., the same directory this readme is in), create a `.env` file. Ensure that the period is present at the start of the filename. Within this file, place the following text:
```
OPENAI_API_KEY=""
GOOGLE_APPLICATION_CREDENTIALS="../../google-api.json"
HUGGINGFACEHUB_API_TOKEN=""
HUGGINGFACEHUB_ENDPOINT="https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
PRIVATE_AI_API_KEY = ""
```

2. OpenAI: Create an OpenAI account (or login) and visit the [API Keys](https://platform.openai.com/account/api-keys) page. Generate an API key here and place it in the `.env` file you created above. These examples were designed with GPT-4. If you do not have access to it, please request access through the [waitlist](https://openai.com/waitlist/gpt-4-api). Or alternatively, you can use `gpt-3.5-turbo` instead.

3. Google: Follow steps 1 through 4 detailed in this [link](https://cloud.google.com/vertex-ai/docs/start/client-libraries). Once you have downloaded the service account key from step 4, place it in the root director of this repository and rename it to `google-api.json`. 

4. HuggingFace: Create a HuggingFace account (or login) and visit the [Access Tokens](https://huggingface.co/settings/tokens) page in the settings menu. Generate an token (read access is sufficient) and place it in the `.env` file.

5. PrivateAI: Request an API key through [this form](https://www.private-ai.com/api-key/). Add it to the `.env` file above.

6. You should now have all fields in the `.env` file setup and ready to go! You can now proceed with the installation steps below.

[[Back to top]](#)

---
## Setup & Installation

0. This repository requires you to have installed poetry as a dependency manager. Please follow the instructions to install poetry from [here](https://python-poetry.org/docs/#installation). 

1. Environment management options
   
    a)  Poetry: ```poetry shell```
    
    b) Conda: create and activate a conda env for this project:
```bash
conda create -n genai-bootcamp python=3.10
conda activate genai-bootcamp
```

2. Install `fiddler-auditor` (we need to install this separately as it sometimes breaks).
```
pip install fiddler-auditor==0.0.1
```

3. Install package
```
poetry install
```

4. Check installation worked by running 
```
pytest .
```

5. Setup private environment files

Paste the `.env` file and `google-api.json` file provided to you into root directory of this repository.

Note: DO NOT COMMIT THIS FILE OR SHARE IT ANYWHERE!

[[Back to top]](#)

## Repository Info
### Poetry
We use [poetry](https://python-poetry.org/) as our dependency manager.
The link above has great documentation but there is a TL;DR.

- Install the package: `poetry install`
- Add a dependency: `poetry add <python-lib>`
- Where are dependencies specified? `pyproject.toml` include the high level requirements. The latests exact versions installed are in `poetry.lock`.

### Debugging
- If for some reason `poetry install` fails to install a library try to `pip install <lib>` and then run `poetry install` again. This solves 95% of these errors.

[[Back to top]](#)

## Resources

* [GenAI Interface Cookiecutter](https://github.com/rodrigo-georgian/genai-interface-cookiecutter): A cookie cutter template for you to start off with a basic UI using streamlit!
* [Georgian AI Library (GAL)](https://github.com/georgian-io/GAL): Our public repository of knowledge on all kinds of AI things!

[[Back to top]](#)