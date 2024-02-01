#include <wiringPi.h>
#include <softTone.h>
#include <stdio.h>

#define SW1_PIN 22
#define SW2_PIN 23
#define SW3_PIN 24
#define LED_RED_PIN 4
#define LED_GREEN_PIN 5
#define LED_BLUE_PIN 6
#define BUZZER_PIN 1

void play_music(int *scale, int *melody, int led_pin, float *duration_list, int size);

int main(void) {
    if (wiringPiSetup() == -1)
        return 1;

    pinMode(SW1_PIN, INPUT);
    pinMode(SW2_PIN, INPUT);
    pinMode(SW3_PIN, INPUT);
    pinMode(LED_RED_PIN, OUTPUT);
    pinMode(LED_GREEN_PIN, OUTPUT);
    pinMode(LED_BLUE_PIN, OUTPUT);
    softToneCreate(BUZZER_PIN);

    while (1) {
        if (digitalRead(SW1_PIN) == LOW) {
            printf("SW1 Pressed! Playing Music 1\n");
            int twinkle_scale[] = {262, 294, 330, 349, 392, 440, 494};
            int twinkle_melody[] = {1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1};
            float twinkle_durations[] = {0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5};
            play_music(twinkle_scale, twinkle_melody, LED_RED_PIN, twinkle_durations, sizeof(twinkle_melody) / sizeof(twinkle_melody[0]));
        } else if (digitalRead(SW2_PIN) == LOW) {
            printf("SW2 Pressed! Playing Music 2\n");
            int school_scale[] = {262, 294, 330, 349, 392, 440, 494};
            int school_melody[] = {5, 5, 6, 6, 5, 5, 3, 5, 5, 3, 3, 2, 5, 5, 6, 6, 5, 5, 3, 5, 3, 2, 3, 1};
            float school_durations[] = {0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25};
            play_music(school_scale, school_melody, LED_GREEN_PIN, school_durations, sizeof(school_melody) / sizeof(school_melody[0]));
        } else if (digitalRead(SW3_PIN) == LOW) {
            printf("SW3 Pressed! Playing Music 3\n");
            int bike_scale[] = {262, 294, 330, 349, 392, 440, 494};
            int bike_melody[] = {3, 5, 5, 3, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 5, 5, 5, 3, 5, 5, 6, 6, 3, 3, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 5, 5, 1};
            float bike_durations[] = {0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25};
            play_music(bike_scale, bike_melody, LED_BLUE_PIN, bike_durations, sizeof(bike_melody) / sizeof(bike_melody[0]));
        }
    }

    return 0;
}

void play_music(int *scale, int *melody, int led_pin, float *duration_list, int size) {
    digitalWrite(led_pin, HIGH);

    for (int i = 0; i < size; ++i) {
        softToneWrite(BUZZER_PIN, scale[melody[i]]);
        delay(duration_list[i] * 1000);
    }

    digitalWrite(led_pin, LOW);
    softToneWrite(BUZZER_PIN, 0);
}

