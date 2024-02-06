#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>
#define LED_RED 7
#define LED_GREEN 21
#define LED_BLUE 22
int main(void){
        int i;
        if(wiringPiSetup () == -1)
                return 1;
        pinMode(LED_RED,OUTPUT);
        pinMode(LED_GREEN,OUTPUT);
        pinMode(LED_BLUE,OUTPUT);
        digitalWrite(LED_RED,0);
        digitalWrite(LED_GREEN,0);
        digitalWrite(LED_BLUE,0);
        printf("3 Color LED Control Start !! \n");
         for(i=0;i<10;i++){
                printf("LED On !! \n");
                digitalWrite(LED_RED,1);
                digitalWrite(LED_GREEN,1);
                digitalWrite(LED_BLUE,1);	  
                usleep(500000);
                printf("LED Off !! \n");
                digitalWrite(LED_RED,0);
                digitalWrite(LED_GREEN,0);
                digitalWrite(LED_BLUE,0);
                usleep(500000);
        }
        return 0;
}

