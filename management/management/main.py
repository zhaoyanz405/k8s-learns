from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/nfs', methods=['POST'])
def handle_nfs_server():
    # Get the JSON data from the request
    data = request.get_json()

    # Check if 'nfs_server' is provided in the request
    if not data or 'nfs_server' not in data:
        return jsonify({"error": "Missing 'nfs_server' parameter"}), 400

    nfs_server = data['nfs_server']

    # Process the nfs_server parameter (example: just return it for now)
    return jsonify({"message": f"NFS server '{nfs_server}' received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
