from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from controllers.servo.horizontalRotationController import HorizontalRotationController
from controllers.led.ledSwitchController import LEDSwitchController
from controllers.led.ledTickController import LEDTickController
from controllers.auth.loginController import LoginController
from controllers.auth.logoutController import LogoutController
from controllers.gps.gpsController import GPSController
from controllers.compass.compassController import CompassController
from controllers.servo.verticalRotationController import VerticalRotationController
from statekeepers.ledStateKeeper import LEDStateKeeper
from session.sessionManager import SessionManager


class Server:
    server = Flask(__name__)
    CORS(server)
    handlers = Api(server)

    def __init__(self):
        session_manager = SessionManager()
        led_state_keeper = LEDStateKeeper()
        self.handlers.add_resource(HorizontalRotationController, "/api/rotateX/<int:angle>",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(VerticalRotationController, "/api/rotateY/<int:angle>",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(LoginController, "/api/login",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(LogoutController, "/api/logout",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(LEDSwitchController, "/api/switchLED/<int:state>",
                                   resource_class_kwargs=
                                   {'session_manager': session_manager, 'led_state_keeper': led_state_keeper})
        self.handlers.add_resource(LEDTickController, "/api/tickLED",
                                   resource_class_kwargs=
                                   {'session_manager': session_manager, 'led_state_keeper': led_state_keeper})
        self.handlers.add_resource(GPSController, "/api/gps",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(CompassController, "/api/compass",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.server.run(host='0.0.0.0', port='1338')


if __name__ == '__main__':
    Server()
