#include <wiringPi.h>
#include <stdio.h>

// GPIO 핀 번호 설정
#define BUTTON1_PIN 3
#define BUTTON2_PIN 4
#define BUTTON3_PIN 5

#define MOTOR1_PIN 27
#define MOTOR2_PIN 0
#define MOTOR3_PIN 1
#define MOTOR4_PIN 24

// 스텝 모터 시퀀스
int motorSeq[8][4] = {
    {1, 0, 0, 1},
    {1, 0, 0, 0},
    {1, 1, 0, 0},
    {0, 1, 0, 0},
    {0, 1, 1, 0},
    {0, 0, 1, 0},
    {0, 0, 1, 1},
    {0, 0, 0, 1}
};

// 버튼 상태 및 마지막으로 눌린 버튼 저장
int buttonStates[3] = {0};
int lastButtonPressed = -1;

// 스텝 모터 회전 함수
void rotateMotor(int degrees) {
    // 1 스텝 당 시간 (조절이 필요할 수 있음)
    int stepDelay = 1000;

    // 회전 각도에 따라 스텝 수 계산
    int steps = (int)(degrees / 0.9);

    // 회전
    for (int step = 0; step < steps; step++) {
        for (int i = 0; i < 8; i++) {
            for (int pin = 0; pin < 4; pin++) {
                digitalWrite(MOTOR1_PIN, motorSeq[i][0]);
                digitalWrite(MOTOR2_PIN, motorSeq[i][1]);
                digitalWrite(MOTOR3_PIN, motorSeq[i][2]);
                digitalWrite(MOTOR4_PIN, motorSeq[i][3]);
            }
            delayMicroseconds(stepDelay);
        }
    }
}

// 버튼 콜백 함수
void buttonCallback(void) {
    // 버튼이 눌릴 때마다 출력 및 회전
    int buttonIndex = -1;

    if (digitalRead(BUTTON1_PIN) == LOW) {
        buttonIndex = 0;
    } else if (digitalRead(BUTTON2_PIN) == LOW) {
        buttonIndex = 1;
    } else if (digitalRead(BUTTON3_PIN) == LOW) {
        buttonIndex = 2;
    }

    if (buttonIndex != -1 && buttonStates[buttonIndex] == 0) {
        lastButtonPressed = buttonIndex;
        printf("Button %d pressed!\n", buttonIndex + 1);

        switch (buttonIndex) {
            case 0:
                printf("1번 스위치: 45도 회전\n\n");
                rotateMotor(45);
                break;
            case 1:
                printf("2번 스위치: 90도 회전\n\n");
                rotateMotor(90);
                break;
            case 2:
                printf("3번 스위치: 180도 회전\n\n");
                rotateMotor(180);
                break;
            default:
                break;
        }

        // 버튼 상태 초기화
        buttonStates[buttonIndex] = 1;
    }
}

int main(void) {
    // WiringPi 초기화
    if (wiringPiSetup() == -1)
        return 1;

    // 버튼 및 모터 핀 설정
    pinMode(BUTTON1_PIN, INPUT);
    pinMode(BUTTON2_PIN, INPUT);
    pinMode(BUTTON3_PIN, INPUT);

    pinMode(MOTOR1_PIN, OUTPUT);
    pinMode(MOTOR2_PIN, OUTPUT);
    pinMode(MOTOR3_PIN, OUTPUT);
    pinMode(MOTOR4_PIN, OUTPUT);

    // 초기화
    digitalWrite(MOTOR1_PIN, LOW);
    digitalWrite(MOTOR2_PIN, LOW);
    digitalWrite(MOTOR3_PIN, LOW);
    digitalWrite(MOTOR4_PIN, LOW);

    // 버튼 인터럽트 설정
    wiringPiISR(BUTTON1_PIN, INT_EDGE_FALLING, &buttonCallback);
    wiringPiISR(BUTTON2_PIN, INT_EDGE_FALLING, &buttonCallback);
    wiringPiISR(BUTTON3_PIN, INT_EDGE_FALLING, &buttonCallback);

    while (1) {
        delay(100);
    }

    return 0;
}

