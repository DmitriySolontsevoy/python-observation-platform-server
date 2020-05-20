from flask_restful import Resource
from flask import request
from utils.compassHelper import CompassHelper


class CompassController(Resource):

    def __init__(self, session_manager):
        self.session_manager = session_manager
        self.compassHelper = CompassHelper()

    # Get bearing
    def get(self):
        error, code = self.session_manager.check_auth_admin(request)

        if error is None:
            try:
                bearing = self.compassHelper.get_bearing()
                return {"success":"true", "bearing": bearing}, 200
            except OSError:
                return {"success":"false", "reason":"Couldn't get magnetic value. Check if compass is connected or retry!"}, 520
