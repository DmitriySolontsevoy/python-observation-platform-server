from flask_restful import Resource
from flask import request

from src.utils.validationHelper import ValidationHelper


class HorizontalRotationController(Resource):

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Rotate horizontally
    def put(self, angle):
        error, code = self.session_manager.check_auth_admin(request)

        if error is None:
            error, code = ValidationHelper.validate_horizontal_servo_angle(angle)

            if error is None:
                return {"success": "true", "rotationPlain": "horizontal", "angle": angle}, 200
            else:
                return error, code
        else:
            return error, code
