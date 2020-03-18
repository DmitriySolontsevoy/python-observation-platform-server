from flask_restful import Resource, reqparse
from flask import request

from src.utils.gpioUtils import GPIOUtils
from src.utils.validationHelper import ValidationHelper


class LEDTickController(Resource):

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Switch LED back and forth periodically (period in ms)
    def post(self):
        error, code = self.session_manager.check_auth_admin(request)

        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()

        if error is None:
            error, code = ValidationHelper.validate_tick_led_parameters(args['period_duration'], args['period_count'])

            if error is None:
                GPIOUtils.blinkLED(args['period_duration'], args['period_count'])
                return \
                    {"success": "true", "BlinkPeriod": args['period_duration'], "BlinkCount": args['period_count']}, 200
            else:
                return error, code
        else:
            return error, code
