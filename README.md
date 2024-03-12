# Temperature controlled water kettle

### A project about modifying a water kettle to be temperature controlled.
The kettle is a wilfa rapid with 1.7L capacity.

### Components
| Part                 | Type                       |
|----------------------|----------------------------|
| Microcontroller      | RPi Pico W, ESP32          |
| Temperature sensor   | TSIC306 / DS18B20+         |
| 230V to 5V step down | Phone charger 5W (IKEA)    |
| Actuator             | Solid state relay 230V 45A |
| Display              | SSD1306                    |
| Interfaces           | Buttons / Potentiometer?   |

### Layout
The microcontroller, transformer and SSR will be put in the base of the kettle. Buttons and display will be put in the base. The main problem is that the kettle can rotate on its base, can be difficult to send signal. The best would be to put everything in the handle, but space makes this impossible. Will use two separate microcontrollers, one ESP32 in the handle and one RPi Pico W in the base. The ESP will drive the thermometer and maybe host the webserver. The RPi Pico will drive the SSR, handle user input and might drive display when this is implemented.  

### PID
Uses PID-control to have precise temperature control.
Because of big termal mass, a PWM signal will have the same effect as a voltage regulator. 

