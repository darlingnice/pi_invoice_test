from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit,send
import base64

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins

@app.route('/signature', methods=["POST"])
def get_signature():
    data: dict = request.get_json()
    image_data: str = data.get("image")

    if image_data and image_data.startswith("data:image"):
        image = image_data.split(',')[-1]
        # with open('image.png', 'wb') as image_obj:
        socketio.emit("new_signature", {"image": image_data})
        return "Image saved successfully", 200
    return "Invalid image data", 400


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html', signature="")


@socketio.on("connect")
def handle_connect():
    print("Connection accepted")
    emit("connection_response", {"message": "Connection was granted"})



if __name__ == "__main__":
    socketio.run(app,host='0.0.0.0', debug=True, port=5001)
