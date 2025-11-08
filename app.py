from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# sample data (you can extend or hook to a real API later)
sample_data = {
    "city": "Sample City",
    "today_waste_tons": 15.2,
    "predicted_tomorrow_tons": 16.4,
    "recycling_rate": 45,
    "daily": [8, 9, 10, 12, 13, 14, 15],
    "dates": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "bins": [
        {"id": "Bin 1", "lat": 40.7128, "lon": -74.0060, "fill_pct": 85},
        {"id": "Bin 2", "lat": 40.7158, "lon": -74.0020, "fill_pct": 60},
        {"id": "Bin 3", "lat": 40.7108, "lon": -74.0120, "fill_pct": 95}
    ]
}

@app.route("/")
def index():
    # render HTML template that uses Plotly + Leaflet (files in templates/)
    return render_template("index.html", data=json.dumps(sample_data))

# optional: endpoint to return JSON (useful later)
@app.route("/api/data")
def api_data():
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
