#include<wiringPi.h>
#include<stdio.h>

#define led_pin 7

int main(void) {
        int i;

        if(wiringPiSetup() == -1)
                return 1;

        pinMode(led_pin, OUTPUT);
        digitalWrite(led_pin, HIGH);

        return 0;
}

