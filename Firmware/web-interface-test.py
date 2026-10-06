# some code from https://RandomNerdTutorials.com/raspberry-pi-pico-web-server-micropython/

import network
import socket
import time
import random
from machine import Pin

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

local_ip = wlan.ifconfig()[0]
print(local_ip)

# Create an LED object on pin 'LED'
led = Pin('LED', Pin.OUT)

# Wi-Fi credentials
ssid = '****'
password = '********'

template_file = "template.html"

template = ""
with open(template_file) as file:
    template = file.read()
    
if not template:
    print("Failed to load HTML template.")
    exit(1)
    
style_file = "style.css"

style = ""
with open(style_file) as file:
    style = file.read()

def webpage():
    return template

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

connection_timeout = 10
while connection_timeout > 0:
    if wlan.status() >= 3:
        break
    connection_timeout -= 1
    print('Waiting for Wi-Fi connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('Failed to establish a network connection')
else:
    print('Connection successful!')
    network_info = wlan.ifconfig()
    print('IP address:', network_info[0])

# Set up socket and start listening
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen()

print('Listening on', addr)

state = "OFF"

while True:
    try:
        conn, addr = s.accept()
        print('Got a connection from', addr)
        
        request = conn.recv(1024)
        request = str(request)

        try:
            request = request.split()[1]
            print('Request:', request)
        except IndexError:
            pass
        
        if request == '/lighton?':
            print("LED on")
            led.value(1)
            state = "ON"
        elif request == '/lightoff?':
            led.value(0)
            state = 'OFF'
        elif request == "/style":
            response = style
            
            conn.send('HTTP/1.0 200 OK\r\nContent-Type: text/css\r\n\r\n')
            conn.send(response)
            conn.close()
            
            continue
        response = webpage()

        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()

    except OSError as e:
        conn.close()
        print('Connection closed')

