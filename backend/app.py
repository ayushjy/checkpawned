from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/check", methods=["GET"])
def check():
    email = request.args.get("email")
    
    # XposedOrNot API endpoint
    url = f"https://api.xposedornot.com/v1/check-email/{email}"

    try:
        r = requests.get(url)
        
        # XposedOrNot returns 404 if email is not found in any breach (Safe)
        if r.status_code == 404:
            return jsonify({"safe": True, "breaches": []})
            
        # If 200, it returns the breach data
        if r.status_code == 200:
            data = r.json()
            # XposedOrNot returns 'breaches' (lowercase) which can be a list of lists 
            # e.g. [["Breach1", "Breach2", ...]]
            raw_breaches = data.get('Breaches') or data.get('breaches', [])
            
            # Additional check: If raw_breaches is a dict, it might be nested (safety check)
            if isinstance(raw_breaches, dict):
                raw_breaches = raw_breaches.get('breaches') or raw_breaches.get('Breaches', [])

            final_breaches = []
            if isinstance(raw_breaches, list):
                for item in raw_breaches:
                    if isinstance(item, list):
                        final_breaches.extend(item)
                    else:
                        final_breaches.append(item)
            else:
                 final_breaches = raw_breaches

            return jsonify({"safe": False, "breaches": final_breaches})

        return jsonify({"safe": True, "error": "Unexpected API response"}), 500

    except Exception as e:
         return jsonify({"error": str(e)}), 500


app.run(debug=True)
