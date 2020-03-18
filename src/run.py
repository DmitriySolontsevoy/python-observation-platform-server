from flask import Flask
from flask_restful import Api

from src.controllers.horizontalRotationController import HorizontalRotationController
from src.controllers.ledSwitchController import LEDSwitchController
from src.controllers.ledTickController import LEDTickController
from src.controllers.loginController import LoginController
from src.controllers.verticalRotationController import VerticalRotationController
from src.session.SessionManager import SessionManager


class Server:
    server = Flask(__name__)
    handlers = Api(server)

    def __init__(self):
        session_manager = SessionManager()
        self.handlers.add_resource(HorizontalRotationController, "/api/rotateX/<string:angle>",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(VerticalRotationController, "/api/rotateY/<string:angle>",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(LoginController, "/api/login",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(LEDSwitchController, "/api/switchLED/<int:state>",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.handlers.add_resource(LEDTickController, "/api/tickLED/<float:period_duration>/<int:period_count>",
                                   resource_class_kwargs={'session_manager': session_manager})
        self.server.run(host='0.0.0.0', port='1337')


if __name__ == '__main__':
    Server()
