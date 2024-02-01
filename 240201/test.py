import RPi.GPIO as GPIO
import time
import spidev

SPI_CH = 0
ADC_CH2 = 2
ADC_CS = 8
SPI_SPEED = 500000
THRESHOLD = 500
LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, SPI_CH)
spi.max_speed_hz = SPI_SPEED

def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    clap_detected = False

    while True:
        adc_value = read_adc(ADC_CH2)
        print(f"Sound ADC Value -> {adc_value}")

        if adc_value > THRESHOLD and not clap_detected:
            clap_detected = True
            print("박수 감지! LED 켜짐.")
            GPIO.output(LED_PIN, GPIO.HIGH)  # LED 켜기
        elif adc_value <= THRESHOLD and clap_detected:
            clap_detected = False
            print("박수 소리 끝. LED 꺼짐.")
            GPIO.output(LED_PIN, GPIO.LOW)  # LED 끄기

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

