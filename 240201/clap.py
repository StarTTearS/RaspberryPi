import RPi.GPIO as GPIO
import time
import spidev

SPI_CH = 0
ADC_CH2 = 2
ADC_CS = 8
SPI_SPEED = 500000
THRESHOLD = 500

buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
pwm = GPIO.PWM(buzzer_pin, 1.0)
pwm.start(50.0)

spi = spidev.SpiDev()
spi.open(0, SPI_CH)
spi.max_speed_hz = SPI_SPEED

def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    print("Waiting for 3 seconds...")
    time.sleep(3)  # 3-second delay

    while True:
        adc_value = read_adc(ADC_CH2)
        print(f"Sound ADC Value -> {adc_value}")

        if adc_value > THRESHOLD:
            scale = [262, 294, 330, 349, 392, 440, 494, 523]
            
            for i in range(8):
                pwm.ChangeFrequency(scale[i])
                time.sleep(1.0)

            for i in range(7, 0, -1):
                pwm.ChangeFrequency(scale[i])
                time.sleep(1.0)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()

