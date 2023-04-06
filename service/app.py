import os
import tempfile

import flask
import requests
from google.cloud import storage

BUCKET_NAME = os.environ.get("BUCKET_NAME")
FUNCTION_NAME = os.environ.get("FUNCTION_NAME")

app = flask.Flask(__name__)
storage = storage.Client()
bucket = storage.bucket(BUCKET_NAME)


@app.route("/item/<img>")
def item(img):
    blob = bucket.blob(img)
    with tempfile.NamedTemporaryFile() as temp:
        blob.download_to_filename(temp.name)
        return flask.send_file(temp.name, download_name=img)


def get_items(bucket):
    images = storage.list_blobs(BUCKET_NAME)

    # auth when running a privte function
    # https://cloud.google.com/functions/docs/securing/authenticating#functions-bearer-token-example-python
    if "cloudfunctions.net" in FUNCTION_NAME:
        metadata_server_url = "http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience="
        token_full_url = metadata_server_url + FUNCTION_NAME
        token_headers = {"Metadata-Flavor": "Google"}

        token_response = requests.get(token_full_url, headers=token_headers)
        jwt = token_response.text
        function_headers = {"Authorization": f"bearer {jwt}"}
    else:
        function_headers = {}

    items = []
    for img in images:
        print(img)
        # resp returns response from cloud functions
        resp = requests.get(
            FUNCTION_NAME,
            params={"bucket": BUCKET_NAME, "resource": img.name},
            headers=function_headers,
        )
        items.append({"image": img, "data": resp.json()})

    return items


@app.route("/")
def process_images():
    if not BUCKET_NAME:
        return flask.render_template_string(
            "Missing environment variable: BUCKET_NAME."
        )

    if not FUNCTION_NAME:
        return flask.render_template_string(
            "Missing environment variable: FUNCTION_NAME."
        )

    items = get_items(BUCKET_NAME)
    print(items)
    
    return flask.render_template("image-processor.html", items=items)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
