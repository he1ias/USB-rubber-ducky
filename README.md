# USB-rubber-ducky
A USB rubber ducky made for Hack Club's HalfLife event.

![The finalised PCB](https://raw.githubusercontent.com/he1ias/USB-rubber-ducky/refs/heads/main/PCB.jpeg)

### What is a Rubber Ducky?

A Rubber Ducky is a toy hacking tool that can emulate USB keyboards, helping show the limits of what physical access to a device can achieve. 

### What can it do?

It can play Snake, run commands on your computer at superhuman speeds, or just make you look like a hacker; among other things.

### How do I use it?

You'll first need to print the PCB and order all the parts (located in `bom.csv`, and shown below). Then, simply assemble, plug in the ESP32 and run the code located in `/Firmware`. The microcontroller will spin up its own web interface which can be accessed from your local network.

### What parts do I need?

| Item | Description | Qty | Unit Price (AUD) | Line Total (AUD) | Link |
|------|-------------|-----|------------------|------------------|------|
| 1 | ESP32-S3-Zero Mini Development Board (4MB Flash, pre-soldered headers) | 1 | $10.60 | $10.60 | [Link](https://littlebirdelectronics.com.au/products/esp32-s3-mini-development-board-based-on-esp32-s3fh4r2-dual-core-processor-240mhz-running-frequency-2-4ghz-wi-fi-bluetooth-5?collection=esp32-development-boards&variant=WS-25517) |
| 2 | Female 10-pin header (PTH, 0.1") | 2 | $1.60 | $3.20 | [Link](https://littlebirdelectronics.com.au/products/header-10-pin-female-pth-0-1) |
| 3 | Little Bird Lorikeet WS2812B rainbow board (right angle header) | 1 | $3.50 | $3.50 | [Link](https://littlebirdelectronics.com.au/products/little-bird-lorikeet-ws2812b-rainbow-board-with-right-angle-header) |
| 4 | Tactile button (SMD, 12mm) | 2 | $1.65 | $3.30 | [Link](https://littlebirdelectronics.com.au/products/tactile-button-smd-12mm) |
| 5 | 470 ohm 0.5W metal film resistors (pack of 8) | 1 | $0.70 | $0.70 | [Link](https://littlebirdelectronics.com.au/products/470-ohm-0-5-watt-metal-film-resistors-pack-of-8) |
| 6 | OTG converter USB 3.0 to USB-C adapter | 1 | $2.40 | $2.40 | [Link](https://littlebirdelectronics.com.au/products/otg-converter-usb-3-0-convert-to-usb-c) |
| | **Total** | | | **$23.70** | |

### How was it made?

Using KiCad!

I first drew the schematic:

![The finalised schematic](https://raw.githubusercontent.com/he1ias/USB-rubber-ducky/refs/heads/main/schematic.jpg)

...and then routed my PCB!

![The finalised routing](https://raw.githubusercontent.com/he1ias/USB-rubber-ducky/refs/heads/main/circuit.jpeg)