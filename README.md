# Self Driving RC Car
This repository houses all of the software/instructions, as well as schematics, that will allow you to turn an ordinary RC car into a "smart" self-driving car 🤓. The car is capable of autonomously detecting the bounds of the road

All of the software in this project (except for a smidgeon of HTML/CSS/JS) is Python 3.6.0.

##Things you'll need
Below is the list of parts that I used to make this project happen.
#### Hardware/Electrical
- Raspberry Pi
- Raspberry Pi camera ([case](https://www.amazon.ca/gp/product/B00IJZK66G/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1) is recommended)
- Lots of jumper cables (male to male & male to female)
- Half breadboard [L293D](http://www.robotshop.com/ca/en/600-ma-dual-h-bridge-motor-driver-dc-steppers-l293d.html) H-Bridge Motor Driver
- [HC-SR04](http://www.robotshop.com/ca/en/hc-sr04-ultrasonic-range-finder.html) Ultrasonic Range Finder
- Resistors: 330Ω and 470Ω
- RC Car - I used one like [this](https://www.amazon.ca/gp/product/B00A9NJHS4/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)

**Note on the Raspberry Pi**: I used the Model 2B but the 3 has since come out, either or should work for this project. I would recommend the 3 as you don't need to worry about purchasing an extra WiFi dongle. A kit like [this](https://www.amazon.ca/CanaKit-Raspberry-Complete-Starter-Kit/dp/B01CCF6V3A/ref=sr_1_3?s=electronics&ie=UTF8&qid=1491049831&sr=1-3&keywords=raspberry+pi+2+model+b) is probably best as it comes with a case, preinstalled SD, etc. For this walkthrough I'll make the assumption that you already have a functioning, WiFi connected Pi.

**Note on the RC Car**: If you're crafty you really don't need to purchase an RC car. Essentially you'll be "tearing the guts" out of the car down to just the DC motor that controls forwards/reverse, servo that controls left/right, and the chassis. You could build a car with a kit like [this](https://www.amazon.ca/JOSYOO-4-wheel-Chassis-Encoder-Arduino/dp/B0116UY41I/ref=sr_1_1?s=electronics&ie=UTF8&qid=1491050965&sr=1-1&keywords=robot+car) for cheaper but I decided not to focus on that (at least for now).

#### Tools
- Electrical tape
- A small screwdriver set like [this](https://www.amazon.ca/TEKTON-2985-Jewelers-Precision-Screwdriver/dp/B000NY6Q8S/ref=sr_1_1?ie=UTF8&qid=1491053451&sr=8-1&keywords=small+screwdriver+set) comes in handy
- Soldering Iron Kit (optional)
- Wire-stripper (or if you don't have this a box-cutter/knife will do the trick)

**Note on soldering**: soldering isn't *really* necessary for this project, although it's a temporary solution. If you're a noob at soldering like me, you can just strip your wires back, inter-twine the cooper and throw some electrical tape on it.

## Wiring things up
![Schematic](/schematics/schematic.png?raw=true)
**Note**: [Fritzing](http://fritzing.org/download/) schematic can be found [here](/schematics/self_driving_car.fzz).

## Testing out our connections
...test scripts to make sure everything works fine

## To-do list
- [x] Get materials
- [x] Control rear DC motor from Pi
- [ ] Control front DC motor from Pi
- [ ] Control HC-SR04 from Pi
- [x] Create schematic
- [ ] Stream video to Mac from Pi camera
- [ ] Connect to web server running on Pi
- [ ] Drive car from Mac
- [ ] Collect data
...

## References
- Connecting an [HC-SR04](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)
- Connecting an [L293D](http://www.rhydolabz.com/wiki/?p=11288)
- Connecting an [SG-5010](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/hardware)
