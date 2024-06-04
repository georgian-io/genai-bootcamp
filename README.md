![Georgian](assets/georgian-logo.png)

# Georgian GenAI Bootcamp

Welcome to the Georgian GenAI Bootcamp repository. This repository contains all demo and code from our bootcamps. 

We're hard at work preparing materials for the next bootcamp. In the mean time, feel free to check out materials from previous editions of the bootcamp through the links below.

## Table of Contents
- [Georgian GenAI Bootcamp](#georgian-genai-bootcamp)
  - [Table of Contents](#table-of-contents)
  - [Setup \& Installation](#setup--installation)
  - [Previous Bootcamp Materials](#previous-bootcamp-materials)
  - [Resources](#resources)


## Setup & Installation

1. Clone this repository and `cd genai-bootcamp`

2. Setup your environment

If you use Conda:

```bash
conda create -n llm-evaluation python=3.10
conda activate llm-evaluation
pip install -r requirements.txt
```

If you use Poetry:

```bash
poetry shell
poetry install
```

If you use standard Python:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Create private environment file (this will not be committed!). If you are a bootcamp participant, you would have received this file. Please rename it to `.env`. Some operating systems might rename `.env` to `env`. The period at the front is important as all the notebooks expect this. Please rename the file if you run into this issue.
Note: DO NOT COMMIT THIS FILE OR SHARE IT ANYWHERE!
```
mv .env-template .env
```

4. Test your installation by running `notebooks/00-test_environment.ipynb`. If all code blocks work in this notebook, you are all set for the bootcamp!

[[Back to top]](#)

## Previous Bootcamp Materials

You can find the content from previous bootcamps in the [releases](https://github.com/georgian-io/genai-bootcamp/releases) page. The table below also links you to all our bootcamps, workshops, and other events directly. 

IMPORTANT: Please note code in the linked repositories are provided as-is from the dates of the respective bootcamps. All code provided in those pages is for illustrative purposes only. Dependent libraries have since been updated and current versions may contain vulnerabilities. We do NOT recommend running the code in the archive.

| Date    | Event                                                                                           | Link                                                                                |
| ------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| 2023-10 | [Bootcamp](https://github.com/georgian-io/genai-bootcamp/releases/tag/2023_10_october_bootcamp) | [HERE](https://github.com/georgian-io/genai-bootcamp/tree/2023_10_october_bootcamp) |
| 2023-06 | [Bootcamp](https://github.com/georgian-io/genai-bootcamp/releases/tag/2023_06_june_bootcamp)    | [HERE](https://github.com/georgian-io/genai-bootcamp/tree/2023_06_june_bootcamp)    |

[[Back to top]](#)

## Resources

* [GenAI Interface Cookiecutter](https://github.com/rodrigo-georgian/genai-interface-cookiecutter): A cookie cutter template for you to start off with a basic UI using streamlit.
* [Georgian AI Library (GAL)](https://github.com/georgian-io/GAL): Our library containing overviews of AI techniques.

[[Back to top]](#)