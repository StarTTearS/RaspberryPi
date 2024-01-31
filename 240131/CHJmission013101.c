#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define LED_RED 4
#define LED_GREEN 5
#define LED_BLUE 6

void setup_leds() {
    // GPIO 초기화 및 LED 핀 설정
    // 이 부분은 Raspberry Pi의 WiringPi 라이브러리를 사용하는 것을 가정하고 있습니다.
    // WiringPi 라이브러리에 대한 헤더 파일을 include하고 초기화 코드를 작성해야 합니다.
    // https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/
}

void choose_colors(int *selected_colors, int *count) {
    // 랜덤하게 2개 또는 3개의 색상 선택
    srand(time(NULL));
    *count = rand() % 2 + 2;  // 2 또는 3
    for (int i = 0; i < *count; ++i) {
        selected_colors[i] = rand() % 3;  // 0부터 2까지의 랜덤한 색상 선택
    }
}

void print_title() {
    // 타이틀 출력
    printf("------------------------------------------------------------------------\n");
    printf("\t\t빛의 삼원색 게임\n");
    printf("\t- 색을 확인하고 합쳐지면 어떤 색이 되는지 맞춰보자 -\n");
    printf("------------------------------------------------------------------------\n");
}

void print_choices() {
    // 선택창 출력
    printf("------------------------------------------------------------------------\n");
    printf("1. yellow\n");
    printf("2. magenta\n");
    printf("3. cyan\n");
    printf("4. white\n");
    printf("------------------------------------------------------------------------\n");
}

int get_user_answer() {
    // 사용자에게 숫자 입력 받기
    int number;
    printf("숫자를 입력하세요: ");
    scanf("%d", &number);
    return number;
}

int check_answer(int *selected_colors, int count, int user_answer) {
    // 정답 확인
    int correct_combinations[3][3] = {
        {1},   // 노랑
        {2},   // 마젠타
        {3}    // 시안
    };

    if (count == 3) {
        correct_combinations[0][1] = correct_combinations[0][2] = correct_combinations[1][2] = 4;  // 화이트
    }

    for (int i = 0; i < count; ++i) {
        if (user_answer == correct_combinations[selected_colors[i]][selected_colors[(i + 1) % count]]) {
            return 1;  // 정답
        }
    }

    return 0;  // 오답
}

void display_colors(int *selected_colors, int count) {
    // LED에 색상 출력
    // WiringPi 라이브러리의 digitalWrite 함수를 사용하여 LED를 켜고 끄는 코드를 작성해야 합니다.
}

void clear_leds() {
    // 모든 LED 끄기
}

void blink_leds() {
    // 빨간 LED 3번 깜빡이기
}

void main_game() {
    setup_leds();
    print_title();

    while (1) {
        int selected_colors[3];
        int count;
        choose_colors(selected_colors, &count);
        display_colors(selected_colors, count);
        print_choices();
        int user_answer = get_user_answer();
        clear_leds();

        if (check_answer(selected_colors, count, user_answer)) {
            printf("정답입니다!\n");
            for (int i = 0; i < 3; ++i) {
                display_colors(selected_colors, count);
                sleep(1);  // 1초 동안 LED를 켜두고
                clear_leds();
                sleep(1);  // 1초 동안 LED를 끄기
            }
        } else {
            printf("오답입니다.\n");
            blink_leds();
        }

        // 다음 문제를 위해 초기화
        clear_leds();
    }
}

int main() {
    main_game();
    return 0;
}

