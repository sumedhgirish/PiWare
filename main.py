import gpiozero as gpio
import signal
from sys import argv

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

    # testing some cool stuff
    led = gpio.LED(18);
    led.blink()

    signal.pause()

    if stop:
        led.off()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, IntHandler)
    main()
