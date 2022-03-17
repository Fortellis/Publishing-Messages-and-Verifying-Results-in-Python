
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

import json

import requests

import uuid

app = Flask(__name__)
api = Api(app)

class Event(Resource):
    def post(self):
        app.logger.debug('headers: %s' , request.headers)
        print("Request received")
        token = requests.post('https://identity-dev.fortellis.io/oauth2/aus1ni5i9n9WkzcYa2p7/v1/token', data = {'grant_type': 'client_credentials', 'scope': 'anonymous'}, headers= {'Authorization':'Basic UW5OeExtYVJFVFdDZVZ3bEZUeUgwUnBucnQ3S2pyT286VnhubDVva2VVQ2M1eGFuTg==', 'Accept':'application/json', 'Cache-Control':'no-cache' })
        print((token.json()['access_token']), flush=True)

        requestId = str(uuid.uuid4())
        print(requestId)

        event = requests.post('https://event-relay-dev.fortellis.io/v2/events', json = {"id":"6620800b-7029-4a7a-8e80-cdd852fc01c8", "number": 16,"haveYouSaidHello": True, "waysToSayHello": ["Hello", "Hola", "Hallo", "Bonjour", "Guttendag", "Ola"],"helloID": { "language": "English", "id": "b2f7494a-5dcf-448c-9585-5301fc0dd231"}}, headers = {'Accept':'application/json', 'Content-Type': 'application/json', 'Data-Owner-Id': 'b74c3f9a-17ee-4943-81f2-ae22bb4f260d', 'X-Request-Id': requestId,'Authorization': 'Bearer ' + token.json()['access_token']})
        print(event.json(), flush=True)

        return(event.json())

api.add_resource(Event, '/event')

if __name__ == '__main__':
    app.run(debug=True) 




