# TODO
- Rodrigo: Delete history

# General Hackathon Info
## Access
To be able to run the notebooks here, you'll need access to API keys for all these services. Fear not! We've provided you with all the API keys you need! Just extract the zip file we've sent to you in the root of this directory. 

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

4. Paste private environment file (this should not be committed!)
Paste the `.env` file and `google-api.json` file provided separately into root directory of this repository.
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

