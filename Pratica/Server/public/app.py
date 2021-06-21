from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index():
    return render_template('index.html', sync_mode=socketio.async_mode)

@app.route('/dashboard')
def dashboard():
    return render_template('sgu.html', sync_mode=socketio.async_mode)

@app.route('/data_from_sgu', methods=['POST'])
def process_data():
    content = request.get_json(force=False)
    print(content)
    transmit_json(content)
    resp = jsonify(success=True)
    return resp

@socketio.on('json')
def transmit_json(json_data):
    socketio.emit('sgu_data', json_data)

@socketio.on('connect', namespace='/')
def connect():
    print("Connected to SocketIO!")


if __name__ == '__main__':
    socketio.run(app, debug=True)
