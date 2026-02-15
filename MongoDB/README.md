# Embeddings and Cosine Similarity with MongoDB

## Prerequisite

- Python
- Gemini API Keys

## Index

1. [MongoDB Account](#mongodb-account) (Skip this step if you already have MongoDB connection string.)
2. [Code](#code)

## MongoDB Account

### Step 1: Create new account

- Creating a new account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register).

### Step 2: Create an organization

- Create an organization from [this page](https://cloud.mongodb.com/v2#/preferences/organizations).

![image](https://github.com/user-attachments/assets/9d7729b8-2300-492f-8109-6a4eb53080a6)

- You can give any name to the organization.
- Select `MongoDB Atlas`

![image](https://github.com/user-attachments/assets/84c0c8fd-cce9-4af7-8108-be26bf76ce8f)

- Do not need to fill any information on this page.
- Click on `Create Organization` button.

![image](https://github.com/user-attachments/assets/0ee9dcbe-23df-4b41-a4cd-d80e120e0eb6)

### Step 3: Create a project

- Once you create an organization, you will be redirected to Projects page.
- Click on `New Project` button to create a new project.

![image](https://github.com/user-attachments/assets/9183830d-83fe-4694-86c9-f18d9aee38a1)

- Give it any name and click `Next`.

![image](https://github.com/user-attachments/assets/c31d6c5e-762a-4cd2-86a5-3d63ca502c1d)

- Do not need to add anything on this page.
- Click on `Create Project` button.

![image](https://github.com/user-attachments/assets/70ce10d6-3eae-4a5d-8a6c-674c18623294)

### Step 4: Create a cluster

- The next step is to create a cluster.
- Click `Create` to create a new cluster.

![image](https://github.com/user-attachments/assets/49af8614-d8ca-4168-9300-e9ee329effd5)

- Choose the `Free` option.
- Give the cluster any name.
- Keep everything else default.

![image](https://github.com/user-attachments/assets/e857ba79-dd30-429c-9f2f-7103e4a3955e)

### Step 5: Get MongoDB connection string

- As soon as you deploy a cluster, a modal will be displayed on the screen with the title `Connect to <cluster name>`.
- Set the username and password and store it anywhere safely.
- Click on `Create Database User` to create a user for database.
- Then, click `Choose a connection method` button.

![Image](https://github.com/user-attachments/assets/8a6aedbc-9095-42bf-bdd8-92158831ef6c)

- Click `Drivers` under `Connect to your application`

![image](https://github.com/user-attachments/assets/fe4ed023-cef3-49a4-859c-f8063d5ae2c2)

- From this page, please copy MongoDB connection string and paste it anywhere safely.
- In the string, replace `<db_username>` and `<db_password>` with your username and password that we copied earlier.

> [!WARNING]
> DO NOT SHARE your 'MongoDB Connection String' with anyone.

- Finally, click 'Done'.

![Image](https://github.com/user-attachments/assets/ce899fff-a5cd-488f-b03d-d77d7c9e81c3)

### Step 6: Set Network Access

- Click on `Database & Network Access` button under `Security`.

![image](https://github.com/user-attachments/assets/f5eb275f-4394-4320-925f-71b5d3054a4a)

- Click on `Edit` button.
- Click on `Allow Access From Anywhere` button and then click `Confirm` button.

![image](https://github.com/user-attachments/assets/f6b8e055-cfbb-4d56-8527-9ced8154117c)

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
MONGODB_CONNECTION_STRING='mongodb+srv://...........'
GEMINI_API_KEYS='.....'
```

- Use the following command to install the required libs and deps.

```bash
pip install --upgrade sentence-transformers langchain_community langchain langchain_google_genai pymongo python-dotenv
```

- Create a `main.py` file and add [this code](./main.py).

- Finally run the script using the following command.

```bash
python main.py
```
