import gpiozero as gpio
from signal import pause

from gpiozero.output_devices import PiGPIOFactory

factory = PiGPIOFactory()


def main():
    print("Hello from piware!")

    # testing some cool stuff

    led = gpio.LED(18, pin_factory=factory);
    led.blink()
    pause()


if __name__ == "__main__":
    main()
