# Chapter 2 Application Layer

Main driving force to dev Inet - creation of applications:

- text email, remote access to computers, file transfers, and newsgroups
- World Wide Web:
    - Web surfing
    - search
    - electronic commerce

-  instant messaging and P2P file sharing
-  voice and video applications:

    - voice-over-IP (VoIP) and video conferencing over IP such as Skype
    - user-generated video distribution (YouTube)
    - movies on demand (Netflix) 

- multi-player online games
- social networking applications (Facebook, Twitter)

## 2.1 Principles of Network Applications :large_blue_circle:

Network application dev - write programs that:
1. run on different end systems 
2. communicate with each other over the network

For example, Web apps:
1. the browser program running in the user’s host (desktop, laptop, tablet, smartphone, and so on)
2. the Web server program running in the Web server host

You do not need to (and actually can not) write software that runs on network core devices, such as routers or link-layer switches - they do not function at the application layer but instead function at lower layers.

### 2.1.1. Network Apps Architectures :small_blue_diamond:

Two predominant architectural paradigms used in modern network applications: 
- the client-server architecture 
- the peer-to-peer (P2P) architecture

**Client-server architecture**

There is an always-on host, called the **server**, which services requests from many other hosts, called **clients**. 

Web application: always-on Web server services requests from browsers running on client hosts. When a Web server receives a request for an object from a client host, it responds by sending the requested object to the client host. 

Clients do not directly communicate with each other (in the Web application, two browsers do not directly communicate). 

Another characteristic of the client-server architecture is that the server has a fixed, well-known IP address.

Apps with a client-server architecture: Web, FTP, Telnet, and e-mail. 

To keep up with requests from clients - virtual server in data center. Google has 30 to 50 data centers distributed around the world, which collectively handle search, YouTube, Gmail, and other services. A data center can have 100s of 1000s of servers, which must be powered and maintained. Additionally, the service providers must pay recurring interconnection and bandwidth costs for sending data from their data centers.

**P2P architecture**

No dedicated servers. Instead -  direct communication between pairs of intermittently connected hosts, **peers**. E.g. file sharing (BitTorrent), peer-assisted download acceleration (Xunlei), Internet Telephony (Skype), and IPTV (Kankan and PPstream).

Some apps have hybrid architectures, combining both client-server and P2P elements. For example, for many instant messaging applications, servers are used to track the IP addresses of users, but user-to-user messages are sent directly between user hosts (without passing through intermediate servers).

P2P architectures pros:
- self-scalability
- cost effective


P2P architectures cons:
- most residential ISPs have been dimensioned for “asymmetrical” bandwidth usage, that is, for much more downstream than upstream traffic. P2P video streaming and file distribution apps shift upstream traffic from servers to residential ISPs,thereby putting significant stress on the ISPs.
- challenge to secure
- The success of P2P applications depends on convincing users to volunteer bandwidth, storage, and computation resources to the apps, which is the challenge of incentive design 

### 2.1.2 Processes Communicating

**A process** - a program that is running within an end system. When processes are running on the same end system, they can communicate with each other with interprocess communication, using rules that are governed by the end system’s operating system.

Processes on two different end systems communicate with each other by exchanging **messages** across the computer network. A sending process creates and sends messages into the network; a receiving process receives these messages and possibly responds by sending messages back.

 **Client and Server Processes**

Label one of the two processes as the client and the other process as the server (“client side and server side of an application”). Web: a browser is a client process and a Web server is a server process. P2P file sharing: the peer that is downloading the file is labeled as the client, and the peer that is uploading the file is labeled as the server.

In the context of a communication session between a pair of processes, the process that initiates the communication (that is, initially contacts the other process at the beginning of the session) is labeled as the client. The process that waits to be contacted to begin the session is the server.

**The Interface Between the Process and the Computer Network**

A process sends messages into, and receives messages from, the network through a software interface called a **socket**.

![This is an image](2.3.png)

A **socket** is the interface between the application layer and the transport layer within a host. It is also referred to as the **Application Programming Interface (API)** between the application and the network, since the socket is the programming interface with which network applications are built.

The application developer has control of everything on the app-layer side of the socket but has little control of the transport-layer side of the socket. The only control that the application developer has on the transport-layer side is:
1. choice of transport protocol  
2. fix a few transport-layer parameters such as max buffer and max segment sizes 

**Addressing Processes**

In order for a process running on one host to send packets to a process running on another host, the receiving process needs to have an address.

To identify the receiving process, two pieces of information need to be specified: (1) the address of the host -  IP address
(2) an identifier that specifies the receiving process  (more specifically, the receiving socket) in the destination host - destination **port number** serves this purpose.

Web server is identified by port number 80; A mail server process (using the SMTP protocol) is identified by port number 25. 

### 2.1.3 Transport Services Available to Applications

Need to choose transport-layer protocol based on provided services:
- reliable data transfer
- throughput
- timing
- security

**Reliable Data Transfer**

If a protocol provides a guaranteed data delivery service - Reliable Data Transfer.
Transport-layer protocol can potentially provide process-to-process reliable data transfer.

Without reliable data transfer - some of the data sent by the sending process may never arrive at the receiving process. This may be acceptable for **loss-tolerant applications** (multimedia apps such as conversational audio/video that can tolerate some amount of data loss. Lost data might result in a small glitch in the audio/video—not a crucial impairment).

**Throughput**

Available throughput - the rate at which the sending process can deliver bits to the receiving process. Can fluctuate as other sessions is sharing bandwidth along the network path.

Transport layer can potentially provide guaranteed available throughput (bits/sec). Important for **bandwidth-sensitive apps** (multimedia apps).

**Elastic applications** can make use of as much, or as little, throughput as happens to be available. Electronic mail, file transfer, and Web transfers are all elastic applications.

**Timing**

Timing guarantees can be in diff form, e.g. every bit that the sender pumps into the socket arrives at the receiver’s socket no more than 100 msec later. \
Important for interactive real-time applications - Internet telephony, virtual environments, teleconferencing, and multiplayer games.

**Security**

Examples:

- confidentiality: in the sending host, a transport protocol can encrypt all data transmitted by the sending process, and in the receiving host, the transport-layer protocol can decrypt the data before delivering the data to the receiving process. Such a service would provide confidentiality between the two processes, even if the data is somehow observed between sending and receiving processes. 
- data integrity 
- end-point authentication

### 2.1.4 Transport Services Provided by the Internet

The Internet (and, more generally, TCP/IP networks) makes two transport protocols available to applications, UDP and TCP.

The service requirements for some selected applications:

![This is an image](2.4.png)

**TCP Services**

The TCP service model includes a connection-oriented service and a reliable data transfer service. When an application invokes TCP as its transport protocol, the application receives both of these services from TCP.

- **Connection-oriented service**  
    **Handshaking procedure**:
    - TCP has the client and server exchange transport layer control information with each other before the app-level messages begin to flow.
    - Alerts the client and server, allowing them to prepare for an onslaught of packets. After the handshaking phase, a TCP connection is said to exist between the sockets of the two processes.
    - The connection is a full-duplex connection in that the two processes can send messages to each other over the connection at the same time. 
    - When the application finishes sending messages, it must tear down the connection. 


- **Reliable data transfer service.** All data sent without error and in the proper order. When one side of the application passes a stream of bytes into a socket, it can count on TCP to deliver the same stream of bytes to the receiving socket, with no missing or duplicate bytes.

- **Congestion-control mechanism**

**UDP Services**

Lightweight transport protocol, providing minimal services; no handshaking; unreliable data transfer; no congestion-control mechanism;  

**Services Not Provided by Internet Transport Protocols**

- reliable data transfer - Yes (TCP)
- throughput - No guarantees
- timing - No guarantees
- security - Yes (TCP)

Time-sensitive apps in Inet often work fairly well because they have been designed to cope, to the greatest extent possible, with this lack of guarantee --> Internet can often provide satisfactory service to time-sensitive applications, but no timing or throughput guarantees.

Many firewalls are configured to block (most types of) UDP traffic.


![This is an image](2.5.png)

### 2.1.5 Application-Layer Protocols

An application-layer protocol defines how an application’s processes, running on diff end systems, pass messages to each other:
- The types of messages exchanged, for example, request messages and response messages
- The syntax of the various message types, such as the fields in the message and how the fields are delineated
- The semantics of the fields - the meaning of the information in the fields
- Rules for determining when and how a process sends messages and responds to
messages

App-layer protocols:

- public (HTTP)
- proprietary (Skype)

Network applications vs application-layer protocols:

Web app:
-  standard for document formats, eg **HTTP (the HyperText Transfer Protocol)**
-  Web browsers (Firefox and Microsoft Internet Explorer)
-  Web servers (Apache and Microsoft servers)
-  app-layer protocol , HTTP, defines the format and sequence of messages exchanged between browser and Web server

Internet e-mail app:
-  mail servers that house user mailboxes
-  mail clients (such as Microsoft Outlook) that allow users to read and create messages
-  a standard for defining the structure of an e-mail message
-  and app-layer protocols that define how messages are passed between servers, how messages are passed between servers and mail clients, and how the contents of message headers are to be interpreted. e.g. **SMTP (Simple Mail Transfer Protocol)**


## 2.2 The Web and HTTP

Until the early 1990s the Internet was used by researchers, academics, and university students to log in to remote hosts, to transfer files from local hosts to remote hosts and vice versa, to receive and send news, and to receive and send electronic mail.\
2003 - YouTube, Gmail, and Facebook.


### 2.2.1 Overview of HTTP

HTTP is implemented in two programs: (1) a client program and (2) a server program. They talk to each other by exchanging HTTP messages. HTTP defines the structure of these messages and how the client and server exchange the messages.

A Web page ( document) consists of objects. An object is simply a file (HTML file, a JPEG image, a Java applet, a video clip)—that is addressable by a single URL. Most Web pages consist of a base HTML file and several referenced objects. For example, if a Web page contains HTML text and five JPEG images, then the Web page has six objects: the base HTML file plus the five images. The base HTML file references the other objects in the page with the objects’ URLs. Each URL has two components: the hostname of the server that houses the object and the object’s path name. For example, the URL
http://www.someSchool.edu/someDepartment/picture.gif
has www.someSchool.edu for a hostname and /someDepartment/ picture.gif for a path name. 
Web browsers (Internet Explorer,Firefox) - implement the client side of HTTP --> we will use the words browser and client interchangeably. 
Web servers - implement the server side of HTTP, house Web objects, each addressable by a URL. Popular Web servers include Apache and Microsoft Internet Information Server.

 HTTP server maintains no info about the clients - **stateless protocol**. 

 ### 2.2.2 Non-Persistent and Persistent Connections
