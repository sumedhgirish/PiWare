import gpiozero as gpio
from signal import pause

from gpiozero.output_devices import PiGPIOFactory

gpio.Device.pin_factory = PiGPIOFactory("127.0.0.1", "8888")


def main():
    print("Hello from piware!")

    # testing some cool stuff

    led = gpio.LED(18);
    led.blink()
    pause()


if __name__ == "__main__":
    main()
