from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_student():
    data = {
        "Instancia": "Instancia #1 - API #1",
        "Curso": "Seminario de Sistemas 1",
        "Estudiante": "Estudiante - 201901374"
    }
    return jsonify(data)

@app.route('/check', methods=['GET'])
def check():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=3000)