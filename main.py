import gpiozero as gpio
from signal import pause

def main():
    print("Hello from piware!")

    # testing some cool stuff
    led = gpio.LED(18);
    led.blink()
    pause()


if __name__ == "__main__":
    main()
