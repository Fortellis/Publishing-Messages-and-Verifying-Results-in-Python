
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
        token = requests.post('https://identity.fortellis.io/oauth2/aus1p1ixy7YL8cMq02p7/v1/token', data = {'grant_type': 'client_credentials', 'scope': 'anonymous'}, headers= {'Authorization':'Basic base64Encoded{yourClientID:yourClientSecret}', 'Accept':'application/json', 'Cache-Control':'no-cache' })
        print((token.json()['access_token']), flush=True)

        requestId = str(uuid.uuid4())
        print(requestId)

        event = requests.post('https://event-relay.fortellis.io/v2/events/{youChannel}', json = {"id":"6620800b-7029-4a7a-8e80-cdd852fc01c8", "number": 16,"haveYouSaidHello": True, "waysToSayHello": ["Hello", "Hola", "Hallo", "Bonjour", "Guttendag", "Ola"],"helloID": { "language": "English", "id": "7211fedc-e7a8-49eb-93a4-c7e9c732d121"}}, headers = {'Accept':'application/json', 'Content-Type': 'application/json', 'Data-Owner-Id': '{subscribingOrganizationId}', 'X-Request-Id': requestId,'Authorization': 'Bearer ' + token.json()['access_token'], 'partitionKey': '{aUniqueUUIDForYourPartition}'})
        print(event.json(), flush=True)

        return(event.json())

api.add_resource(Event, '/event')

if __name__ == '__main__':
    app.run(debug=True) 




