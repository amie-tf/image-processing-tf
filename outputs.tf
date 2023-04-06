output "service_url" {
  value = google_cloud_run_service.image-recognition-processor.status[0].url
}

output "bucket_name" {
  value = google_storage_bucket.media.name
}

output "cloud_function_name" {
  value = google_cloudfunctions_function.function.name
}

