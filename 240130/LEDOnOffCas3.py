import RPi.GPIO as GPIO
import time

led_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    for t_high in range(11):
        cnt = 0
        while True:
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(t_high / 1000)  # 초 단위로 변환
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep((10 - t_high) / 1000)  # 초 단위로 변환
            
            cnt += 1
            if cnt == 100:
                break

