import RPi.GPIO as GPIO
import time

LED_PIN = 4

def initialize_led():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)

def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)

def fade_in(duration):
    pwm_led = GPIO.PWM(LED_PIN, 1000)
    pwm_led.start(0)

    for duty_cycle in range(0, 101, 5):
        pwm_led.ChangeDutyCycle(duty_cycle)
        time.sleep(duration / 20)

    pwm_led.stop()

def fade_out(duration):
    pwm_led = GPIO.PWM(LED_PIN, 1000)
    pwm_led.start(100)

    for duty_cycle in range(100, -1, -5):
        pwm_led.ChangeDutyCycle(duty_cycle)
        time.sleep(duration / 20)

    pwm_led.stop()

def fade_in_out(duration):
    fade_in(duration)
    time.sleep(duration)
    fade_out(duration)

def custom_fade_in_out(seconds):
    fade_in(seconds)
    time.sleep(seconds)
    fade_out(seconds)

def main():
    initialize_led()

    while True:
        print("\nSelect LED function:")
        print("1. LED On")
        print("2. LED Off")
        print("3. LED Fade In (3 seconds)")
        print("4. LED Fade Out (3 seconds)")
        print("5. LED Fade In & Out (6 seconds)")
        print("6. Custom Fade In & Out (input seconds)")
        print("0. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            led_on()
        elif choice == "2":
            led_off()
        elif choice == "3":
            fade_in(3)
        elif choice == "4":
            fade_out(3)
        elif choice == "5":
            fade_in_out(3)
        elif choice == "6":
            seconds = float(input("Enter the duration in seconds: "))
            custom_fade_in_out(seconds)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        GPIO.cleanup()

