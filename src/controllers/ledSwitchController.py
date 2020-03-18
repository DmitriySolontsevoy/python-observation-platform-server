from flask_restful import Resource
from flask import request

from src.utils.gpioUtils import GPIOUtils


class LEDSwitchController(Resource):
    session_manager = {}

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Set the LED to a 0 or 1 state
    def put(self, state):
        header = request.headers.get("Authorization")

        if self.session_manager.check_auth(header, True):
            if state not in range(0, 2):
                return {"success": "false", "reason": "Bad state given, expected 0 or 1"}, 400
            else:
                GPIOUtils.updateLED(state)
                return {"success": "true", "LEDState": state}, 200
        else:
            return {"success": "false", "reason": "Unauthorized"}, 401
