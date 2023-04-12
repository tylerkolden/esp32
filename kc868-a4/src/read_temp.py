import machine, onewire, ds18x20, time

# Set up the GPIO pin to read data from the DS18B20 temperature sensor
ds_pin = machine.Pin(13)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Scan for DS18B20 temperature sensors on the one-wire bus
roms = ds_sensor.scan()

# If no temperature sensors are found, print an error message and exit
if not roms:
    print("No DS18B20 temperature sensors found")
    sys.exit()

while True:
    # Read the temperature from the first temperature sensor found
    ds_sensor.convert_temp()
    time.sleep(1)
    temp_c = ds_sensor.read_temp(roms[0])

    # Convert the temperature from Celsius to Fahrenheit
    temp_f = temp_c * 1.8 + 32

    # Print the temperature in Fahrenheit
    print("Temperature: %.2f F" % temp_f)
