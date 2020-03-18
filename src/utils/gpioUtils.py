from gpiozero import LED
from time import sleep

led = LED(17)


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
