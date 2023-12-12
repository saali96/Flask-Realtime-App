from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize a variable to keep track of connected users
connected_users = 0

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connected')
def handle_connect():
    global connected_users
    connected_users += 1
    print(f'\nUser connected. Total connected users: {connected_users}\n')
    # Emit an event to update the connected users on the client side
    emit('update_users', {'count': connected_users}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    global connected_users
    connected_users -= 1
    print(f'\nUser disconnected. Total connected users: {connected_users}\n')
    # Emit an event to update the connected users on the client side
    emit('update_users', {'count': connected_users}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
