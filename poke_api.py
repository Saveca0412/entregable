import requests
from flask import Flask, request

app = Flask(__name__)

def controller_poke(headers):

    try:
        endpoint_poke_api = headers['poke_api']
        exists_ability_name = headers['ability_name']

        response = requests.get(endpoint_poke_api)
        response = response.json()

        abilities = response['abilities'][0]
        ability_name = abilities['ability']['name']

    except Exception as e:
        return {'error':e.args[0]}, 400
    else:
        if exists_ability_name in ability_name:
            return {'This pokemon does have this ability':True}, 200
        return {'This pokemon does not have this ability':False}, 200

@app.route('/api/v2/poke')
def poke():
    response = controller_poke(request.headers)
    return response

if __name__ == "__main__":
    app.run (host='127.0.0.1', port=3100, debug=True)

