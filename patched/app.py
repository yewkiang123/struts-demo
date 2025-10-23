# patched/app.py (reject %{} and ${})
from flask import Flask, request, jsonify, make_response
import re

app = Flask(__name__)

# Pattern to detect %{...} or ${...}
PATTERN = re.compile(r"(\%\{.*?\}|\$\{.*?\})", re.DOTALL)

def contains_suspicious(value: str) -> bool:
    if not value:
        return False
    return bool(PATTERN.search(value))

@app.route('/', methods=['GET','POST'])
def index():
    content_type = request.headers.get('Content-Type', '')
    if contains_suspicious(content_type):
        print(f"[PATCHED-REJECT] Blocked suspicious header: {content_type}")
        return make_response(jsonify({
            'error': 'Rejected suspicious payload (simulated patch)',
            'reason': 'Suspicious token in Content-Type header'
        }), 403)

    raw_body = request.get_data(as_text=True)
    if contains_suspicious(raw_body):
        print(f"[PATCHED-REJECT] Blocked suspicious body")
        return make_response(jsonify({
            'error': 'Rejected suspicious payload (simulated patch)',
            'reason': 'Suspicious token in request body'
        }), 403)

    return jsonify({
        'message': 'Request accepted (no suspicious tokens detected)'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
