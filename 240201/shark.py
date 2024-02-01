import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

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

try:
    for note, duration in shark_song:
        if note != 0:
            pwm.ChangeFrequency(note_freq[note])
        time.sleep(duration)

finally:
    pwm.stop()
    GPIO.cleanup()

