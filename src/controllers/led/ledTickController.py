from flask_restful import Resource, reqparse
from flask import request

from src.config.constants import Constants
from src.utils.gpioUtils import GPIOUtils
from src.utils.validationHelper import ValidationHelper


class LEDTickController(Resource):

    def __init__(self, session_manager, led_state_keeper):
        self.session_manager = session_manager
        self.led_state_keeper = led_state_keeper

    # Switch LED back and forth periodically (period in ms)
    def post(self):
        error, code = self.session_manager.check_auth_admin(request)

        parser = reqparse.RequestParser()
        parser.add_argument('period_duration', type=float)
        parser.add_argument('period_count', type=int)
        args = parser.parse_args()

        if error is None:
            error, code = ValidationHelper.validate_tick_led_parameters(args['period_duration'], args['period_count'])

            if error is None:
                if self.led_state_keeper.get_state() == Constants.LED_BLINKING:
                    data, response_code = {"success": "false", "reason": "LED is already blinking"}, 400
                else:
                    self.led_state_keeper.set_state(Constants.LED_BLINKING)
                    GPIOUtils.blinkLED(args['period_duration'], args['period_count'])
                    self.led_state_keeper.set_state(Constants.LED_OFF)
                    data, response_code = {
                            "success": "true",
                            "BlinkPeriod": args['period_duration'],
                            "BlinkCount": args['period_count']
                    }, 200
                return data, response_code
            else:
                return error, code
        else:
            return error, code
