#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>

#define SW1_PIN 22
#define SW2_PIN 23
#define SW3_PIN 24
#define LED_RED_PIN 4
#define LED_GREEN_PIN 5
#define LED_BLUE_PIN 6
#define BUZZER_PIN 1  // WiringPi 번호, BCM_GPIO 18

// Function Declarations
void playMelody(int *scale, int *melody, int ledPin, float *durationList, int melodyLength);
void waitBuzzer(int duration);

// Melody Definitions
int twinkleScale[] = {262, 294, 330, 349, 392, 440, 494};
int twinkleMelody[] = {1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1};
float twinkleDurations[] = {0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5};

int schoolScale[] = {262, 294, 330, 349, 392, 440, 494};
int schoolMelody[] = {5, 5, 6, 6, 5, 5, 3, 5, 5, 3, 3, 2, 5, 5, 6, 6, 5, 5, 3, 5, 3, 2, 3, 1};
float schoolDurations[] = {0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25};

int bikeScale[] = {262, 294, 330, 349, 392, 440, 494};
int bikeMelody[] = {3, 5, 5, 3, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 5, 5, 5, 3, 5, 5, 6, 6, 3, 3, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 5, 5, 1};
float bikeDurations[] = {0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25};

int main(void) {
    if (wiringPiSetup() == -1)
        return 1;

    pinMode(SW1_PIN, INPUT);
    pinMode(SW2_PIN, INPUT);
    pinMode(SW3_PIN, INPUT);
    pinMode(LED_RED_PIN, OUTPUT);
    pinMode(LED_GREEN_PIN, OUTPUT);
    pinMode(LED_BLUE_PIN, OUTPUT);
    softPwmCreate(BUZZER_PIN, 0, 100);  // 소리 크기 초기화

    while (1) {
        waitBuzzer(2);  // 스위치 입력 전에 부저 깜빡깜빡 대기

        if (digitalRead(SW1_PIN) == LOW) {
            printf("SW1 Pressed! Playing Music 1\n");
            playMelody(twinkleScale, twinkleMelody, LED_RED_PIN, twinkleDurations, sizeof(twinkleMelody) / sizeof(int));
        } else if (digitalRead(SW2_PIN) == LOW) {
            printf("SW2 Pressed! Playing Music 2\n");
            playMelody(schoolScale, schoolMelody, LED_GREEN_PIN, schoolDurations, sizeof(schoolMelody) / sizeof(int));
        } else if (digitalRead(SW3_PIN) == LOW) {
            printf("SW3 Pressed! Playing Music 3\n");
            playMelody(bikeScale, bikeMelody, LED_BLUE_PIN, bikeDurations, sizeof(bikeMelody) / sizeof(int));
        }
    }

    softPwmWrite(BUZZER_PIN, 0);
    return 0;
}

// Function Definitions
void playMelody(int *scale, int *melody, int ledPin, float *durationList, int melodyLength) {
    digitalWrite(ledPin, HIGH);

    for (int i = 0; i < melodyLength; i++) {
        softPwmWrite(BUZZER_PIN, scale[melody[i]]);
        delay(durationList[i] * 1000);
    }

    digitalWrite(ledPin, LOW);
}

void waitBuzzer(int duration) {
    for (int i = 0; i < duration; i++) {
        softPwmWrite(BUZZER_PIN, 50);  // 중간 크기의 소리로 대기
        delay(500);
        softPwmWrite(BUZZER_PIN, 0);  // 부저 끄기
        delay(500);
    }
}

