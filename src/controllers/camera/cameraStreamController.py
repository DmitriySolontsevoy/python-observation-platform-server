from flask import request
from flask_restful import Resource


class CameraStreamController(Resource):

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Stream camera feed
    def get(self):
        error, code = self.session_manager.check_auth_regular_user(request)

        if error is None:
            return {"success": "true", "feed": "Yep, this is totally a video"}, 200
        else:
            return error, code
