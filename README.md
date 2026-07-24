# LAN Chat Application

## Description

A real-time text chat application built with Python using the Client-Server architecture. The application allows multiple clients to communicate over a Local Area Network (LAN) using TCP sockets.

---

## Features

- Real-time messaging
- Multi-client support
- Client-Server architecture
- Socket Programming
- Multi-threading
- Broadcast messages to all connected clients

---

## Requirements

- Python 3.x

---

## Project Structure

```
LAN-CHAT/
│── server.py
│── client.py
│── README.md
```

---

## How to Run

### Start the Server

```bash
python server.py
```

### Start the Client

Open a new terminal and run:

```bash
python client.py
```

Run multiple clients to test the chat application.

---

## Running on a Local Network (LAN)

1. Find the server's IPv4 address using:

```bash
ipconfig
```

2. Update the server IP inside `client.py`:

```python
client.connect(("SERVER_IP", 5555))
```

Replace `SERVER_IP` with the server's IPv4 address.

3. Make sure all devices are connected to the same local network.

---

## How It Works

- The server creates a socket and binds it to an IP address and port.
- The server listens for incoming client connections.
- Each connected client is handled in a separate thread.
- Messages received from one client are broadcast to all other connected clients.
- Clients can send and receive messages simultaneously.

---

## Files

- `server.py` – Server application
- `client.py` – Client application
