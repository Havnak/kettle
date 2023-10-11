# Temperature controlled water kettle

### A project about modifying an existing water kettle to be temperature controlled.
The kettle is a wilfa rapid with 1.7L capacity.

### Components
| Part                 | Type                       |
|----------------------|----------------------------|
| Microcontroller      | RPi Pico                   |
| Temperature sensor   | Thermistor                 |
| 230V to 5V step down | Phone charger 5W           |
| Actuator             | Solid state relay 230V 10A |
| Display              | 7 segment or LCD           |
| Switches             | Buttons                    |

### Layout
The microcontroller, transformer and SSR will be put in the base of the kettle. Buttons, display and thermometer will be put in the handle of the kettle if possible. The main problem is that the kettle can rotate on its base, can be difficult to send signal. The best would be to put everything in the handle, but space might be a problem. 

### PID
Uses PID-control to have precise temperature control.
Because of big termal mass, a PWM signal will have the same effect as a voltage regulator. 


