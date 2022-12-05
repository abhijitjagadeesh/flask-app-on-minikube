from flask import Flask
import uuid

app = Flask(__name__)

@app.route("/")
def get_instance_uuid():
    return f"Instance id: {uuid.uuid4()}"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 6000)  