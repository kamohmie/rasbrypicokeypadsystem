from machine import Pin
import time

KEY_UP   = const(0)
KEY_DOWN = const(1)

keys = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]

rows = [9,8,7,6]
cols = [5,4,3,2]

gled = Pin(0, Pin.OUT)
rled = Pin(1, Pin.OUT)
row_pins = [Pin(pin_name, mode=Pin.OUT) for pin_name in rows]
col_pins = [Pin(pin_name, mode=Pin.IN, pull=Pin.PULL_DOWN) for pin_name in cols]

def init():
    for row in range(0,4):
        for col in range(0,4):
            row_pins[row].low()

def scan(row, col):
    row_pins[row].high()
    key = None

    if col_pins[col].value() == KEY_DOWN:
        key = KEY_DOWN
    if col_pins[col].value() == KEY_UP:
        key = KEY_UP
    row_pins[row].low()

    return key

init()

code = ""

while True:
    for row in range(4):
        for col in range(4):
            key = scan(row, col)
            if key == KEY_DOWN:
              last_key_press = keys[row][col]
              if last_key_press == "*":
                code = ""
              elif last_key_press == "#":
                if code == "9B4C2D9A":
                  print("Le code est valide.")
                  code = ""
                  gled.toggle()
                  time.sleep(1)
                  gled.toggle()
                else:
                  print("Le code est invalide.")
                  code = ""
                  rled.toggle()
                  time.sleep(1)
                  rled.toggle()
              else:
                code = code + last_key_press
                print("Key Pressed", keys[row][col])
                print(code)
                time.sleep(1)
