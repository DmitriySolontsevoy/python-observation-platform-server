from src.config.constants import Constants


class Converters:

    @staticmethod
    def to_modulation_width(angle):
        return 1 + angle * Constants.PWM_SG90_DEGREE_WIDTH
