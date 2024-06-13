![Georgian](assets/georgian-logo.png)

# Georgian GenAI Bootcamp

Welcome to the Georgian GenAI Bootcamp repository. This repository contains all demo and code from our bootcamps. 

<!-- We're hard at work preparing materials for the next bootcamp. In the meantime, you can read the materials below to get familiar with the topics we covered in previous bootcamps. Please note that we have not updated these materials since the dates noted in the libraries and the code is provided for illustrative purposes only. See the disclosure below for more information. -->

## Table of Contents
- [Georgian GenAI Bootcamp](#georgian-genai-bootcamp)
  - [Table of Contents](#table-of-contents)
  - [Setup \& Installation](#setup--installation)
  - [Previous Bootcamp Materials](#previous-bootcamp-materials)
  - [Resources](#resources)


## Setup & Installation

1. Clone this repository and `cd genai-bootcamp`

2. Setup your environment. Note: This repository requires Python 3.12 or higher.

If you use Conda:

```bash
conda create -n genai_bootcamp python=3.12
conda activate genai_bootcamp
pip install -r requirements.txt
```

If you use Poetry:

```bash
poetry shell
poetry install
```

Troubleshooting Tip:

* If you get an error like `Current Python version (3.x.x) is not allowed by the project (^3.12)`: Delete your old poetry env by running `poetry env remove <env-name>`. You can get the env name by running `poetry env list`. Then run `poetry shell` again.

If you use standard Python:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Create private environment file (this will not be committed!). If you are a bootcamp participant, you should have received this file. Please rename it to `.env`. Some operating systems might rename `.env` to `env`. The period at the front is important as all the notebooks expect this. Please rename the file if you run into this issue.
Note: DO NOT COMMIT THIS FILE OR SHARE IT ANYWHERE!
```
mv env-template .env
```

4. Test your installation by running `notebooks/00-test_environment.ipynb`. If all code blocks work in this notebook, you are all set for the bootcamp! If you use VSCode, you can run notebooks directly in the editor. Otherwise run `jupyter notebook` in your terminal (`poetry run jupyter notebook` if you use Poetry).

[[Back to top]](#)

## Previous Bootcamp Materials

You can find the content from previous bootcamps in the [releases](https://github.com/georgian-io/genai-bootcamp/releases) page. The table below also links you to all our bootcamps, workshops, and other events directly. 

Disclosures: 
Please note code in the linked repositories are provided as-is from the dates of the respective bootcamps. All code provided in those pages is for illustrative purposes only. Dependent libraries may have updated since then and versions in the linked repositories may contain vulnerabilities. No guarantee, representation or warranty is being made, express or implied, as to the safety or correctness of the code. It has not been audited and as such there can be no assurance it will work as intended, and users may experience delays, failures, errors, omissions or loss of transmitted information. We do NOT recommend running the code in the archive. Nothing in this repo should be construed as investment advice or legal advice for any particular facts or circumstances and is not meant to replace competent counsel. It is strongly advised for you to contact a reputable attorney in your jurisdiction for any questions or concerns with respect thereto. Georgian is not liable for any use of the foregoing, and users should proceed with caution and use at their own risk. Please contact info@georgian.io for more info.


| Date    | Event                                                                                           | Link                                                                                |
| ------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| 2023-10 | [Bootcamp](https://github.com/georgian-io/genai-bootcamp/releases/tag/2023_10_october_bootcamp) | [HERE](https://github.com/georgian-io/genai-bootcamp/tree/2023_10_october_bootcamp) |
| 2023-06 | [Bootcamp](https://github.com/georgian-io/genai-bootcamp/releases/tag/2023_06_june_bootcamp)    | [HERE](https://github.com/georgian-io/genai-bootcamp/tree/2023_06_june_bootcamp)    |

[[Back to top]](#)

## Resources

* [GenAI Interface Cookiecutter](https://github.com/rodrigo-georgian/genai-interface-cookiecutter): A cookie cutter template for you to start off with a basic UI using streamlit.
* [Georgian AI Library (GAL)](https://github.com/georgian-io/GAL): Our library containing overviews of AI techniques.

[[Back to top]](#)