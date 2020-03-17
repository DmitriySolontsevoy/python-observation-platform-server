from flask import request
from flask_restful import Resource
from uuid import uuid1


from src.config.Constants import Constants


class LoginController(Resource):
    session_manager = {}

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Rotate vertically
    def post(self):
        if request.form['username'] == Constants.REGULAR_USER_USERNAME \
                & request.form['password'] == Constants.REGULAR_USER_PASSWORD:

            token = uuid1()

            self.session_manager.add_session(token, False)

            return {"token": token}, 200
        elif request.form['username'] == Constants.ADMIN_USER_USERNAME \
                & request.form['password'] == Constants.ADMIN_USER_PASSWORD:

            token = uuid1()

            self.session_manager.add_session(token, True)

            return {"token": uuid1()}, 200
        else:
            return {"error": "wrongCredentials"}, 401
