from flask import Flask, request, jsonify
import os
import logging
from nba_api.stats.static import players
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@app.route("/")
def getPlayer():
    fullName = request.args.get("fullName")

    if fullName is None:
        logging.error("The arg 'fullName' is not entered")
        return jsonify({"Error":"The arg 'fullName' is not entered"})
    else:
        logging.info(f"The args is fullName: {fullName}")
    
    fullName = fullName.lower().strip()
    logging.info("Trying to find a player with his name")
    player = players.find_players_by_full_name(fullName)
    logging.info("Found the player")

    if len(player) > 1:
        logging.error("There are multiple players with same name")
        return jsonify({"Exception":"There are multiple players with same name"})

    if len(player) < 1:
        logging.error(" with that name not found")
        return jsonify({"Error":"Player with that name not found"})

    player = player[0]

    imgLink = f"https://cdn.nba.com/headshots/nba/latest/1040x760/{player['id']}.png"

    return jsonify({"Image link":imgLink})

if __name__ == '__main__':
    from waitress import serve
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 8006))
    serve(app, host="0.0.0.0", port=port)

