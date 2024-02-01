#include <wiringPi.h>
#include <softTone.h>
#include <stdio.h>

#define SW1_PIN 3   // SW1이 연결된 GPIO 핀 번호
#define SW2_PIN 4   // SW2이 연결된 GPIO 핀 번호
#define SW3_PIN 5   // SW3이 연결된 GPIO 핀 번호
#define LED_RED_PIN 7   // LED-Red가 연결된 GPIO 핀 번호
#define LED_GREEN_PIN 0 // LED-Green이 연결된 GPIO 핀 번호
#define LED_BLUE_PIN 2  // LED-Blue가 연결된 GPIO 핀 번호
#define BUZZER_PIN 1    // 부저가 연결된 GPIO 핀 번호

void play_music(int *scale, int *melody, int led_pin, float *duration_list, int size) {
    digitalWrite(led_pin, HIGH); // LED 켜기

    for (int i = 0; i < size; ++i) {
        softToneWrite(BUZZER_PIN, scale[melody[i]]);
        delay(duration_list[i] * 1000); // 초를 밀리초로 변환
    }

    digitalWrite(led_pin, LOW); // LED 끄기
}

int main() {
    wiringPiSetup();
    pinMode(SW1_PIN, INPUT);
    pinMode(SW2_PIN, INPUT);
    pinMode(SW3_PIN, INPUT);
    pinMode(LED_RED_PIN, OUTPUT);
    pinMode(LED_GREEN_PIN, OUTPUT);
    pinMode(LED_BLUE_PIN, OUTPUT);
    softToneCreate(BUZZER_PIN);

    // 동요1 : 반짝 반짝 작은별 계이름
    int twinkle_scale[] = {262, 294, 330, 349, 392, 440, 494};
    int twinkle_melody[] = {1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1};
    float twinkle_durations[] = {0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5};

    // 동요2: 학교 종이 땡땡땡 계이름
    int school_scale[] = {262, 294, 330, 349, 392, 440, 494};
    int school_melody[] = {5, 5, 6, 6, 5, 5, 3, 5, 5, 3, 3, 2, 5, 5, 6, 6, 5, 5, 3, 5, 3, 2, 3, 1};
    float school_durations[] = {0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25};

    // 동요3: 자전거
    int bike_scale[] = {262, 294, 330, 349, 392, 440, 494};
    int bike_melody[] = {3, 5, 5, 3, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 5, 5, 5, 3, 5, 5, 6, 6, 3, 3, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 5, 5, 1};
    float bike_durations[] = {0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25};

    while (1) {
        if (digitalRead(SW1_PIN) == LOW) {
            printf("SW1 Pressed! Playing Music 1\n");
            play_music(twinkle_scale, twinkle_melody, LED_RED_PIN, twinkle_durations, sizeof(twinkle_melody) / sizeof(twinkle_melody[0]));
        } else if (digitalRead(SW2_PIN) == LOW) {
            printf("SW2 Pressed! Playing Music 2\n");
            play_music(school_scale, school_melody, LED_GREEN_PIN, school_durations, sizeof(school_melody) / sizeof(school_melody[0]));
        } else if (digitalRead(SW3_PIN) == LOW) {
            printf("SW3 Pressed! Playing Music 3\n");
            play_music(bike_scale, bike_melody, LED_BLUE_PIN, bike_durations, sizeof(bike_melody) / sizeof(bike_melody[0]));
        }
    }

    return 0;
}

