import RPi.GPIO as GPIO
import time

buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)   # 초기 주파수를 1Hz로 설정
pwm.start(50.0)               # 듀티비를 50%로 설정

# 4옥타브 주파수 : 도(262)/레(294)/미(330)/파(349)/솔(392)/라(440)/시(494)/도(523)  
scale = [262, 294, 330, 349, 392, 440, 494, 523]

for i in range(0, 8):
    pwm.ChangeFrequency(scale[i])
    time.sleep(1.0)

for i in range(7, -1, -1):
    pwm.ChangeFrequency(scale[i])
    time.sleep(1.0)

pwm.stop()
GPIO.cleanup()

