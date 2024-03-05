from flask import Flask, request, jsonify
import base64
import boto3

app = Flask(__name__)

rekognition_client = boto3.client(
    'rekognition',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name=''
)

@app.route('/tarea3-201901055', methods=['POST'])
def tarea3_201901055():
    datos = request.get_json()
    image = datos['image']
    image_base64 = base64.b64decode(image)
    response = rekognition_client.detect_labels( Image={'Bytes': image_base64} )
    labels = [
            label['Name'] 
            for label in response['Labels']
            ]
    
    return jsonify({'Labels': labels}), 200
    

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
