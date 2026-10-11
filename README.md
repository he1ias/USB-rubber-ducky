# USB-rubber-ducky
A USB rubber ducky made for Hack Club's HalfLife event.

!(The finalised PCB)['./PCB.jpeg']

### What is a Rubber Ducky?

A Rubber Ducky is a toy hacking tool that can emulate USB keyboards, helping show the limits of what physical access to a device can achieve.

### What can it do?

It can play Snake, run commands on your computer at superhuman speeds, or just make you look like a hacker; among other things.

### How do I use it?

You'll first need to print the PCB and order all the parts (located in `bom.txt`). Then, simply assemble, plug in the ESP32 and run the code located in `/Firmware`. The microcontroller will spin up its own web interface which can be accessed from your local network.