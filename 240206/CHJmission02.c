#include <wiringPi.h>
#include <softTone.h>
#include <unistd.h>

#define BUZZER_PIN 1  // WiringPi 번호, BCM_GPIO 18

void playTone(int frequency, int duration) {
    softToneWrite(BUZZER_PIN, frequency);
    delay(duration);
    softToneWrite(BUZZER_PIN, 0);
}

int main(void) {
    if (wiringPiSetup() == -1)
        return 1;

    softToneCreate(BUZZER_PIN);

    // 4옥타브: 도(1)/ 레(2)/ 미(3)/ 파(4)/ 솔(5)/ 라(6)/ 시(7)
    int scale[] = {262, 294, 330, 349, 392, 440, 494};

    // 동요: 학교 종이 땡땡땡 계이름
    int school[] = {5, 5, 6, 6, 5, 5, 3, 5, 5, 3, 3, 2, 5, 5, 6, 6, 5, 5, 3, 5, 3, 2, 3, 1};

    // 재생 간격 추가
    int delayTime = 50;

    for (int i = 0; i < 24; i++) {
        playTone(scale[school[i]], (i == 6 || i == 11 || i == 18 || i == 23) ? 1000 : 500);
        delay(delayTime);
    }

    softToneWrite(BUZZER_PIN, 0);

    return 0;
}

