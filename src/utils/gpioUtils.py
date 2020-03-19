from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO

from src.utils.converters import Converters


led = LED(17)
servo_horizontal_pin = 18
servo_vertical_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_horizontal_pin, GPIO.OUT)
GPIO.setup(servo_vertical_pin, GPIO.OUT)


class GPIOUtils:

    @staticmethod
    def updateLED(state):
        if state is 0:
            led.off()
        else:
            led.on()

    @staticmethod
    def blinkLED(period_duration, period_count):
        for i in range(0, period_count):
            led.on()
            sleep(period_duration / 2)
            led.off()
            sleep(period_duration / 2)

    @staticmethod
    def rotate_servo(angle, servo):
        modulation_width = Converters.to_modulation_width(angle)

        if servo == 0:
            servo_chosen = GPIO.PWM(servo_horizontal_pin, 50)
        else:
            servo_chosen = GPIO.PWM(servo_vertical_pin, 50)

        servo_chosen.start(modulation_width)
        sleep(1)
        servo_chosen.stop()
