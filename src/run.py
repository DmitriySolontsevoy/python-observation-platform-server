from flask import Flask
from flask_restful import Api

from src.controllers.horizontalRotationController import HorizontalRotationController
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
        self.server.run(port='1337')


if __name__ == '__main__':
    Server()
