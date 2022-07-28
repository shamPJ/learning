# Chapter 3 Transport Layer

## :green_circle: 3.1 Introduction and Transport-Layer Services

A transport-layer protocol provides for logical communication between app processes running on different hosts. \
**Logical communication** - from an app’s perspective, it is as if the hosts running the processes were directly conn;\
in reality, the hosts may be on opposite sides of the planet, conn via numerous routers and a wide range of link types. App processes use the logical communication provided by the transport layer to send messages to each other, free from the worry of the details of the physical infrastructure used to carry these messages.

Transport-layer protocols are implemented in the end systems but not in network routers. Routers - do not examine the fields of the transport-layer segment encapsulated with the datagram. On the sending side, the transport layer converts the app-layer messages it receives from a sending app process into transport-layer packets, known as **transport-layer segments** in Internet terminology. 

- breaking the app messages into smaller chunks and adding a transport-layer header to each chunk to create the transport-layer segment. 
- transport layer then passes the segment to the network layer at the sending end sys, where the segment is encapsulated within a network-layer packet (a datagram) and sent to the destination. 
- the network layer extracts the transport-layer segment from the datagram and passes the segment up to the transport layer. 
- transport layer processes the received segment, making the data in the segment available to the receiving app.

### :small_blue_diamond: 3.1.1 Relationship Between Transport and Network Layers

Transport-layer protocol provides logical communication between processes running on different hosts  VS\
Network-layer protocol provides logical communication between hosts

**Transport-layer protocols live in the end systems**. Within an end system, a transport protocol moves messages from app processes to the network edge (that is, the network layer) and vice versa, but it doesn’t have any say about how the messages are moved within the network core. In fact intermediate routers neither act on, nor recognize, any info that the transport layer may have added to the appl messages.

The services that a transport protocol can provide are often constrained by the service model of the underlying network-layer protocol. If the network-layer protocol cannot provide delay or bandwidth guarantees for transport-layer segments sent between hosts, then the transport-layer protocol cannot provide delay or bandwidth guarantees for app messages sent between processes.

Nevertheless, certain services can be offered by a transport protocol even when the underlying network protocol doesn’t offer the corresponding service at the network layer. For example, a transport protocol can offer reliable data transfer service to an app even when the underlying network protocol is unreliable, that is, even when the network protocol loses, garbles, or duplicates packets. As another example, a transport protocol can use encryption to guarantee that app messages are not read by intruders, even when the network layer cannot guarantee the confidentiality of transport-layer segments.

### :small_blue_diamond: 3.1.2 Overview of the Transport Layer in the Internet

- **UDP (User Datagram Protocol)** provides an unreliable, connectionless service to the invoking app. 
- **TCP (Transmission Control Protocol)** provides a reliable, connection-oriented service to the invoking app. 

When designing a network app, the app developer must specify one of these two transport protocols; the app developer selects between UDP and TCP when creating sockets.

The Internet’s network-layer protocol **IP Internet Protocol**. IP provides logical communication between hosts. The IP service model is a **best-effort delivery service** - IP makes its “best effort” to deliver segments between communicating hosts, but it makes no guarantees. Does not guarantee:
- segment delivery, 
- orderly delivery of segments,  
- the integrity of the data in the segments. 

->IP is said to be an unreliable service. \
Every host has at least one network-layer address, a so-called **IP address**. 

The most fundamental responsibility of UDP and TCP is to extend IP’s delivery service between two end systems to a delivery service between two processes running on the end systems.
Extending host-to-host delivery to process-to-process delivery is called **transport-layer multiplexing and demultiplexing**. 

Two minimal transport-layer services:
- process-to-process data delivery 
- error checking—are 

e.g. UDP -> unreliable service — does not guarantee that data sent by one process will arrive intact (or at all!) to the destination process.


TCP in addition provides:
- reliable data transfer (flow control, sequence numbers, acknowledgments, and timers)
- congestion control. Prevents any one TCP conn from swamping the links and routers between communicating hosts with an excessive amount of traffic. 

-> TCP converts IP’s unreliable service between end sys into a reliable data transport service between processes. 

## :green_circle: 3.2 Multiplexing and Demultiplexing

The transport layer in the receiving host does not deliver data directly to a process, but instead to an intermediary socket. 

- **Demultiplexing** job of delivering the data in a transport-layer segment to the correct socket. 

- **Multiplexing** job of gathering data chunks at the source host from diff sockets, encapsulating each data chunk with header info (that will later be used in demultiplexing) to create segments, and passing the segments to the network layer. 

Transport-layer multiplexing requires (1) that sockets have unique identifiers, and (2) that each segment have special fields that indicate the socket to which the segment is to be delivered. These special fields, are the **source port number field** and the **destination port number field**.

Each port number is a 16-bit number, ranging from 0 to 65535. \
The port numbers ranging from 0 to 1023 are called well-known port numbers and are restricted, which means that they are reserved for use by well-known app protocols such as HTTP (which uses port number 80) and FTP (which uses port number 21). 

The transport layer automatically assigns a port number to the socket. The transport layer assigns a port number in the range 1024 to 65535 that is currently not being used by any other UDP port in the host. Alternatively, we can add a line into our Python program after we create the socket to associate a specific port number (say, 19157) to this UDP socket via the socket bind() method. \
Typically, the client side of the application lets the trans- port layer automatically (and transparently) assign the port number, whereas the server side of the application assigns a specific port number.

UDP socket is fully identified by a two-tuple consisting of a dest IP address and a dest port number. As a consequence, if two UDP segments have diff source IP addresses and/or source port numbers, but have the same dest IP address and dest port number, then the two segments will be directed to the same dest process via the same dest socket.

TCP socket is identified by a four-tuple: (source IP address, source port number, destination IP address, destination port number).\
In contrast with UDP, two arriving TCP segments with diff source IP addresses or source port numbers will (with the exception of a TCP segment carrying the original connection-establishment request) be directed to two diff sockets. 

- The TCP server application has a “welcoming socket,” that waits for connection-establishment requests from TCP clients e.g. on port number 12000.
- The TCP client creates a socket and sends a conn establishment request segment with the lines: 

`clientSocket = socket(AF_INET, SOCK_STREAM)`
`clientSocket.connect((serverName,12000))`

- A connection-establishment request is nothing more than a TCP segment with dest port number 12000 and a special connection-establishment bit set in the TCP header. The segment also includes a source port number that was chosen by the client.
- When the host OS of the computer running the server process receives the incoming conn-request segment with dest port 12000, it locates the server process that is waiting to accept a connection on port number 12000. The server process then creates a new socket:

`connectionSocket, addr = serverSocket.accept()`

- The transport layer at the server notes the following four values in the conn-request segment: (1) the source port number in the segment, (2) the IP address of the source host, (3) the dest port number in the segment, and (4) its own IP address. The newly created connection socket is identified by these four values; all subsequently arriving segments whose source port, source IP address, destination port, and destination IP address match these four values will be demultiplexed to this socket. 

**Web Servers and TCP**

There is not always a one-to-one correspondence between connection sockets and processes. Today’s high-performing Web servers often use only one process, and create a new **thread** with a new connection socket for each new client connection. (A thread can be viewed as a lightweight subprocess.) I

## :green_circle: 3.3 Connectionless Transport: UDP



### :small_blue_diamond: 3.3.1 UDP Segment Structure
### :small_blue_diamond: 3.3.2 UDP Checksum

## :green_circle: 3.4 Principles of Reliable Data Transfer

### :small_blue_diamond: 3.4.1 Building a Reliable Data Transfer Protocol
### :small_blue_diamond: 3.4.2 Pipelined Reliable Data Transfer Protocols
### :small_blue_diamond: 3.4.3 Go-Back-N (GBN)
### :small_blue_diamond: 3.4.4 Selective Repeat (SR)

## :green_circle: 3.5 Connection-Oriented Transport: TCP

### :small_blue_diamond: 3.5.1 The TCP Connection
### :small_blue_diamond: 3.5.2 TCP Segment Structure
### :small_blue_diamond: 3.5.3 Round-Trip Time Estimation and Timeout
### :small_blue_diamond: 3.5.4 Reliable Data Transfer
### :small_blue_diamond: 3.5.5 Flow Control
### :small_blue_diamond: 3.5.6 TCP Connection Management


## :green_circle: 3.6 Principles of Congestion Control

### :small_blue_diamond:
### :small_blue_diamond:
### :small_blue_diamond:



## :green_circle 3.7 TCP Congestion Control

### :small_blue_diamond:




