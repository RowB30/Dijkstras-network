# Dijkstras-network

This program was a homework assignment given 2 weeks to finish. The purpose of this script is to implement Dijkstra's algorithm in an imaginary network where messages are being sent between the nodes. This program reqires the main.py file and inputs from 4 seprate files to work.

<h2>main.py</h2>
This python file houses all of the functionality of the actual script.

<h2>topology.txt</h2>
This file creates the edges and weights between the nodes. How it works is that you enter a number in each coloumn(can be double digent) that represents the <i>first node, second node</i> and then the <i>weight</i> between nodes. The current version of this program creates a bidirectional graph so it will create paths between both nodes with the same weight.

<h2>message.txt</h2>
Simmalrly to topology.txt, you are ment to enter inputs into 3 coloums. The start node, the destination node, and the message you wish to send to the destination node. Since there is no actual network it just prints a message confirming that the message was sent.

<h2>changes.txt</h2>
This text file is used to add and remove edges between nodes. To accomplish this, the same 3 coloumn format as the last two files is used. <i>first node, second node</i> and the <i>weight</i>. To remove an edge between nodes enter -999 exactly in the 3rd coloumn.

<h2>output.txt</h2>
This file is how you will see the forwading table of each node and the messages sent between nodes. If there is no information in message.txt or changes.txt, the inital forwarding tables will be displayed. When reading the table the same 3 coloum format is used. Destination node, the very next most efficent hop, and the cost to get to the destination node. Each table is displayed in order of node ID.
