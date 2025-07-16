import gpiozero as gpio

def main():
    print("Hello from piware!")

    # testing some cool stuff
    led = gpio.LED(18);
    try:
        led.blink()
        while True:
            pass
    except (KeyboardInterrupt, EOFError):
        print("Exiting")


if __name__ == "__main__":
    main()
