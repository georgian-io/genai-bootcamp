# General Hackathon Info
## Access
_TODO: Describe how to access the instances used for this hackathon and any other necessary tools._

## Data
_TODO: Describe how to access the data used for this hackathon, preferably through code in src/utils._

## Goals
_TODO: Describe the goal of this hackathon, preferably through quantifiable metrics in src/utils._

## Streams
_TODO: Describe the main work streams (teams) in this hackathon, try to keep it up to date with changes or additional streams._

# Installation

1. Environment management options
   
    a)  Poetry: ```poetry shell```
    
    b) Conda: create and activate a conda env for this project:
```bash
conda create -n genai-bootcamp python=3.9
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

4. Create private environment file (this will not be committed!)
```
cp .env-template .env
```
Add any necessary API keys there following the given format.

# Contributing

## General Guidelines
- **Each stream should have it's own folders in `notebooks` and `src`**. This is to minimize the chances of affecting other people's code and keeping code separation across streams.

- **Notebooks should contain as little code as possible.** Consider moving large amounts of code into functions and classes, and moving those to the right location in `src`.

- **Write some tests, but don't go overboard.** We recommend writing mostly short, easy tests. Especially regression tests that showcase how to use crucial / complex code.

## Shared Utilities
One of the main reasons make this repo easily installable is to facilitate code re-use. 

With this in mind we recommend that you consider implementing the following utilities to make it easy for everyone to use them:

- `src/genai_bootcamp/utils` a directory with shared tools.

    - `../utils/datasets.py`: Dataset classes that can load data relevant to the hackathon. The idea is to make it as easy as possible to load data in a consistent way.

    - `.../utils/metrics.py`: metric classes that compute common metrics of interest. Usually, improving these metrics is the whole goal of the hackathon.

- `notebooks/start_here.ipynb`: A notebook that shows how to import and call any shared utilities, and demonstrates a baseline to improve on for the final goal.

# Repo Info
## Poetry
We use [poetry](https://python-poetry.org/) as our dependency manager.
The link above has great documentation but there is a TL;DR.

- Install the package: `poetry install`
- Add a dependency: `poetry add <python-lib>`
- Where are dependencies specified? `pyproject.toml` include the high level requirements. The latests exact versions installed are in `poetry.lock`.

