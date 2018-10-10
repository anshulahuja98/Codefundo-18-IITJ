# CFD-18
Project developed for Microsoft code.fun.do hackathon 2018



Team Name: The DarkSide
College: Indian Institute of Technology, Jodhpur 
Team Members: 
    - Anshul Ahuja
    - Aksh Chordia
    - Ayush Saxena

We felt that targeting a specific Calamity cannot have a good enough impact for a larger population, hence we propose our project split in parts targeting different calamities, with a plan to integrate them all together under one common disaster service.

## Project Disaster Chain
### Blockchain based Disaster Management and Tracking 
**Under Planning**
- Using **Ethereum Blockchain** and **smart contracts** built using **Azure Blockchain Workbench** to smartly track Disaster Relief Management. 
    - Keep accurate statistics about disasters, publicly available and untamperable by the government.
    - Make publicly available the government and donation expenditure for relief management.
    - Track resources sent to impacted areas using **Blockchain and IOT based devices**, to ensure that help reaches where it needs to.
    - Using **Smart Contracts** to execute important tasks automatically without dependence on government action and decision.        
        - Automated Warning systems.
        - Managing the Transportation Chain for relief resources.
        - Automatic fund release for affected places.      
        - Unbiased execution in tracking unregulated usage of funds.       
     - ##Sub Parts
        > The sub parts are all based on the blockchain to ensure the safety of data and to execute appropriate measures for relief.
        ### Part 1: Earthquake management system
        **Under Development**
        - A **distributed IOT** based solution for earthquake detection and early warning system.
        - Using **Raspberry Pi** as a central Hub for multiple IOT solutions and Node MCU units deployed in different rooms of a given building providing real time data to the central hub through API calls.
        - Using battery powered **Node MCU as slave boards**, capable of handling both security and automation in particular rooms, connected over wireless channels to the central hub.
        - The **central hub is connected to Azure through REST API** calls to provide a dashboard monitoring system and as an early warning system.
        - Using **Azure IOT Hub** for above implementation.
        - The central hub is responsible for following safety protocols such as
            - Kill the power, water and gas supply to prevent further hazard to people.  
            - Sound based warning system.
            - Keep track of number of people inside to ensure everyone left the building.
        - This sends the results to be saved directly to the blockchain.           
        ### Part 2: Skin disease prediction after Floods
        **Under Development**
        - Using **Custom Vision** service of Azure cognitive services to predict different type of skin diseases which may arise during a flood scenario.
        - The accompanying Web App/Android App communicates with **Custom Vision** service through REST API calls.
            - Eliminates the need Medical Test when there is lack of infrastructure during a calamity.
            - Provide **faster medical diagnosis**.
        - The results are directly saved in the blockchain to keep accurate track of diseases/epidemics that might arise and to ensure appropriate help is provided for the same.
                