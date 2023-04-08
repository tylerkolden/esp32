# import required modules
from machine import SoftI2C, Pin
import time

# configure the I2C pins (SDA and SCL)
sda_pin = 4
scl_pin = 15

# initialize SoftI2C with the specified SDA and SCL pins
i2c = SoftI2C(sda=Pin(sda_pin), scl=Pin(scl_pin))

# define the I2C address for the PCF8574
pcf8574_address = 0x24

# define a function to read the current state of the PCF8574
def read_pcf8574_state(i2c, address):
    state = bytearray(1)
    i2c.readfrom_into(address, state)
    return state[0]

# define a function to write a new state to the PCF8574
def write_pcf8574_state(i2c, address, state):
    i2c.writeto(address, bytes([state]))

# toggle all relays on the PCF8574
def toggle_all_relays(i2c, address):
    # read current state
    state = read_pcf8574_state(i2c, address)
    # toggle all bits (all relays)
    state ^= 0xFF
    # write updated state
    write_pcf8574_state(i2c, address, state)

# Define a function to toggle a specific relay on the PCF8574
def toggle_relay(i2c, address, relay_number):
    if 1 <= relay_number <= 6:
        # read current state
        state = read_pcf8574_state(i2c, address)
        # toggle the specified relay
        state ^= 1 << (relay_number - 1)
        # write updated state
        write_pcf8574_state(i2c, address, state)
    else:
        print("Invalid relay number. Please choose a number between 1 and 6.")

# demo relay toggling
while True:
    # turn on all relays
    toggle_all_relays(i2c, pcf8574_address)
    # print
    print("All relays toggled")
    # wait for 2 seconds before toggling again
    time.sleep(2)
    # turn off all relays
    toggle_all_relays(i2c, pcf8574_address)
    # print
    print("All relays toggled")
    # toggle relays 1 to 6 sequentially
    for relay in range(1, 7):
        # toggle specific relay
        toggle_relay(i2c, pcf8574_address, relay)
        # print which relay was toggled
        print(f"Relay {relay} toggled")
        # wait for 1 second before toggling the next relay
        time.sleep(1)