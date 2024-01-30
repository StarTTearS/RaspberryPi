import RPi.GPIO as GPIO
import time

LED_RED = 4
LED_GREEN = 5
LED_BLUE = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

GPIO.output(LED_RED, 0)
GPIO.output(LED_GREEN, 0)
GPIO.output(LED_BLUE, 0)

print("3 Color LED Control Start !!")

for i in range(1, 21):
    print(f"Count : {i} \n\nRed LED On !!")
    GPIO.output(LED_RED, 1)
    time.sleep(0.5)
    print("Red LED Off !! \nGreen LED On !!")
    GPIO.output(LED_RED, 0)
    GPIO.output(LED_GREEN, 1)
    time.sleep(0.5)
    print("Green LED Off !! \nBlue LED On !!")
    GPIO.output(LED_GREEN, 0)
    GPIO.output(LED_BLUE, 1)
    time.sleep(0.5)
    print("Blue LED Off !!\n\n\n\n")
    GPIO.output(LED_BLUE, 0)

GPIO.cleanup()

