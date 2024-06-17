<h1 align="center">Graduated Project</h1>

## Our Idea

The goal of this project is to construct a physical FANET, outside the simulator, this can be done by constructing a number of drones built on the ESP-Drone repository, along with our own PCB and a 3D printed drone body. The FANET nodes will communicate with each other using LoRaWAN through our own modified AODV routing protocol. The FANET is planned to operate over the area of Birzeit University.

Since we will be using light-weight drones for nodes, the weight of anything carried by drones is critical, for this reason we decided on using the LoRa32 microcontroller, that integrates the ESP32 chip along with the LoRa module in a compact package, which weighs about 18grams, our testing shows a current draw of 45-50 mA during normal operations, goes up by 10 mA during transmission/reception.
- We currently have 2 LoRa32 microcontrollers in our possession
<div align="center">
  <img src="https://github.com/mahmoud024/ESP-Drone-Graduated-Project-/assets/83675107/bb4fb2ca-eb1c-45c1-800c-01652d9669d8" alt="Image 3" heigh="100" width="500">
</div>


## Step 1: Build ESP23 Drone

Since the scope of the project is rapidly expanding, we don’t have enough time
to design and build a drone from scratch, instead we will be using Espressif
Systems’ drone design.

For more information on getting started with ESP-IDF, visit the [Espressif ESP-Drone Documentation](https://docs.espressif.com/projects/espressif-esp-drone/en/latest/getespidf.html).


<h3 align="center">Hardware Part</h3>

1. **PCB**

    As is previously, our drone design is light-weight, so we will need to conserve as much as possible on the drone weight, and therefore we found it best to construct our own PCB.
   
3. **Parts**

   We faced some difficulties in providing the parts because we are restricted by the Israeli occupation and the high cost of the parts, but the parts were eventually provided with great difficulty.

<h3 align="center">Software Part</h3>

## Step 2: Routing Protocol

we will be using a LoRa module for transmission/Re- ception between nodes in our physical test bench, the LoRa module is chosen for its extended range, up to 14Km at SF12, and extremely low current draw, our own testing showed an 10 mA increase in current draw at transmission/re- ception at SF7, matching the datasheet specification.

The drawback to all this, is the low bandwidth, 290 bps at SF12, choosing a lower spread factor, will provide a higher bandwidth at a lower range, SF7 is rated to give 5470 bps for 2km, a range of 2km is well above our needs for this project, the bit rate is also sufficient for the communication protocol used, table 2 shows LoRa transmission ranges and bandwidth at different Spread Factors.

<div align="center">
  
| **Spreading Factor** | **Bitrate** | **Range** |
|----------------------|-------------|-----------|
| SF7                  | 5470 bps    | 2 Km      |
| SF8                  | 3125 bps    | 4 Km      |
| SF9                  | 1760 bps    | 6 Km      |
| SF10                 | 980 bps     | 8 Km      |
| SF11                 | 440 bps     | 11 Km     |
| SF12                 | 290 bps     | 14 Km     |
--------------------------------------------------
</div>


Our routing protocol builds upon the AODV protocol, and improves on it in two substantial ways, multiple paths and speed dependent route lifetime. The AODV routing protocol establishes a singular path for packets to travel from the source node to the destination node, however this can be unreliable in unstable networks, therefore establishing multiple paths will incur small overhead for the reward of a more reliable communication link, this is proposed in the AOMDV
routing protocol.

<div align="center">

| **Parameter**                    | **AODV**                    | **AOMDV**                    |
|----------------------------------|-----------------------------|------------------------------|
| Routing Protocol                 | Single path routing protocol | Multipath routing protocol   |
| Average End-to-End Delay         | 175 ms                      | 194 ms                       |
| Routing Overhead                 | Low                         | High                         |
| Number of Packets Dropped        | High                        | Low                          |
| Performance Metrics              | Low                         | High                         |
-------------------------------------------------------------------------------------------------

</div>

The AODV routing protocol doesn’t provide a method to calculate the lifetime of established routes between nodes, ns3 simulator keeps an arbitrary period of time of 10 seconds, we suggest making use of the instantaneous speed
of each node in the calculation of the lifetime, where the lifetime of any path is decided by the speed of the nodes in the path at route instantiation, equation below is followed when calculating the lifetime of any route established between any two nodes, where Sx is the speed of node x at the time of RREP packet transmission/forwarding, and  is scalar hyperparameter used for scaling the lifetime
of all routes.

<div align="center">

Life time Route = min(S<sub>0</sub>, S<sub>1</sub>, S<sub>2</sub>, &hellip;, S<sub>n</sub>) / &alpha;

</div>

Currently, we were able to construct the lifetime calculations on the ns3 simulator and it has yield promising results, as it outperformed the AODV protocol in terms on Packet Receive Rate, this is probably at the cost of increased routing calculations.


#### Multi-path implementation is currently stagnate as some unexpected difficulties were faced.




