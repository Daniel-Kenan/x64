import asyncio
import websockets
import socket
import os
from ACtualAI import get_groq_response  # Import the function from ACtualAI

# Get the current machine's IP address and set the port
hostname = socket.gethostname()
IPADDR = socket.gethostbyname(hostname)
PORT = int(os.getenv("PORT", 8765))
HOST = '0.0.0.0'  # Bind to all interfaces

# List of allowed hosts (you can modify this as needed)
ALLOWED_HOSTS = ["*"]

# Define the WebSocket handler
async def handler(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            
            # Get the AI response using the ActualAI function
            ai_response = get_groq_response(message)
            
            # Send the AI response back to the WebSocket client
            await websocket.send(ai_response)
    except websockets.ConnectionClosedOK:
        print("Connection closed normally")

# Start the WebSocket server
print(f"Running on => {IPADDR}:{PORT}")
start_server = websockets.serve(handler, host=HOST, port=PORT)

# Run the server until it is stopped
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
