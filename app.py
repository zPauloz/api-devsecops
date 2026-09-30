from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "security": "enabled"
    })


@app.route("/")
def home():
    return jsonify({
        "message": "API DevSecOps funcionando!"
    })


if __name__ == "__main__":
    app.run()