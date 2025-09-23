# Embeddings and Cosine Similarity with BigQuery

## Prerequisite

- Python
- Gemini API Keys

## BigQuery Dataset

[Work in progress]

## Code

- Create a python virtual environment using the following command

```bash
python3 -m venv .venv
```

- Active the virtual environment using the following command

```bash
source .venv/bin/activate
```

- Create `.env` file and store the following variables along with their values.

```env
PROJECT_ID=
GEMINI_API_KEYS=
DATASET=
TABLE=
REGION=
```

- Use the following command to install the required libs and deps.

```bash
pip install python-dotenv langchain langchain-community langchain-huggingface langchain-google-community langchain-google-genai
```

- Create a `main.py` file and add [this code](./main.py).

- Finally run the script using the following command.

```bash
python main.py
```
