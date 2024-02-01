import RPi.GPIO as GPIO
import time

buzzer = 18
button_start_pin = 15  # 시작 버튼과 연결된 핀
button_stop_pin = 16  # 정지 버튼과 연결된 핀

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(button_start_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 풀업 저항 사용
GPIO.setup(button_stop_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 풀업 저항 사용

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(10.0)  # Duty Cycle을 10으로 설정

# 상어 가족 동요 음표와 스타카토 효과 적용
shark_song = [
    (4, 0.25), (4, 0.25), (0, 0.25), (5, 0.25), (5, 0.25), (0, 0.25),
    (6, 0.25), (6, 0.25), (6, 0.25), (6, 0.25), (0, 0.25), (5, 0.25), (5, 0.25), (0, 0.25),
    (6, 0.25), (6, 0.25), (0, 0.25), (5, 0.25), (5, 0.25), (0, 0.25),
    (4, 0.25), (4, 0.25), (0, 0.25), (5, 0.25), (5, 0.25), (0, 0.25),
    (6, 0.5), (6, 0.25), (6, 0.25), (6, 0.25), (6, 0.25), (0, 0.25),
    (5, 0.25), (5, 0.25), (0, 0.25), (6, 0.25), (6, 0.25), (0, 0.25),
    (5, 0.25), (5, 0.25), (0, 0.25), (4, 0.25), (4, 0.25), (0, 0.25),
    (5, 0.25), (5, 0.25), (0, 0.25), (4, 0.25), (4, 0.25), (0, 0.25),
    (3, 0.25), (3, 0.25), (0, 0.25), (1, 0.25), (1, 0.25), (0, 0.25),
    (6, 1.0),
    (6, 0.25), (6, 0.25), (6, 0.25), (6, 0.25), (0, 0.25),
    (5, 0.25), (5, 0.25), (0, 0.25), (6, 0.25), (6, 0.25), (0, 0.25),
    (5, 0.25), (5, 0.25), (0, 0.25), (4, 0.25), (4, 0.25), (0, 0.25),
    (5, 0.25), (5, 0.25), (0, 0.25), (4, 0.25), (4, 0.25), (0, 0.25),
    (3, 0.25), (3, 0.25), (0, 0.25), (1, 0.25), (1, 0.25), (0, 0.25),
]

# 음표에 해당하는 주파수
note_freq = {
    1: 261,  # 도
    2: 294,  # 레
    3: 330,  # 미
    4: 349,  # 파
    5: 392,  # 솔
    6: 440,  # 라
}

playing = False  # 노래 재생 여부

def play_song():
    global playing
    playing = True
    pwm.ChangeDutyCycle(90.0)  # Duty Cycle을 90으로 변경
    for note, duration in shark_song:
        if not playing:
            break
        if note != 0:
            pwm.ChangeFrequency(note_freq[note])
        time.sleep(duration)

def stop_song():
    global playing
    playing = False
    pwm.ChangeDutyCycle(10.0)  # Duty Cycle을 10으로 변경

try:
    while True:
        button_start_state = GPIO.input(button_start_pin)
        button_stop_state = GPIO.input(button_stop_pin)

        if button_start_state == GPIO.LOW and not playing:
            play_song()
        elif button_stop_state == GPIO.LOW and playing:
            stop_song()

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()

