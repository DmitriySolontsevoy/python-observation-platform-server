class ServoAngleStateKeeper:

    __angle = None

    def set_angle(self, angle):
        self.__angle = angle

    def get_angle(self):
        return self.__angle
