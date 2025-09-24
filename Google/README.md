# Embeddings and Cosine Similarity with BigQuery

## Prerequisite

- [Python](https://www.python.org/downloads) `>= 3.13.7`
- [Gemini API Keys](https://aistudio.google.com/app/apikey)

## Index

1. [BigQuery Dataset](#bigquery-dataset)
2. [Code](#code)
3. Do not forget to [Clean the Cloud](#clean-the-cloud)

## BigQuery Dataset

1. Go to [Google Console](https://console.cloud.google.com/projectcreate) to create a new project.

<img width="1916" height="936" alt="Screenshot From 2025-09-23 07-01-27" src="https://github.com/user-attachments/assets/4a7eff3d-f6d6-4d0d-a337-7ac4993390ba" />

2. Once the project is created, search `BigQuery` in the search bar and click on `BigQuery`.

<img width="1916" height="936" alt="Screenshot From 2025-09-23 07-08-41" src="https://github.com/user-attachments/assets/465fc3a1-86f0-4ce2-a673-512171591682" />

3. Click on the three dots in the explorer column and click `Create dataset`,

<img width="1916" height="936" alt="Screenshot From 2025-09-23 07-10-21" src="https://github.com/user-attachments/assets/99b844b5-f763-43b9-85fd-2aa45c3d9920" />

4. Give a name to the dataset, change the location type of region, select the region closest to your location, and then click the `Create dataset` button.

<img width="1916" height="936" alt="Screenshot From 2025-09-23 07-13-58" src="https://github.com/user-attachments/assets/0eb9f54d-a233-4412-9ada-777ea074cb7b" />

5. Finally, note down the project ID, dataset ID, and region of the dataset. In this case, `main-ember-473011-a4` is the project ID, `vector_database` is the dataset ID, and `us-east1` is the region; similarly, note down the specific data for your case.

## Code

1. Create a Python virtual environment using the following command

Linux/macOS

```bash
python3 -m venv .venv
```

Windows

```bash
py -m venv .venv
```

2. Activate the virtual environment using the following command

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate.bat
```

3. Use the following command to install the required libs and deps.

Linux/macOS

```bash
pip install python-dotenv langchain langchain-community langchain-huggingface langchain-google-community langchain-google-genai
```

Windows

```bash
py -m pip install python-dotenv langchain langchain-community langchain-huggingface langchain-google-community langchain-google-genai
```

4. Create a `.env` file and store the following variables along with their values.

```env
GEMINI_API_KEYS=
PROJECT_ID=
DATASET=
REGION=
TABLE=
```

5. Create a `main.py` file and paste [this code](./main.py).

6. Finally, run the script using the following command.

Linux/macOS

```bash
python main.py
```

Windows

```bash
py main.py
```

## Clean the Cloud

1. Go to the [Google Cloud](https://console.cloud.google.com) and search `manage resources` and go to the `Manage Resources` page.

2. Click the checkbox of the project that you created, and click the `Delete` button on the top navigation bar. This will open a modal where you will be prompted to enter a project ID and then click the `Shut down anyway` button to delete the project and its resources.
