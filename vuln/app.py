from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():

    content_type = request.headers.get("Content-Type", "")
    print(f"[VULN SERVER] Received Content-Type: {content_type}")
    return jsonify({
        "message": "Simulated vulnerable echo",
        "received_header": content_type
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
