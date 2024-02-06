import RPi.GPIO as GPIO
import time

LED_RED = 4  # GPIO 핀 번호
LED_GREEN = 5  # GPIO 핀 번호
LED_BLUE = 6  # GPIO 핀 번호

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_RED, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_BLUE, GPIO.OUT)

    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.LOW)

    print("3 Color LED Control Start !!")

    for i in range(10):
        print("LED On !!")
        GPIO.output(LED_RED, GPIO.HIGH)
        GPIO.output(LED_GREEN, GPIO.HIGH)
        GPIO.output(LED_BLUE, GPIO.HIGH)
        time.sleep(0.5)

        print("LED Off !!")
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.LOW)
        GPIO.output(LED_BLUE, GPIO.LOW)
        time.sleep(0.5)

    GPIO.cleanup()

if __name__ == "__main__":
    main()
