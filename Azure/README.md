# Embeddings and Cosine Similarity with Azure

## Index

1. [Azure Resources](#azure-resources)
   - [Azure AI Search](#azure-ai-search)
   - [Azure AI Foundry](#azure-ai-foundry)
2. [Code](#code)
3. Do not forget to [Clean the Cloud](#clean-the-cloud)

## Azure Resources

### Azure AI Search

In this lab, we are using **Azure AI Search** as a vector database. To use that, we need to provision the resource and get two values: `VECTOR_SEARCH_ENDPOINT` and `VECTOR_SEARCH_KEY`, which will be used as environment variables.

1. Go to the [Azure Portal](portal.azure.com) and open `AI Search`.

<img width="800" alt="Screenshot From 2026-03-07 11-48-30" src="https://github.com/user-attachments/assets/e5e9123f-1e41-4280-a43a-ca9818297f69" />

2. Click `Create` to create a new search service.

<img width="800" alt="Screenshot From 2026-03-07 11-49-39" src="https://github.com/user-attachments/assets/2eb36210-035b-4d0d-98c1-379250b44011" />

3. Create a new or use an existing resource group. (Suggest: create a new one so its easy to delete the resources later on.)
4. Give a unique name for `Service name`.
5. Make sure the `Pricing tier` is free, unless you want to experience paid service.
6. Finally, click `Review + Create` button at the bottom and then click `Create` button to create the resource.

<img width="800" alt="Screenshot From 2026-03-07 11-53-43" src="https://github.com/user-attachments/assets/98c24fd8-3266-409e-81f7-129c3bcad103" />

7. Next, go to the resource dashboard and copy the `Url` from the `Essentials`. This `Url` will be used as `VECTOR_SEARCH_ENDPOINT`.

<img width="800" alt="Screenshot From 2026-03-07 11-57-59" src="https://github.com/user-attachments/assets/181f5efc-c51f-4169-8cac-ec9c6d66decf" />

8. To get the `VECTOR_SEARCH_KEY` go to the `Keys` tab under `Settings` section from the left navbar. From this screen, copy the `Primary admin key`.

<img width="800" alt="Screenshot From 2026-03-07 11-59-14" src="https://github.com/user-attachments/assets/3aed742c-cac6-44cd-8287-c122cc47307b" />

## Azure AI Foundry

We are using **Azure AI Foundry** to deploy and use models. To use that, we need to provision the resource and get two values: `AZURE_OPEN_API_KEY` and `AZURE_OPEN_API_ENDPOINT`, which will be used as environment variables.

1. Go to the [Azure AI Foundry](http://ai.azure.com/)
2. Click `Create new` button to create a new project.
3. For the resource type, keep the recommended option and click `Next`.

<img width="800" alt="Screenshot From 2026-03-07 12-21-42" src="https://github.com/user-attachments/assets/5d7e25ed-17f4-4edc-95ea-d70be24616de" />

4. Give it a good name, keep everything else default and click `Create`.

<img width="800" alt="Screenshot From 2026-03-07 12-33-28" src="https://github.com/user-attachments/assets/58b32bb3-8018-4c6c-87d8-c8670b43a927" />

5. Finally, from the project overview page, copy `API Key` to use as `AZURE_OPEN_API_KEY` and `Azure OpenAI endpoint` to use as `AZURE_OPEN_API_ENDPOINT`.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/5e61638d-8654-4f21-85b5-d527f00213c6" />

6. Now from the left navbar, click `Models + endpoints` under `My assets` section.
7. Click `Deploy base model`. Now we will deploy an embedding model and a generation model.

<img width="800" alt="Screenshot From 2026-03-07 12-41-27" src="https://github.com/user-attachments/assets/09317a2b-d7f0-47d7-83a9-67c8634a8fda" />

8. Search for `text-embedding-3-small` and click `Confirm`.

<img width="800" alt="Screenshot From 2026-03-07 12-43-59" src="https://github.com/user-attachments/assets/0f378759-24a6-4c89-9533-8d88bad6fe68" />

9. Change the `Deployment type` to `Standard` and click `Deploy` to deploy the model.

<img width="800" alt="Screenshot From 2026-03-07 12-45-04" src="https://github.com/user-attachments/assets/af6bba7b-7095-40cb-8d02-58ec6653d393" />

10. Similarly, deploy `gpt-4.1-mini` model.

## Code

1. Open [this notebook](./main.ipynb) in Google Colab.

2. Add the following environment variables by clicking on this key button, and grant them notebook access

- `AZURE_OPEN_API_ENDPOINT`
- `AZURE_OPEN_API_KEY`
- `VECTOR_SEARCH_ENDPOINT`
- `VECTOR_SEARCH_KEY`

<img width="400" alt="Screenshot From 2026-03-07 13-01-29" src="https://github.com/user-attachments/assets/7a0aa861-37bc-406e-accd-73ca673d6938" />

3. Finally, you can run the commands in the notebook.

## Clean the Cloud

1. On [Azure Portal](portal.azure.com) go to `All Resources` and delete all the resources we created for this lab.

<img width="400" alt="Screenshot From 2026-03-07 13-05-17" src="https://github.com/user-attachments/assets/914b5ee6-6083-422d-86d4-b9878a90496e" />
