from lcd1602 import LCD
import utime

lcd = LCD()
string = "Hello\n"
lcd.message(string)
utime.sleep(2)
string = "Tracy"
lcd.message(string)
utime.sleep(5)
lcd.clear()
