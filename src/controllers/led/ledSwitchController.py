from flask_restful import Resource
from flask import request

from config.constants import Constants
from utils.gpioUtils import GPIOUtils
from utils.validationHelper import ValidationHelper


class LEDSwitchController(Resource):

    def __init__(self, session_manager, led_state_keeper):
        self.session_manager = session_manager
        self.led_state_keeper = led_state_keeper

    # Set the LED to a 0 or 1 state
    def put(self, state):
        error, code = self.session_manager.check_auth_admin(request)

        if error is None:
            error, code = ValidationHelper.validate_led_state_parameter(state)

            if error is None:
                if state == self.led_state_keeper.get_state():
                    data, response_code = {"success": "true", "LEDState": state}, 304
                elif self.led_state_keeper.get_state() == Constants.LED_BLINKING:
                    data, response_code = {"success": "false", "reason": "LED used by api/tickLED"}, 400
                else:
                    self.led_state_keeper.set_state(state)
                    GPIOUtils.updateLED(state)
                    data, response_code = {"success": "true", "LEDState": state}, 200
                return data, response_code
            else:
                return error, code
        else:
            return error, code
