import RPi.GPIO as GPIO
import time

buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)  # 초기 주파수를 1Hz로 설정
pwm.start(30.0)  # 듀티비를 90%로 높여 설정함(음 구분이 더 잘되고 조금 더 부드럽게 들림)

# 동요: 자전거
# 미솔솔 미솔솔 라라 라라라 솔솔솔솔 파파파파 미미미미미 미솔 솔솔 미 솔솔 라라 미미솔 파파파파 미미미미 레레 솔솔도

# 4옥타브: 도(1)/ 레(2)/ 미(3)/ 파(4)/ 솔(5)/ 라(6)/ 시(7)
scale = [262, 294, 330, 349, 392, 440, 494]

school = [3, 5, 5, 3, 5, 5, 6, 6, 6, 6, 6,
	5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3,
	3, 5, 5, 5, 3, 5, 5, 6, 6, 3, 3, 5,
	4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 5, 5, 1]

try:
    for i in range(0, 49):
        pwm.ChangeFrequency(scale[school[i]])
        if i == 2 or i == 5 or i == 10 or i == 23 or i ==30 or i == 35 or i == 48:
            time.sleep(1.0)  # 2분음표 부분을 모두 1초로 출력
        else:
            time.sleep(0.5)  # 기타 4분음표는 모두 0.5초로 출력함

finally:
    pwm.stop()
    GPIO.cleanup()

