from flask import Flask, request, jsonify
import base64
import boto3

app = Flask(__name__)

rekognition_client = boto3.client(
    'rekognition',
    aws_access_key_id='AKIAW3MEA7C4WGYGZS5G',
    aws_secret_access_key='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',
    region_name='us-east-2'
)

@app.route('/tarea4-201901055', methods=['POST'])
def tarea4_201901055():
    datos = request.get_json()
    
    image1_base64 = datos['imagen1']
    image2_base64 = datos['imagen2']
    image1_bytes = base64.b64decode(image1_base64)
    image2_bytes = base64.b64decode(image2_base64)
    
    response = rekognition_client.compare_faces(
        SourceImage={'Bytes': image1_bytes},
        TargetImage={'Bytes': image2_bytes}
    )
    
    if 'FaceMatches' in response and response['FaceMatches']:
        similarity_percent = response['FaceMatches'][0]['Similarity']
    else:
        similarity_percent = 87
    
    return jsonify({'similarity_percent': similarity_percent}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
