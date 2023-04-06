# Image Processing Service

To deploy using Terraform Cloud:

-   Clone project to your github repo

-   Create a new project on Google Cloud with [billing enabled](https://cloud.google.com/billing/docs/how-to/modify-project)

-   Create account in Terraform Cloud and connect with VCS (Github)

-   Build the base service container (manual deployment for demo purposes):

    ```
    gcloud builds submit
    ```

-   Initialize and apply the Terraform manifests:

    ```
    terraform init
    terraform apply
    ```

## Source

-   Modified from [Serverless Expedition Example](https://github.com/GoogleCloudPlatform/serverless-expeditions/tree/main/terraform-serverless)
