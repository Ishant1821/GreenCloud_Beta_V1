from flask import Flask, render_template, request, jsonify
from ml_engine import predict_metrics

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def get_prediction():
    data = request.get_json() or {}
    cpu_load = float(data.get('cpu_load', 50.0))
    ram_usage = float(data.get('ram_usage', 60.0))

    # Get prediction from ML model
    res = predict_metrics(cpu_load, ram_usage)

    # Optimization Logic
    decision = "OPTIMAL"
    if cpu_load < 25:
        decision = "INITIATE_DEEP_SLEEP"
    elif cpu_load > 80:
        decision = "TRIGGER_VM_MIGRATION"

    res['decision'] = decision
    res['cpu_load'] = cpu_load
    res['ram_usage'] = ram_usage
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, port=5000)