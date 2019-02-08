# 2nd Runner up Microsoft Code.fun.do++ National Challenge 2019 (Microsoft AXLE 2019) 
# Winners Microsoft Code.fun.do++ @IITJ 2018

## IIT Jodhpur
Project developed for Microsoft code.fun.do hackathon 2018
Project Video submission: https://www.youtube.com/watch?v=_PcUHHltb04
Link: http://disaster-chain-1.eastus.cloudapp.azure.com

#### Team Name: The DarkSide

#### College: Indian Institute of Technology, Jodhpur 
![iitj team second runner up](https://user-images.githubusercontent.com/36476228/52478943-ff6a7380-2bcc-11e9-8383-dfee1695df4f.JPG)

![img_1164](https://user-images.githubusercontent.com/36476228/49571558-a9c0e300-f95f-11e8-962c-947171c0bd65.JPG)

![artboard 1 1](https://user-images.githubusercontent.com/36476228/52478726-4b68e880-2bcc-11e9-9afd-4755ed13804a.jpg)
![vlcsnap-2019-02-08-18h07m54s583](https://user-images.githubusercontent.com/36476228/52478796-7d7a4a80-2bcc-11e9-8c40-e8bbb10e3e17.png)
![vlcsnap-2019-02-08-18h08m46s905](https://user-images.githubusercontent.com/36476228/52478841-9be04600-2bcc-11e9-9547-c6681f9afe92.png)

![image](https://user-images.githubusercontent.com/36476228/49571626-d674fa80-f95f-11e8-806a-f53a5767edc1.png)
![image](https://user-images.githubusercontent.com/36476228/49571648-e68cda00-f95f-11e8-92f2-bb9260bc7d33.png)

#### Team Members: 
    - Anshul Ahuja
    - Aksh Chordia
    - Ayush Saxena

After going through the issue in particular, a need was observed that targetting a specific Calamity will not impact a large  population, hence we propose: Our project split in parts targeting different calamities, with a plan to integrate them all together under one common Disaster Management Solution.

## Part 1: Earthquake management system

- A **distributed IOT** based solution for earthquake detection and early warning system.
- Using **Raspberry Pi** as a central Hub for multiple IOT solutions and Node MCU units acting as slave boards deployed in different rooms of a given building providing real time data to the central hub through API calls and also capable of handling both security and automation in those rooms
- The **central hub is connected to Azure through REST API** calls to provide a dashboard monitoring system and as an early warning system.
- Using **Azure IOT Hub** for above implementation.
- The central hub is responsible for following safety protocols such as
    - Kill the power, water and gas supply to prevent further hazard to people.  
    - Sound based warning system.
    - Keep track of number of people inside to ensure everyone left the building.
   
## Part 2: Skin disease prediction after Floods

- Using **Custom Vision** service of Azure cognitive services to predict different type of skin diseases which may arise during a flood scenario.
- The accompanying Web App/Android App communicates with **Custom Vision** service through REST API calls.
    - Eliminates the need Medical Test when there is lack of infrastructure during a calamity.
    - Provide **faster medical diagnosis**.
