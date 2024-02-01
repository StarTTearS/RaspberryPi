#include <stdio.h>
#include <wiringPi.h>

#define PIR_PIN 2  // PIR 센서 연결된 GPIO 핀 번호
#define BUZZER_PIN 1  // 부저 연결된 GPIO 핀 번호

int main(void) {
    int pir_val;
    int buzzer_val;

    if (wiringPiSetup() == -1)
        return -1;

    pinMode(PIR_PIN, INPUT);
    pinMode(BUZZER_PIN, OUTPUT);

    printf("PIR Sensor and Buzzer Test\n");

    while (1) {
	pir_val = digitalRead(PIR_PIN);
        if (pir_val ==1) {
	    buzzer_val = 1;
            printf("Motion detected! Buzzing...\n");
            digitalWrite(BUZZER_PIN, buzzer_val);  // 부저 울리기
            delay(1000);  // 1초 동안 부저 울리기
	}
	else { 
	    buzzer_val = 0;
	    printf("Buzzer off\n");
            digitalWrite(BUZZER_PIN, buzzer_val);   // 부저 끄기
            delay(500);  // 0.5초 대기
        }

        delay(100);  // 0.1초 대기
	}
    return 0;
}

