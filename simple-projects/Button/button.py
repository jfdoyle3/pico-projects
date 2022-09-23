import machine
import utime

button = machine.Pin(14, machine.Pin.IN)
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
    print(str(button.value()))
    if button.value() == 1:
        led_onboard.value(0)
        # When the button is pressed, GPIO will be connected to GND.
        print("Button is up!")
    utime.sleep(1)
    if(button.value())==0:
        led_onboard.value(1)
        print("Button is down!")
        

