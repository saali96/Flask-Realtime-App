# Flask Realtime App

This repository contains a simple real-time server implementation using Flask and Socket.IO. The project demonstrates how to establish WebSocket connections between clients and a server to achieve real-time communication.

## Features:
1. WebSocket Communication: Utilizes Socket.IO for bidirectional communication between the server and connected clients.
1. User Tracking: Keeps track of the number of connected users in real-time.
1. Event Handling: Listens for 'connected' and 'disconnected' events to update the user count dynamically.

## Technologies Used:
1. Frontend: HTML, JavaScript (Socket.IO client)
1. Backend: Flask, Socket.IO

## How to Use:
1. Clone the repository: git clone https://github.com/your-username/real-time-server.git
1. Install dependencies: pip install -r requirements.txt
1. Run the server: python app.py
1. Open http://127.0.0.1:5000/ in your browser to connect to the real-time server.

Feel free to explore, modify, and integrate this real-time server into your projects. If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

Happy coding!
