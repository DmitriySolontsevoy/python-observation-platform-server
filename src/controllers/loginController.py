from flask import request
from flask_restful import Resource, reqparse
from uuid import uuid1


from src.config.Constants import Constants


class LoginController(Resource):
    session_manager = {}

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Rotate vertically
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()

        if args['username'] == Constants.REGULAR_USER_USERNAME and args['password'] == Constants.REGULAR_USER_PASSWORD:

            token = uuid1().__str__()

            self.session_manager.add_session(token, False)

            return {"token": token}, 200
        elif args['username'] == Constants.ADMIN_USER_USERNAME and args['password'] == Constants.ADMIN_USER_PASSWORD:

            token = uuid1().__str__()

            self.session_manager.add_session(token, True)

            return {"token": token}, 200
        else:
            return {"error": "wrongCredentials"}, 401
