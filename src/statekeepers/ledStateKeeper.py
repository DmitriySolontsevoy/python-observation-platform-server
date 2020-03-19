class LEDStateKeeper:

    __state = None

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state
