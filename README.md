<h1 align="center">Graduation Project</h1>

## Our Idea

The goal of this project is to construct a physical FANET, outside the simulator, this can be done by constructing a number of drones built on the ESP-Drone repository, along with our own PCB and a 3D printed drone body. The FANET nodes will communicate with each other using LoRaWAN through our own modified AODV routing protocol. The FANET is planned to operate over the area of Birzeit University.

Since we will be using light-weight drones for nodes, the weight of anything carried by drones is critical, for this reason we decided on using the LoRa32 microcontroller, that integrates the ESP32 chip along with the LoRa module in a compact package, which weighs about 18grams, our testing shows a current draw of 45-50 mA during normal operations, goes up by 10 mA during transmission/reception

<div align="center">
  <img src="https://github.com/mahmoud024/Graduation-Project/assets/83675107/38d05341-0041-4593-b1ab-114193afe815" alt="Image 3" heigh="100" width="500">
</div>


## Step 1: Build ESP23 Drone

Since the scope of the project is rapidly expanding, we don’t have enough time
to design and build a drone from scratch, instead we will be using Espressif
Systems’ drone design.

For more information on getting started, visit the [Espressif ESP-Drone Documentation](https://docs.espressif.com/projects/espressif-esp-drone/en/latest/getespidf.html).


<h3 align="center">Hardware Part</h3>
   
1. **Components**

    We faced some difficulties in providing the parts because we are restricted by the Israeli occupation and the high cost of the parts, but the parts were eventually provided with great difficulty.

    - ##### Basic Component List
    <div align="center">
      
      | **Component**                         | **Number** | **Notes**                         |
      |---------------------------------------|------------|-----------------------------------|
      | Main board                            | 1          | ESP32 LORA V3 + MPU6050           |
      | Frame                                 | 1          | We Build it using 3D printer      |
      | 716 motor                             | 4          | Optional: 720 motor               |
      | 46mm propeller A                      | 2          |                                   |
      | 46mm propeller B                      | 2          |                                   |
      | 1000mAh 1s LiPo battery               | 1          |                                   |
      
    </div>

     1. **Frame**

      Steps to make the Frame:

      <div align="center">
          <img src="https://github.com/mahmoud024/Graduation-Project/assets/83675107/9fdd4a80-abf6-4a71-997c-49bf59f386d8" alt="Description of your image">
      </div>

   Final Output:
   
    <div align="center">
        <img src="https://github.com/mahmoud024/Graduation-Project/assets/83675107/1863fa9f-0a03-4924-9f0e-cd6063b6a2df" alt="Image 3" heigh="100" width="370">
        <img src="https://github.com/mahmoud024/Graduation-Project/assets/83675107/5008ded2-6388-4104-a6dc-7f4ec9774773" alt="Image 3" heigh="100" width="300">
    </div>

  

     2. **Main Controller**

      <div align="center">
          <img src="https://github.com/mahmoud024/Graduation-Project/assets/83675107/ddcf0431-47ec-44ce-981e-860ed99c0848" alt="Image 3" heigh="100" width="200">
      </div>

    <div align="center">

      | **Chip**       | **Module**           |     **Battery**       |    **Dimensions**     |
      |----------------|----------------------|-----------------------|-----------------------|
      | ESP32-S3FN8    | ESP32 LORA V3        | 3.7V lithium battery  |  50.2 * 25.5* 10.2 mm |


    </div>

     3. **Sensor**
        
      <div align="center">
          <img src="https://github.com/mahmoud024/Graduation-Project/assets/83675107/ce09b5fe-a602-4896-9a0d-7666c90b56e7" alt="Image 3" heigh="100" width="200">
      </div>
   
    <div align="center">
  
      | **Sensor**     | **Interface**        | **Notes**                             |
      |----------------|----------------------|---------------------------------------|
      | MPU6050        | I2C0                 | Main board sensor                     |
   
    </div>

    3. **Motor**
        
      <div align="center">
          <img src="https://github.com/mahmoud024/Graduation-Project/assets/83675107/e7b8a98f-8b70-4aaa-8dc8-cffc97882f01" alt="Image 3" heigh="100" width="200">
      </div>
   
    <div align="center">
  
      | **Motor**      | **Type**             | **Notes**                              |
      |----------------|----------------------|----------------------------------------|
      | 716 motor      | Coreless motor       | Use 720 if you have issue in altitude  |
   
    </div>

    3. **Battery**
        
      <div align="center">
          <img src="https://github.com/mahmoud024/Graduation-Project/assets/83675107/c964d249-2c8f-4658-ae71-17c734f56bef" alt="Image 3" heigh="100" width="200">
      </div>
   
    <div align="center">
  
      | **Battery**             | **Voltage**     | **Dimensions**      | **Dimensions**    |
      |-------------------------|-----------------|---------------------|-------------------|
      | 1000mAh 1s LiPo battery | 3.7V (1S)       | 48 x 30 x 9         | 28.5              |
   
    </div>


    - ##### Definition of Main Board IO

    <div align="center">

      | **Pins**       | **Function**         | **Notes**                             |
      |----------------|----------------------|---------------------------------------|
      | GPIO23         | I2C0_SDA             | Only for MPU6050                      |
      | GPIO22         | I2C0_SCL             | Only for MPU6050                      |
      | GPIO2          | interrupt            | MPU6050 interrupt                     |
      | GPIO12         | MOT_1                |                                       |
      | GPIO35         | MOT_2                |                                       |
      | GPIO32         | MOT_3                |                                       |
      | GPIO33         | MOT_4                |                                       |
      | GND            |                      | With Ground                           |
      | 3V3            |                      | With VCC of MPU6050                   |

    </div>

2. **PCB**

    As is previously, our drone design is light-weight, so we will need to conserve as much as possible on the drone weight, and therefore we found it best to construct our own PCB.

    Scheme Below show our PCB design:

    <div align="center">
      <img src="https://github.com/mahmoud024/Graduated-Project/assets/83675107/fc382b12-97db-479c-a8b3-8afc9f63bedc" alt="Image 3" heigh="100" width="500">
    </div>

    Steps to make our PCB:

    <div align="center">
      <img src="https://github.com/mahmoud024/Graduated-Project/assets/83675107/4eb8d103-1a8b-4c8b-9119-ecc378a2f171" alt="Image 3" heigh="80" width="233">
      <img src="https://github.com/mahmoud024/Graduated-Project/assets/83675107/c6a7d125-b92d-4774-b11b-b85f9ecfd1b1" alt="Image 3" heigh="80" width="233">
      <img src="https://github.com/mahmoud024/Graduated-Project/assets/83675107/5a0af580-b99b-4a47-a10b-99e02f950d08" alt="Image 3" heigh="80" width="200">
      <img src="https://github.com/mahmoud024/Graduated-Project/assets/83675107/9630c564-b713-4e2b-a183-aba882432c51" alt="Image 3" heigh="80" width="200">
    </div>

    The Link below show some videos While working on the production of the PCB (https://google.com)

    You Can Find All File You Needed in (PCB) Folder
---

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

</div>

The AODV routing protocol doesn’t provide a method to calculate the lifetime of established routes between nodes, ns3 simulator keeps an arbitrary period of time of 10 seconds, we suggest making use of the instantaneous speed
of each node in the calculation of the lifetime, where the lifetime of any path is decided by the speed of the nodes in the path at route instantiation, equation below is followed when calculating the lifetime of any route established between any two nodes, where Sx is the speed of node x at the time of RREP packet transmission/forwarding, and  is scalar hyperparameter used for scaling the lifetime
of all routes.

<div align="center">

Life time Route = min(S<sub>0</sub>, S<sub>1</sub>, S<sub>2</sub>, &hellip;, S<sub>n</sub>) / &alpha;

</div>

Currently, we were able to construct the lifetime calculations on the ns3 simulator and it has yield promising results, as it outperformed the AODV protocol in terms on Packet Receive Rate, this is probably at the cost of increased routing calculations.


#### Multi-path implementation is currently stagnate as some unexpected difficulties were faced.
#

- <h4>Part 1: code inspection and review of ns3 aodv implementtion</h4>
- <h4>Part 2: code inspection of ns3 mobility models to obtain speed</h4>
- <h4>Part 3: implantation of speed reliant timeout</h4>
- <h4>Part 4: attempt at implementing multi-path protocol(fail)</h4>
- <h4>Part 5: implement RREQ and RERR counter</h4>
- <h4>Part 6: Simulation results at different max_distance parameter values</h4>








