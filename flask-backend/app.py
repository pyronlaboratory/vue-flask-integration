from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

input_file="email.txt"


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def check_email(email):
    check = False
    with open(input_file, 'r') as file:
        for line in file:
            if line == email:
                check = True
                #print('the email is valid')
        return check

    
@app.route('/', methods=['POST'])
def authenticate_email():
    data_multidict = request.form.copy()
    data_dict = data_multidict.to_dict()
    for key in data_dict.keys():
        data = json.loads(key)
        email = data["email"]
        if check_email(email):
            return jsonify({
            'status': 'success',
            'message': email
            })
        else:
            return jsonify({
            'status':'error',
            'message':'User is not registered!'
            })


if __name__ == '__main__':
    app.run()
