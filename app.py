from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin # Allows Cross Origin Resource Sharing

from constants import POST, LOCAL_FRONT_END_ORIGIN
from utils import get_image_path, get_encoded_image


# Initialize a flask object
app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/translate', methods=[POST])
@cross_origin(origin = LOCAL_FRONT_END_ORIGIN)
def translate():
    """Recieve a letter and send back a base-64 encoded image of the ASL translation."""

    # Extract the letter from the request
    letter = request.form['letter']

    # TODO: add error handling to check that it's valid

    # Get the correct corresponding image path 
    image_path = get_image_path(letter)

    # Encode the image into base64
    image_encoded = get_encoded_image(image_path)

    # Return the encoded string
    return image_encoded

    


# app.run()
if __name__ == '__main__':
    app.run()