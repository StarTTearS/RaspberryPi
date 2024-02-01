#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>

#define SW1_PIN 22
#define SW2_PIN 23
#define SW3_PIN 24
#define LED_RED_PIN 4
#define LED_GREEN_PIN 5
#define LED_BLUE_PIN 6
#define BUZZER_PIN 1  // GPIO 18

void play_music(int *scale, int *melody, int *durations, int size, int led_pin);

int main(void) {
    if (wiringPiSetup() == -1) {
        fprintf(stderr, "Failed to initialize wiringPi\n");
        return 1;
    }

    pinMode(SW1_PIN, INPUT);
    pinMode(SW2_PIN, INPUT);
    pinMode(SW3_PIN, INPUT);
    pinMode(LED_RED_PIN, OUTPUT);
    pinMode(LED_GREEN_PIN, OUTPUT);
    pinMode(LED_BLUE_PIN, OUTPUT);
    pinMode(BUZZER_PIN, OUTPUT);

    while (1) {
        if (digitalRead(SW1_PIN) == LOW) {
            printf("SW1 Pressed! Playing Music 1\n");
            int twinkle_scale[] = {262, 294, 330, 349, 392, 440, 494};
            int twinkle_melody[] = {1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1};
            int twinkle_durations[] = {250, 250, 500, 250, 250, 500, 250, 250, 250, 250, 250, 250, 250, 500};
            play_music(twinkle_scale, twinkle_melody, twinkle_durations, sizeof(twinkle_melody) / sizeof(twinkle_melody[0]), LED_RED_PIN);
        } else if (digitalRead(SW2_PIN) == LOW) {
            printf("SW2 Pressed! Playing Music 2\n");
            int school_scale[] = {262, 294, 330, 349, 392, 440, 494};
            int school_melody[] = {5, 5, 6, 6, 5, 5, 3, 5, 5, 3, 3, 2, 5, 5, 6, 6, 5, 5, 3, 5, 3, 2, 3, 1};
            int school_durations[] = {250, 250, 250, 250, 250, 250, 500, 250, 250, 500, 250, 250, 500, 250, 250, 250, 250, 250, 500, 250, 250, 500, 250, 250};
            play_music(school_scale, school_melody, school_durations, sizeof(school_melody) / sizeof(school_melody[0]), LED_GREEN_PIN);
        } else if (digitalRead(SW3_PIN) == LOW) {
            printf("SW3 Pressed! Playing Music 3\n");
            int bike_scale[] = {262, 294, 330, 349, 392, 440, 494};
            int bike_melody[] = {3, 5, 5, 3, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 5, 5, 5, 3, 5, 5, 6, 6, 3, 3, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 5, 5, 1};
            int bike_durations[] = {250, 250, 500, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 500, 250, 250, 500, 250, 250, 500, 250, 250, 250, 250, 250, 250, 250, 500, 250, 250, 250, 500, 250, 250, 500, 250, 250, 250, 250, 250, 250, 250, 250, 500, 250, 250};
            play_music(bike_scale, bike_melody, bike_durations, sizeof(bike_melody) / sizeof(bike_melody[0]), LED_BLUE_PIN);
        }
    }

    return 0;
}

void play_music(int *scale, int *melody, int *durations, int size, int led_pin) {
    for (int i = 0; i < size; ++i) {
        digitalWrite(led_pin, HIGH);
        delayMicroseconds(scale[melody[i]]);
        digitalWrite(led_pin, LOW);
        delayMicroseconds(durations[i] * 1000);
    }
}

