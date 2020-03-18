from flask_restful import Resource
from flask import request

from src.utils.validationHelper import ValidationHelper


class VerticalRotationController(Resource):

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Rotate vertically
    def put(self, angle):
        error, code = self.session_manager.check_auth_admin(request)

        if error is None:
            error, code = ValidationHelper.validate_vertical_servo_angle(angle)

            if error is None:
                return {"success": "true", "rotationPlain": "vertical", "angle": angle}, 200
            else:
                return error, code
        else:
            return error, code
