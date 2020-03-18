class ValidationHelper:

    @staticmethod
    def validate_horizontal_servo_angle(angle):
        if angle not in range(0, 181):
            return {"success": "false", "reason": "Bad angle given, expected from 0 to 180 degrees"}, 400
        else:
            return None, None

    @staticmethod
    def validate_vertical_servo_angle(angle):
        if angle not in range(0, 91):
            return {"success": "false", "reason": "Bad angle given, expected from 0 to 90 degrees"}, 400
        else:
            return None, None

    @staticmethod
    def validate_led_state_parameter(state):
        if state not in range(0, 2):
            return {"success": "false", "reason": "Bad state given, expected 0 or 1"}, 400
        else:
            return None, None

    @staticmethod
    def validate_tick_led_parameters(period_duration, period_count):
        if period_duration < 0.1:
            return {"success": "false", "reason": "Period of blinking is to short (Expected >= 0.1ms)"}, 400
        elif period_count not in range(0, 51):
            return {"success": "false", "reason": "Number of period is invalid (50 >= Expected > 0)"}, 400
        else:
            return None, None
