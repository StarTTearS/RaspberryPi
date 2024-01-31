import RPi.GPIO as GPIO
import random
import time

LED_RED = 4
LED_GREEN = 5
LED_BLUE = 6

def setup_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_RED, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_BLUE, GPIO.OUT)

def choose_colors():
    return sorted(random.sample(range(3), random.randint(2, 3)))

def print_title():
    print("------------------------------------------------------------------------")
    print("\t\t빛의 삼원색 게임")
    print("\t- 색을 확인하고 합쳐지면 어떤 색이 되는지 맞춰보자 -")
    print("------------------------------------------------------------------------")

def print_choices():
    print("------------------------------------------------------------------------")
    print("1. yellow")
    print("2. magenta")
    print("3. cyan")
    print("4. white")
    print("------------------------------------------------------------------------")

def get_user_answer():
    return int(input("숫자를 입력하세요: "))

def check_answer(selected_colors, user_answer):
    correct_combinations = {
        (0, 1): [1],  # 노랑
        (0, 2): [2],  # 마젠타
        (1, 2): [3],  # 시안
        (0, 1, 2): [4]  # 화이트
    }

    try:
        return user_answer in correct_combinations[tuple(selected_colors)]
    except KeyError:
        return False

def display_colors(selected_colors):
    for color in selected_colors:
        if color == 0:
            GPIO.output(LED_RED, GPIO.HIGH)
        elif color == 1:
            GPIO.output(LED_GREEN, GPIO.HIGH)
        elif color == 2:
            GPIO.output(LED_BLUE, GPIO.HIGH)

def clear_leds():
    for led_pin in [LED_RED, LED_GREEN, LED_BLUE]:
        GPIO.output(led_pin, GPIO.LOW)

def blink_leds():
    for _ in range(3):
        GPIO.output(LED_RED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_RED, GPIO.LOW)
        time.sleep(0.5)

def main():
    setup_leds()
    print_title()

    try:
        while True:
            selected_colors = choose_colors()
            display_colors(selected_colors)
            print_choices()
            user_answer = get_user_answer()
            clear_leds()

            if check_answer(selected_colors, user_answer):
                print("정답입니다!")
                for color in [0, 1, 2]:
                    if color == 0:
                        GPIO.output(LED_RED, GPIO.HIGH)
                    elif color == 1:
                        GPIO.output(LED_GREEN, GPIO.HIGH)
                    elif color == 2:
                        GPIO.output(LED_BLUE, GPIO.HIGH)
                    time.sleep(0.5)
                    clear_leds()
                    time.sleep(0.5)
            else:
                print("오답입니다.")
                blink_leds()

            # 다음 문제를 위해 초기화
            clear_leds()

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()

