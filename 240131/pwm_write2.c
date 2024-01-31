#include<stdio.h>
#include<wiringPi.h>
int main(){
	const int led_pin = 1;

	wiringPiSetup();

	pinMode(led_pin, PWM_OUTPUT);
	pwmWrite(led_pin, 1000);
}

