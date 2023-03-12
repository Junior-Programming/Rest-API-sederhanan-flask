# Import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS


# Inisiasi Object
app = Flask(__name__)


# inisiasi Object flask_restful
api = Api(app)


# Inisiasi object flask_cors
CORS(app)


# Inisiasi Variabel tipe Dictionary
identitas = {}  # Variabel global, Dictionary = json


# membuat class Resource
class ContohResource(Resource):

    # Buat method GET
    def get(self):

        #response = {"msg": "Hello World"}

        return identitas

    # buat method POST
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]

        # tampung identitas input
        identitas["nama"] = nama
        identitas["umur"] = umur

        # buat response ketika data berhasil ditambahkan
        response = {"msg": "Data Berhasil Di Tambahkan!"}

        # Kembalikan nilai
        return response


# Setup Resourcenyaa
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])


# buat code Eksekutornya
if __name__ == "__main__":
    app.run(debug=True, port=8080)
