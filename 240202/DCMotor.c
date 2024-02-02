#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>
#define DC_INA 26
#define DC_INB 23
int main(void){
        int direction,i;
        if(wiringPiSetup () == -1)
                return 1;
        pinMode(DC_INA,OUTPUT);
        pinMode(DC_INB,OUTPUT);
        digitalWrite(DC_INA,0);
        digitalWrite(DC_INB,0);
        printf("DC motor Control Start !! \n");
        while(1){
        printf("1. forward, 2. reverse 3.exit \n select : ");
                scanf("%d",&direction);
                if(direction==1){
                        printf("forward Selected !!\n");
                        for(i=0; i<5;i++){
                                digitalWrite(DC_INB,1);
                                sleep(1);
                                digitalWrite(DC_INB,0);
                                sleep(1);
                        }
                } else if(direction==2){
                        printf("reverse Selected !!\n");
                        for(i=0; i<5; i++){
                                digitalWrite(DC_INA,1);
                                sleep(1);
                                digitalWrite(DC_INA,0);
                                sleep(1);
                        }
                }else if(direction==3){
                        printf("exit Selected !!\n");
                        break;
                }
        }
        return 0;
}

