#include <stdio.h>
#include <wiringPi.h>

PI_THREAD(blink_led) {
        const int led_pin = 7;

        pinMode(led_pin, OUTPUT);

        while(1) {
                digitalWrite(led_pin, HIGH);
                delay(500);
                digitalWrite(led_pin, LOW);
                delay(500);
        }
}
int main(void) {
        wiringPiSetup();

        piThreadCreate(blink_led);

        while(1) {
                printf("main\n");
                delay(1000);
        }
}

