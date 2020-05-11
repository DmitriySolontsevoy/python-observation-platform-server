from flask_restful import Resource
from flask import request

from statekeepers.servoAngleStateKeeper import ServoAngleStateKeeper
from utils.gpioUtils import GPIOUtils
from utils.validationHelper import ValidationHelper


class HorizontalRotationController(Resource):

    state_servo_angle = ServoAngleStateKeeper()

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Rotate horizontally
    def put(self, angle):
        error, code = self.session_manager.check_auth_admin(request)

        if error is None:
            error, code = ValidationHelper.validate_horizontal_servo_angle(angle)

            if error is None:
                if angle == self.state_servo_angle.get_angle():
                    response_code = 304
                else:
                    self.state_servo_angle.set_angle(angle)
                    GPIOUtils.rotate_servo(angle, 0)
                    response_code = 200
                return {"success": "true", "rotationPlain": "horizontal", "angle": angle}, response_code
            else:
                return error, code
        else:
            return error, code
