from flask_restful import Resource
from flask import request
from utils.gpsUtils import GPSUtils
from serial import SerialException


class GPSController(Resource):

    def __init__(self, session_manager):
        self.session_manager = session_manager

    # Get coordinates
    def get(self):
        error, code = self.session_manager.check_auth_admin(request)

        if error is None:
            try:
                latitude, longitude = GPSUtils.get_coordinates()
                return {"success":"true", "latitude":latitude, "longitude": longitude}, 200
            except ValueError:
                return {"success":"false", "reason":"GPS signal is too weak"}, 523
            except SerialException:
                return {"success":"false", "reason":"GPS module isn't present"}, 503
