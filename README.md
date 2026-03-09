A collection of lightweight, educational TCP and UDP clients written in Python that demonstrate raw socket programming. These tools allow you to connect directly to any server, send custom data, and receive responses - showing you exactly what happens "under the hood" of network communications.

 ![Screenshot](https://github.com/user-attachments/assets/52ef3281-c0cb-4bf9-8997-81f74d48ccdd)
 <img width="710" height="382" alt="image" src="https://github.com/user-attachments/assets/a8c09acf-96d8-44a4-b6be-8c1737ed7656" />

 1. TCP Client (Connection-Oriented)
2. UDP Client (Connectionless)

TCP CLIENT
What Does It Do?
This TCP client acts like a universal network telephone - it can call any computer/server and have a raw conversation. Unlike web browsers that hide the technical details, this tool shows you the actual data being exchanged.

Core Functionality:
Establishes TCP connections to any host and port

Sends custom data or HTTP requests

Receives and displays raw server responses

Handles both text and binary data

Why Use TCP Client?
Educational Value
Learn how TCP/IP connections actually work

Understand protocols like HTTP, FTP, SMTP at the raw level
See what browsers do behind the scenes
Debugging & Testing
Test if servers are responding correctly
Debug network services without browser interference
Verify firewall rules and connectivity
Banner grabbing (identify server software)
Security Research
Penetration testing basics
Vulnerability assessment
Understanding attack surfaces
TCP Client Features:
Pure Python (no external dependencies)
Interactive command-line interface
Custom message support

What Does It Do?
This UDP client acts like sending postcards through the internet - fast, connectionless communication without the overhead of establishing a connection. Perfect for understanding how real-time applications work.

Core Functionality:
Sends UDP datagrams to any host and port

Optional response waiting with timeout

Broadcast capability (send to all devices on network)

Fire-and-forget mode

Works with any UDP service

Why Use UDP Client?
Educational Value
Understand connectionless protocols

Learn difference between TCP and UDP

See how DNS, DHCP, NTP actually work

Understand packet-based communication

Real-Time Applications
Game server testing
Voice/video chat debugging
Streaming protocol analysis
IoT device communication
Network Diagnostics
Test UDP port availability
DNS query testing
NTP time server checking
Network discovery via broadcast
UDP Client Features:
Pure Python (no external dependencies)
Interactive command-line interface
Configurable timeout settings
Broadcast support
Fire-and-forget mode
Response waiting option
Error handling
Color-coded mahogany brown banner
Works with any UDP service
HTTP GET request generator
Timeout handling (prevents hanging)
Error handling for network issues
Color-coded mahogany brown banner
Works with any TCP service
