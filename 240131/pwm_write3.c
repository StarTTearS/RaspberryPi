#include <stdio.h>
#include <wiringPi.h>

int main(void) {
        const int led_pin = 1;

        wiringPiSetup();

        pinMode(led_pin, PWM_OUTPUT);

        while(1) {
                int t_high;
                for(t_high = 0; t_high <= 1024; t_high++) {
                        pwmWrite(led_pin, t_high);
                        delay(1);
                }
        }
}

