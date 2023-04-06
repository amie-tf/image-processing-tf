# Image Processing Service

##_Architecture Diagram:_

##_Deployment Steps [Demo Only]:_

#### Github

-   Clone project to your github repo

#### Google Cloud

-   Create a new project on Google Cloud with [billing enabled](https://cloud.google.com/billing/docs/how-to/modify-project)

-   Build the base service container (manual deployment for demo purposes):

    ```
    gcloud builds submit
    ```

#### Terraform Cloud (Automated VCS Deployment)

-   Create account in Terraform Cloud

-   Set up Project and Workspace

-   Connect to Workspace with VCS (Github) and link to your Github repo

#### Source

-   Inspired By [Serverless Expedition](https://github.com/GoogleCloudPlatform/serverless-expeditions/tree/main/terraform-serverless)
