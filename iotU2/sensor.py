import name
import ldr
sensor_pin=name.sensor_pin
def read():
	return(ldr.sensorRead(sensor_pin))
