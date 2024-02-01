import RPi.GPIO as GPIO
import time

SW1_PIN = 22  # SW1이 연결된 GPIO 핀 번호
SW2_PIN = 23  # SW2이 연결된 GPIO 핀 번호
SW3_PIN = 24  # SW3이 연결된 GPIO 핀 번호
LED_RED_PIN = 4  # LED-Red가 연결된 GPIO 핀 번호
LED_GREEN_PIN = 5  # LED-Green이 연결된 GPIO 핀 번호
LED_BLUE_PIN = 6  # LED-Blue가 연결된 GPIO 핀 번호
BUZZER_PIN = 18  # 부저가 연결된 GPIO 핀 번호

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_RED_PIN, GPIO.OUT)
GPIO.setup(LED_GREEN_PIN, GPIO.OUT)
GPIO.setup(LED_BLUE_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PIN, 1.0)
pwm.start(10.0)

def play_music(scale, melody, led_pin, duration_list):
    try:
        GPIO.output(led_pin, GPIO.HIGH)  # LED 켜기

        for i in range(len(melody)):
            pwm.ChangeFrequency(scale[melody[i]])
            time.sleep(duration_list[i])

    finally:
        GPIO.output(led_pin, GPIO.LOW)  # LED 끄기

# ==동요1 : 반짝 반짝 작은별 계이름 ==
twinkle_scale = [262, 294, 330, 349, 392, 440, 494]
twinkle_melody = [1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1]
twinkle_durations = [0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5]

# 동요2: 학교 종이 땡땡땡 계이름
school_scale = [262, 294, 330, 349, 392, 440, 494]
school_melody = [5, 5, 6, 6, 5, 5, 3, 5, 5, 3, 3, 2, 5, 5, 6, 6, 5, 5, 3, 5, 3, 2, 3, 1]
school_durations = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25]

# 동요3: 자전거
bike_scale = [262, 294, 330, 349, 392, 440, 494]
bike_melody = [3, 5, 5, 3, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 5, 5, 5, 3, 5, 5, 6, 6, 3, 3, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 5, 5, 1]
bike_durations = [0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25]

try:
    while True:
        if GPIO.input(SW1_PIN) == GPIO.LOW:
            print("SW1 Pressed! Playing Music 1")
            play_music(twinkle_scale, twinkle_melody, LED_RED_PIN, twinkle_durations)

        elif GPIO.input(SW2_PIN) == GPIO.LOW:
            print("SW2 Pressed! Playing Music 2")
            play_music(school_scale, school_melody, LED_GREEN_PIN, school_durations)

        elif GPIO.input(SW3_PIN) == GPIO.LOW:
            print("SW3 Pressed! Playing Music 3")
            play_music(bike_scale, bike_melody, LED_BLUE_PIN, bike_durations)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

