import time
from hardware.blinker import Blinker

b = Blinker(4)
b.start_blinking()
time.sleep(20)
b.stop_blinking()