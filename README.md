# DIS-Rutgers-PerformanceAnalysisOfOpenflowControllers

To run the ryu controller
sudo docker run --network=host -it --rm osrg/ryu /bin/bash

Note: Will only work after executing ryu_setup.sh


Evaluation using Wireshark

Once connection is established between the controller and the network topology, and mininet is running
use the following commands for evaluation
On the mininet terminal, type xterm <host1> <host2>

The xterm window will pop up for both the hosts between which you want to test the network
then ping host2 from host1 using the IP address of host 2. To find out the IP addresses run "dump" on mininet terminal
then run sudo wireshark on the xterm h2, wireshark window will pop up, where further evaluation can be done.