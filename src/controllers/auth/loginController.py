from uuid import uuid1

from flask_restful import Resource, reqparse

from src.config.constants import Constants


class LoginController(Resource):

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Login
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()

        if args['username'] == Constants.REGULAR_USER_USERNAME and args['password'] == Constants.REGULAR_USER_PASSWORD:
            token = uuid1().__str__()
            self.session_manager.add_session(token, False)

            return {"token": token, "role": "user"}, 200
        elif args['username'] == Constants.ADMIN_USER_USERNAME and args['password'] == Constants.ADMIN_USER_PASSWORD:
            token = uuid1().__str__()
            self.session_manager.add_session(token, True)

            return {"token": token, "role": "admin"}, 200
        else:
            return {"error": "wrongCredentials"}, 401
