# Embeddings and Cosine Similarity with BigQuery

## Prerequisite

- Python
- Gemini API Keys

## BigQuery Dataset

1. https://console.cloud.google.com/projectcreate

2. Once the project is created search `BigQuery` on the search bar and click on the `BigQuery`

[SS]

[SS]

3. Click on the three dots from the explorer column and click `Create dataset`,

[SS]

4. Give a name to the dataset, change the location type of region and select the region closed to your location and then click `Create dataset` button.

[SS]

5. Finally, note down the project id, dataset id, and region of the dataset.

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
