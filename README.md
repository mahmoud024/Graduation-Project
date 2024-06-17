<h1 align="center">Graduated Project</h1>

## Our Idea

The goal of this project is to construct a physical FANET, outside the simulator, this can be done by constructing a number of drones built on the ESP-Drone repository, along with our own PCB and a 3D printed drone body. The FANET nodes will communicate with each other using LoRaWAN through our own modified AODV routing protocol. The FANET is planned to operate over the area of Birzeit University.

## Step 1: Build ESP23 Drone

<h3 align="center">Hardware Part</h3>

1. **PCB**
2. **Parts**

<h3 align="center">Software Part</h3>

## Step 2: Routing Protocol

we will be using a LoRa module for transmission/Re- ception between nodes in our physical test bench, the LoRa module is chosen for its extended range, up to 14Km at SF12, and extremely low current draw, our own testing showed an 10 mA increase in current draw at transmission/re- ception at SF7, matching the datasheet specification.

The drawback to all this, is the low bandwidth, 290 bps at SF12, choosing a lower spread factor, will provide a higher bandwidth at a lower range, SF7 is rated to give 5470 bps for 2km, a range of 2km is well above our needs for this project, the bit rate is also sufficient for the communication protocol used, table 2 shows LoRa transmission ranges and bandwidth at different Spread Factors.


| **Spreading Factor** | **Bitrate** | **Range** |
|----------------------|-------------|-----------|
| SF7                  | 5470 bps    | 2 Km      |
| SF8                  | 3125 bps    | 4 Km      |
| SF9                  | 1760 bps    | 6 Km      |
| SF10                 | 980 bps     | 8 Km      |
| SF11                 | 440 bps     | 11 Km     |
| SF12                 | 290 bps     | 14 Km     |
--------------------------------------------------

