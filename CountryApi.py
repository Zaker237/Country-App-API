from flask import Flask
from flask_restful import Resource, Api

import requests

app = Flask(__name__)

api = Api(app)

Data = []
@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


class Country(Resource):
    def get(self):
        url = "https://restcountries.eu/rest/v2/all"
        res = requests.get(url)
        return res.json()

api.add_resource(Country, '/')
if __name__ == "__main__":
    app.run(debug=True)

