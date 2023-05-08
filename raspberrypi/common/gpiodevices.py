
#from RPi.GPIO import GPIO
import RPi.GPIO as GPIO
from gpiozero import Button


class gpio_pins():
    INTER_1_PIN = 18
    INTER_2_PIN = 12
    INTER_3_PIN = 6
    INTER_4_PIN = 5
    LED1_PIN = 12
    LED2_PIN = 4
    LED3_PIN = 21
    LED4_PIN = 16

    ALED2_PIN = 17
    ALED3_PIN = 25
    ALED1_PIN = 24

    TIRETTE_PIN = 26
    URGENCE_PIN = 20
    DEV_MODE_PIN = 22

class Device:
    list_pin = [False] * 59


class Switch(Device):
    def launch_function(self):
        if self.function:
            self.function(*self.args, **self.kwargs)

    def __init__(self, input_pin, function=None, active_high=True, *args, **kwargs):
        if not Device.list_pin[input_pin]:
            self.function = function
            self.state = False
            Device.list_pin[input_pin] = True
            self.args = args
            self.kwargs = kwargs
            self.input_pin = input_pin
            self.button = Button(input_pin, pull_up=True)
            self.set_active_high(active_high)

        else:
            raise RuntimeError('pin already in use')

    def set_function(self, function, *args, **kwargs):
        self.function = function
        self.kwargs = kwargs
        self.args = args

    def set_active_high(self, active_high):
        if active_high:
            self.button.when_pressed = self.launch_function
            self.button.when_released = None
        else:
            self.button.when_pressed = None
            self.button.when_released = self.launch_function

    def close(self):
        Device.list_pin[self.input_pin] = False
        self.button.close()


class LightButton(Device):
    def __init__(self, input_pin, light_pin, function=None, *args, **kwargs):
        if not Device.list_pin[input_pin] and not Device.list_pin[light_pin]:
            self.function = function
            self.state = False
            Device.list_pin[input_pin] = True
            Device.list_pin[light_pin] = True
            self.auto_switch = False
            self.args = args
            self.kwargs = kwargs
            self.input_pin = input_pin
            self.light_pin = light_pin
            
            if GPIO.getmode() != GPIO.BCM:
                GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(self.light_pin, GPIO.OUT)
            GPIO.add_event_detect(
                self.input_pin, GPIO.FALLING, callback=self.launch_function, bouncetime=500)
            
        else:
            raise RuntimeError('pin already in use')

    def launch_function(self, *args):
        if self.function:
            self.function(*self.args, **self.kwargs)

        if self.auto_switch:
            self.switch()

    def set_auto_switch(self, value):
        self.auto_switch = value

    def on(self):
        self.state = True
        GPIO.output(self.light_pin, GPIO.HIGH)

    def off(self):
        self.state = False
        GPIO.output(self.light_pin, GPIO.LOW)

    def switch(self):
        if not self.state:
            self.on()
        else:
            self.off()

    def set_function(self, function, *args, **kwargs):
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def close(self):
        Device.list_pin[self.input_pin] = False
        GPIO.remove_event_detect(self.input_pin)
        GPIO.cleanup(self.input_pin)

        Device.list_pin[self.light_pin] = False
        GPIO.cleanup(self.light_pin)

if __name__ == "__main__":
    from time import sleep
    btn1 = LightButton(gpio_pins.INTER_1_PIN, gpio_pins.LED1_PIN, None)
    btn1.set_function(btn1.switch())
    btn1.on()

    tirette = Switch(gpio_pins.TIRETTE_PIN, print("Tirette"), True)
    
    while 1:
        print(tirette.button.is_pressed())
        sleep(0.1)