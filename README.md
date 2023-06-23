![Georgian](assets/georgian-logo.png)

# Georgian GenAI Bootcamp (June 2023)

Welcome to the official repository for the Georgian GenAI bootcamp. This repository contains all demos used during the bootcamp to help you get started with your own projects!

## Table of Contents

* [Goals](#goals)
* [Agenda](#agenda)
* [API Access](#api-access)
* [Setup & Installation](#setup--installation)
* [Repository Info](#repository-info)

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

5. Paste private environment files (this should not be committed!)
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