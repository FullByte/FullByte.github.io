# Wireshark

| What          | Where                        |
|---------------|------------------------------|
| Official Site | <https://www.wireshark.org/> |
| Ubuntu        | `sudo apt install wireshark` |

## Disectors

Wireshark dissectors are modules within the Wireshark network protocol analyzer that are responsible for interpreting the data structures of specific protocols. When Wireshark captures network traffic, it does not inherently understand the structure and meaning of the data traversing the network. Dissectors are used to analyze and decode the data packets and put the raw data into a human-readable format. Each dissector is designed for a specific protocol (such as TCP, HTTP, FTP, etc.). It understands the structure of the protocol, e.g. header, payload and footer. The dissector takes the bytes of a packet belonging to its protocol and breaks them down into the various fields and elements defined in the protocol's specification. This process allows users to view, analyze and understand the details of network traffic in a structured and meaningful way.

Source: https://wiki.wireshark.org/Lua/Dissectors