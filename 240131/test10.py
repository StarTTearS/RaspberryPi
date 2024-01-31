import RPi.GPIO as GPIO
import time

buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)  # 초기 주파수를 1Hz로 설정
pwm.start(90.0)  # 듀티비를 90%로 높여 설정함(음 구분이 더 잘되고 조금 더 부드럽게 들림)

# 동요: 반짝 반짝 작은별 계이름
# 도도솔솔라라솔파파미미레레도 솔솔파파미미레 솔솔파파미미레 도도솔솔라라솔파파미미레레도

# 4옥타브: 도(1)/ 레(2)/ 미(3)/ 파(4)/ 솔(5)/ 라(6)/ 시(7)
scale = [262, 294, 330, 349, 392, 440, 494]

twinkle = [1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1,
           5, 5, 4, 4, 3, 3, 2, 5, 5, 4, 4, 3, 3, 2,
           1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1]

try:
    for i in range(0, 42):
        pwm.ChangeFrequency(scale[twinkle[i]])
        if i == 6 or i == 13 or i == 20 or i == 27 or i == 34 or i == 41:
            time.sleep(1.0)  # 2분음표 부분을 모두 1초로 출력
        else:
            time.sleep(0.5)  # 기타 4분음표는 모두 0.5초로 출력함

finally:
    pwm.stop()
    GPIO.cleanup()

