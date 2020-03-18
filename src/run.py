from flask import Flask
from flask_restful import Api

from src.controllers.servo.horizontalRotationController import HorizontalRotationController
from src.controllers.led.ledSwitchController import LEDSwitchController
from src.controllers.led.ledTickController import LEDTickController
from src.controllers.auth.loginController import LoginController
from src.controllers.servo.verticalRotationController import VerticalRotationController
from src.session.sessionManager import SessionManager


class Server:
    server = Flask(__name__)
    handlers = Api(server)

    def __init__(self):
        session_manager = SessionManager()
        self.handlers.add_resource(HorizontalRotationController, "/api/rotateX/<int:angle>",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(VerticalRotationController, "/api/rotateY/<int:angle>",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(LoginController, "/api/login",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(LEDSwitchController, "/api/switchLED/<int:state>",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(LEDTickController, "/api/tickLED",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.server.run(host='0.0.0.0', port='1337')


if __name__ == '__main__':
    Server()
