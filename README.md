# TODO
- Kyryl: 06-deployment
- Rodrigo: 01-langchain
- Rodrigo: move memory to day 2
- Rodrigo: check new langchain version works
- Akash: Merge dependabot
- Akash: Pass over notebooks
- Akash: Remove API keys
- Rodrigo: Delete history

# General Hackathon Info
## Access
<!-- - TODO: @Akash API access instructions -->

## Goals
<!-- - TODO: @Rodrigo -->

## Timeline
 <!-- - TODO: @Akash add agenda when final -->

# Installation

1. Environment management options
   
    a)  Poetry: ```poetry shell```
    
    b) Conda: create and activate a conda env for this project:
```bash
conda create -n genai-bootcamp python=3.10
conda activate genai-bootcamp
```

2. Install package
```
poetry install
```
3. Check installation worked by running 
```
pytest .
```

<!-- TODO: @Akash review -->
4. Paste private environment file (this should not be committed!)
Paste `.env` file provided separately into root directory of this repository.
note: DO NOT COMMIT THIS FILE OR SHARE IT ANYWHERE!

# Repo Info
## Poetry
We use [poetry](https://python-poetry.org/) as our dependency manager.
The link above has great documentation but there is a TL;DR.

- Install the package: `poetry install`
- Add a dependency: `poetry add <python-lib>`
- Where are dependencies specified? `pyproject.toml` include the high level requirements. The latests exact versions installed are in `poetry.lock`.

## Debugging
- If for some reason `poetry install` fails to install a library try to `pip install <lib>` and then run `poetry install` again. This solves 95% of these errors.

