import gpiozero as gpio
import signal
from sys import argv

if argv[1] and argv[1] == "Mock":
    from gpiozero.pins.mock import MockFactory
    gpio.Device.pin_factory = MockFactory()

def IntHandler(*_):
    print("Recieved interrupt, Exiting!")

def main():
    print("Hello from piware!")

    # testing some cool stuff
    led = gpio.LED(18);
    led.blink()

    signal.pause()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, IntHandler)
    main()
    signal.getsignal(signal.SIGINT)
