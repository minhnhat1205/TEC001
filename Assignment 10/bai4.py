from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load airport data from JSON file
with open("airports.json", "r", encoding="utf-8") as file:
    airports = json.load(file)


@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    icao = icao.upper()

    for airport in airports:
        if airport["icao"] == icao:
            return jsonify({
                "icao": airport["icao"],
                "name": airport["name"],
                "city": airport["municipality"],
                "country": airport["iso_country"]
            })

    # If not found
    return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)