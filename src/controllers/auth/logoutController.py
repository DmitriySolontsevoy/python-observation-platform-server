from flask_restful import Resource, reqparse
from flask import request


class LogoutController(Resource):

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Logout
    def delete(self):
        token = request.headers.get("Authorization")
        self.session_manager.remove_session(token)

        return {"success": "true"}, 200
