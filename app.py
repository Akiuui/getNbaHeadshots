from flask import Flask, request, jsonify
from nba_api.stats.static import players
app = Flask(__name__)

@app.route("/")
def getPlayer():
    fullName = request.args.get("fullName").lower().strip()

    player = players.find_players_by_full_name(fullName)

    if len(player) > 1:
        return jsonify({"Exception":"There are multiple players with same name"})

    if len(player) < 1:
        return jsonify({"Error":"Player with that name not found"})

    player = player[0]

    imgLink = f"https://cdn.nba.com/headshots/nba/latest/1040x760/{player["id"]}.png"

    return jsonify({"Image link":imgLink})

if __name__ == '__main__':
    from waitress import serve
    serve(app, port=8007)
    # app.run(debug=False)

