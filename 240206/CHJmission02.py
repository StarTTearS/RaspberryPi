import RPi.GPIO as GPIO
import time

buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)  # 초기 주파수를 1Hz로 설정
pwm.start(30.0)  # 듀티비를 90%로 높여 설정함(음 구분이 더 잘되고 조금 더 부드럽게 들림)

# 동요: 학교 종이 땡땡땡 계이름
# 솔솔라라솔솔미 솔솔미미레 솔솔라라솔솔미 솔미레미도

# 4옥타브: 도(1)/ 레(2)/ 미(3)/ 파(4)/ 솔(5)/ 라(6)/ 시(7)
scale = [262, 294, 330, 349, 392, 440, 494]

school = [5, 5, 6, 6, 5, 5, 3,
	5, 5, 3, 3, 2,
	5, 5, 6, 6, 5, 5, 3,
	5, 3, 2, 3, 1]

try:
    for i in range(0, 24):
        pwm.ChangeFrequency(scale[school[i]])
        if i == 6 or i == 11 or i == 18 or i == 23:
            time.sleep(1.0)  # 2분음표 부분을 모두 1초로 출력
        else:
            time.sleep(0.5)  # 기타 4분음표는 모두 0.5초로 출력함

finally:
    pwm.stop()
    GPIO.cleanup()

