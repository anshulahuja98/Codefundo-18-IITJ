# Code.fun.do++ 2018
Project developed for Microsoft code.fun.do hackathon 2018

#### Team Name: The DarkSide

#### College: Indian Institute of Technology, Jodhpur 

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

## Part 3: Blockchain based Disaster Management Tracking 

- Using **Ethereum Blockchain** and **smart contracts** built using **Azure Blockchain Workbench** to smartly track Disaster Relief Management. 
    - Keep accurate statistics about disasters, publicly available and untamperable by the government.
    - Maintain a publically auditable ledger to keep track of govt and donation expenditure for relief management.
    - Track resources sent to impacted areas using **Blockchain and IOT based devices**, to ensure that help reaches where it needs to.
    - Using **Smart Contracts** to execute important tasks automatically without dependence on government action and decision.       
        - Automated Warning systems.
        - Managing the Transportation Chain for relief resources.
        - Automatic fund release for affected places.      
        - Unbiased execution in tracking unregulated usage of funds.
    #### The eventual plan is to integrate part 1 and part 2 into this blockchain to keep track of data
                
