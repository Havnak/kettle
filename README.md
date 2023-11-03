# Temperature controlled water kettle

### A project about modifying an existing water kettle to be temperature controlled.
The kettle is a wilfa rapid with 1.7L capacity.

### Components
| Part                 | Type                       |
|----------------------|----------------------------|
| Microcontroller      | RP2040 (RPi Pico W)        |
| Temperature sensor   | TSIC306 / DS18B20+         |
| 230V to 5V step down | Phone charger 5W (IKEA)    |
| Actuator             | Solid state relay 230V 16A |
| Display              | SSD1306                    |
| Interfaces           | Buttons / Potentiometer?   |

### Layout
The microcontroller, transformer and SSR will be put in the base of the kettle. Buttons, display and thermometer will be put in the handle of the kettle if possible. The main problem is that the kettle can rotate on its base, can be difficult to send signal. The best would be to put everything in the handle, but space might be a problem. 

### PID
Uses PID-control to have precise temperature control.
Because of big termal mass, a PWM signal will have the same effect as a voltage regulator. 

