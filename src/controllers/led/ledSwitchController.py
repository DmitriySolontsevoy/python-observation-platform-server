from flask_restful import Resource
from flask import request

from src.utils.gpioUtils import GPIOUtils
from src.utils.validationHelper import ValidationHelper


class LEDSwitchController(Resource):

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Set the LED to a 0 or 1 state
    def put(self, state):
        error, code = self.session_manager.check_auth_admin(request)

        if error is None:
            error, code = ValidationHelper.validate_led_state_parameter(state)

            if error is None:
                GPIOUtils.updateLED(state)
                return {"success": "true", "LEDState": state}, 200
            else:
                return error, code
        else:
            return error, code
