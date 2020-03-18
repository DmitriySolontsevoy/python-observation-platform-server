from flask_restful import Resource
from flask import request

from src.utils.gpioUtils import GPIOUtils


class LEDTickController(Resource):
    session_manager = {}

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Switch LED back and forth periodically (period in ms)
    def put(self, period_duration, period_count):
        header = request.headers.get("Authorization")

        if self.session_manager.check_auth(header, True):
            if period_duration < 0.1:
                return {"success": "false", "reason": "Period of blinking is to short (Expected >= 0.1ms)"}, 400
            elif period_count not in range(0, 51):
                return {"success": "false", "reason": "Number of period is invalid (50 >= Expected > 0)"}, 400
            else:
                GPIOUtils.blinkLED(period_duration, period_count)
                return {"success": "true", "BlinkPeriod": period_duration, "BlinkCount": period_count}, 200
        else:
            return {"success": "false", "reason": "Unauthorized"}, 401
