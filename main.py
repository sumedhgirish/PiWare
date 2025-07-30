from core import motors

import gpiozero as gpio
import signal
from sys import argv

# Motor Pins
IN1, IN2, IN3, IN4 = 18, 23, 24, 25

stop = False

match argv:
    case [_, "mock"]:
        from gpiozero.pins.mock import MockFactory
        gpio.Device.pin_factory = MockFactory()

def IntHandler(*_):
    global stop
    stop = True
    print("Recieved interrupt, Exiting!")

def main():
    global stop
    print("Hello from piware!")

    step_cycle = [[1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]][::-1]
    motor = motors.StepperMotor(200, IN1, IN2, IN3, IN4, step_cycle=step_cycle)

    motor.move_angle(180)

    signal.pause()
    if stop:
        motor.close()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, IntHandler)
    main()
