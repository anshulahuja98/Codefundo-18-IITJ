# CFD-18
Project developed for Microsoft code.fun.do hackathon 2018

## Part 1: Earthquake management system
* A distributed IOT based solution for earthquake detection and early warning system.
* Using Raspberry Pi as a central Hub for multiple IOT solutions and Node MCU units deployed in different rooms of a given building providing real time data to the central hub through API calls.
* Using battery powered Node-mcu as slave boards, capable of handling both security and automation in particular rooms, connected over wireless channels to the central hub.
* The central hub is connected to Azure through REST API calls to provide a dashboard monitoring system and as an early warning system. 
* The central hub is responsible for following safety protocols such as:
    * Kill the Power.
    * Kill the gas supply to prevent further hazard to people.
    * Kill the water supply to prevent any chances of short circuit.
    * Sound based warning system.
    * Keep track of number of people inside, inorder to ensure everyone left the building.
   
## Part 2: Skin disease prediction after Floods
* Using Custom Vision service of Azure cognitive services to predict different type of skin disesase which may arise during a flood scenario.
* The accompanying Android App communicates with Custom Vision service through REST API calls.
    * Eliminates the need Medical Test when there is lack of infrastructure during a calamity.

## Part 3: Hurricane & Tornado.
The central hub is used to check with the local news servers, for any early warning signs.


## Part 4: Plot available Earthquake Data and provide statistical analysis
``Under planning``

## Part 5:
 `Pending`
        