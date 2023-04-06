resource "random_string" "bucket_suffix" {
  length  = 6
  special = false
  upper   = false
}

resource "google_storage_bucket" "media" {
  name          = "tf-${local.bucket_name}-${random_string.bucket_suffix.result}"
  force_destroy = true
}

resource "google_storage_bucket_object" "images" {
  for_each = fileset("${path.module}/${local.bucket_folder}", "*")

  name   = each.value
  source = "${path.module}/${local.bucket_folder}/${each.value}"
  bucket = google_storage_bucket.media.name
}

resource "google_storage_bucket_iam_policy" "media" {
  bucket = google_storage_bucket.media.name

  # Generated with assistance from terraformer
  policy_data = <<POLICY
{
  "bindings": [
    {
      "members": [
        "projectEditor:${var.project}",
        "projectOwner:${var.project}"
      ],
      "role": "roles/storage.legacyBucketOwner"
    },
    {
      "members": [
        "projectViewer:${var.project}",
        "${local.images_worker_sa}"
      ],
      "role": "roles/storage.legacyBucketReader"
    },
    {
      "members": [
        "projectViewer:${var.project}",
        "${local.images_worker_sa}"
      ],
      "role": "roles/storage.legacyObjectReader"
    }
  ]
}
POLICY
}
