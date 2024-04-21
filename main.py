import machine
import utime

Q1 = 1
Q2 = 2
Q3 = 3
Q4 = 4
Q5 = 5
Q6 = 6
Q7 = 7
Q8 = 8

# Define GPIO pins
gpio_pins = [machine.Pin(i, machine.Pin.OUT) for i in [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8]]

def set_pins(state):
    for pin, value in zip(gpio_pins, state):
        pin.value(value)

def sequence_on_off(sequence, delays):
    for state, delay in zip(sequence, delays):
        set_pins(state)
        utime.sleep_us(delay)

# Define sequence and delays
sequence = [
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 1]
]

delays = [1608, 1895, 4602, 1895, 1608, 1895, 4602, 1895]

# Run the sequence
while True:
    sequence_on_off(sequence, delays)