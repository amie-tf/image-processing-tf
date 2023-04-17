# Image Processing Service

This is a serverless solution that uses the Google Cloud Vision API to process images, and is deployed with Terraform Cloud.
![Architecture diagram](architecture.png)

## Deployment Steps [Demo Only]:

#### Github

-   Fork project to your github repo

#### Google Cloud

-   Create a new project on Google Cloud with [billing enabled](https://cloud.google.com/billing/docs/how-to/modify-project). Note down your project id.

-   Create Terraform Service Account and provide with permissions to create infrastructure. (Save your service account key. You will need to input this into Terraform Cloud later)

-   Enable APIs for in-scope services (Cloud Build, Container Registry, Cloud Run, Cloud Vision, Cloud Run, Cloud Functions)

-   Build the base service container (manual deployment for demo purposes):

    ```
    gcloud builds submit
    ```

#### Terraform Cloud (Automated VCS Deployment)

-   Create account in Terraform Cloud

-   Set up Project and Workspace

-   Connect to Workspace with VCS (Github) and link to your Github repo

-   Add environmental variable and secrets

#### Source

-   Inspired By [Serverless Expedition](https://github.com/GoogleCloudPlatform/serverless-expeditions/tree/main/terraform-serverless)
