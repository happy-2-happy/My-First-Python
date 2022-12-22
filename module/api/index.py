from flask import request, make_response, session
from flask import Flask
from flask_restful import Api, Resource
import json
import time
# import logging
# import logging.config

app = Flask(__name__)
api = Api(app)
# app.config['SECRET_KEY'] = 'SECRET_KEY'  # must be set to use sessions
# logging.config.fileConfig(fname='logging.conf',
#                           disable_existing_loggers=False)

# http://localhost:5000/ - Stock Flask


@app.route('/', methods=['GET'])
def home_page():
    data = {'status': '200', 'message': f'Current time is {time.time()}'}
    return json.dumps(data)


@app.route('/user', methods=['GET'])
def user_page():
    user = str(request.args.get('name'))
    # logging.debug(f'User -> {user}')
    data = {'status': '200', 'name': f'Username is {user}'}
    response = make_response()
    response.status_code = 200
    response.content_type = 'application/json'
    response.data = json.dumps(data)
    # session['temp'] = 'dsfdsfdsfdsfsdfdsfdf'
    return response

# http://localhost:5000/simple/2 -  Flask Restful


class SimpleClass(Resource):
    def get(self, id):
        return f"Get Method called {id}"

    def put(self, id):
        return f"Put Method called {id}"


api.add_resource(SimpleClass, '/simple/<string:id>')

# if __name__ == '__main__':
#     app.run(port=7777)
