from flask_restful import Resource
from flask import request


class HorizontalRotationController(Resource):
    session_manager = {}

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Rotate horizontally
    def put(self, angle):
        header = request.headers.get("Authorization")

        if self.session_manager.check_auth(header, True):
            return {"success": "true", "rotationPlain": "horizontal", "angle": angle}, 200
        else:
            return {"success": "false", "reason": "Unauthorized"}, 401
