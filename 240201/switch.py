import RPi.GPIO as GPIO
import time

buzzer = 18
button_pin = 15  # 사용할 GPIO 핀 설정 (버튼과 연결된 핀)

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 풀업 저항 사용

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(10.0)

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
    for note, duration in shark_song:
        if not playing:
            break
        if note != 0:
            pwm.ChangeFrequency(note_freq[note])
        time.sleep(duration)

def stop_song():
    global playing
    playing = False
    pwm.stop()

try:
    while True:
        button_state = GPIO.input(button_pin)

        if button_state == GPIO.LOW and not playing:
            play_song()
        elif button_state == GPIO.LOW and playing:
            stop_song()

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
