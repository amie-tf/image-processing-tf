import io

from flask import jsonify
from google.cloud import storage, vision
from PIL import Image

vision_client = vision.ImageAnnotatorClient()
storage_client = storage.Client()


def detect_text_uri(vision_image):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """

    response = vision_client.text_detection(image=vision_image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return texts
    
def detect_image(request):
    """
    gets image from bucket and detects label
    """
    print('detect images')
    bucket = request.args.get("bucket", None)
    resource = request.args.get("resource", None)

    if not bucket:
        return "Invalid invocation: require bucket", 400

    if not resource:
        return "Invalid invocation: require resource", 400

    uri = f"gs://{bucket}/{resource}"
    print(uri)

    data = {}

    blob = storage_client.bucket(bucket).get_blob(resource).download_as_bytes()

    # Image specifics
    img = Image.open(io.BytesIO(blob))
    data["image_details"] = {
        "height": img.height,
        "width": img.width,
        "format": img.format,
    }

    # testing only
    # uri = "gs://cloud-samples-data/vision/ocr/sign.jpg"


    # Vision API Labels
    vision_image = vision.Image()
    vision_image.source.image_uri = uri
    response = vision_client.label_detection(image=vision_image)
    labels = response.label_annotations
    data["labels"] = [label.description for label in labels]

    print('labels:')
    print(labels)

    #detect texts
    texts = detect_text_uri(vision_image)
    data["texts"] = [text.description for text in texts]
    print('texts:')
    print(texts)

    return jsonify(data)


#testing
# detect_image(request=None)