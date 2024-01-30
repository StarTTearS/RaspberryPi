#include <stdio.h> 
#include <wiringPi.h>

#define led_pin 7

int main(void) {

	wiringPiSetup();

	pinMode(led_pin, OUTPUT);

	while(1) {
		digitalWrite(led_pin, HIGH);
		delay(50);
		digitalWrite(led_pin, LOW);
		delay(50);
	}
}

