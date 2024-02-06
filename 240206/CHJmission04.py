import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
button_pins = [22, 23, 24]
motor_pins = [16, 17, 18, 19]

# 버튼 상태 및 마지막으로 눌린 버튼 저장
button_states = [GPIO.LOW] * len(button_pins)
last_button_pressed = None

# 스텝 모터 시퀀스
motor_seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# 버튼 콜백 함수
def button_callback(channel):
    global last_button_pressed

    button_index = button_pins.index(channel)
    button_states[button_index] = not button_states[button_index]

    # 버튼이 눌릴 때마다 출력 및 회전
    if button_states[button_index]:
        last_button_pressed = button_index
        print(f"Button {button_index + 1} pressed!")

        if button_index == 0:
            print("1번 스위치: 45도 회전\n")
            rotate_motor(45)
        elif button_index == 1:
            print("2번 스위치: 90도 회전\n")
            rotate_motor(90)
        elif button_index == 2:
            print("3번 스위치: 180도 회전\n")
            rotate_motor(180)

        # 버튼 상태 초기화
        button_states[button_index] = False

# 스텝 모터 회전 함수
def rotate_motor(degrees):
    # 1 스텝 당 시간 (조절이 필요할 수 있음)
    step_delay = 0.001

    # 회전 각도에 따라 스텝 수 계산
    steps = int(degrees / 0.9)

    # 회전
    for _ in range(steps):
        for i in range(8):
            for pin in range(4):
                GPIO.output(motor_pins[pin], motor_seq[i][pin])
            time.sleep(step_delay)

# GPIO 설정
GPIO.setmode(GPIO.BCM)

# 버튼 및 모터 핀 설정
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_callback, bouncetime=300)

for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

