import RPi.GPIO as GPIO
import time

PIR_PIN = 27  # PIR 센서 연결된 GPIO 핀 번호
BUZZER_PIN = 18  # 부저 연결된 GPIO 핀 번호

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

print("PIR Sensor and Buzzer Test")

try:
    while True:
        motion_detected = GPIO.input(PIR_PIN)

        if motion_detected:
            print("Motion detected! Buzzing...")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # 부저 울리기
            time.sleep(1)  # 1초 동안 부저 울리기
            GPIO.output(BUZZER_PIN, GPIO.LOW)   # 부저 끄기
            time.sleep(0.5)  # 0.5초 대기

        time.sleep(0.1)  # 0.1초 대기

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

