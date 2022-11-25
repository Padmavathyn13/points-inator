from flask import Flask, render_template
import os
import random

app = Flask(__name__)
board = {}
board['name'] = 'haddy'
board['users'] = ['Paddy','Harry','Puffs']

points = {}
points['Paddy'] = 10
points['Harry'] = 10
points['Puffs'] = 5
board['points'] = points
options = [1,2,3,5,10,15,20,50,100,'1000 !']
@app.route("/")
def index():
    # url = random.choice(images)

    return render_template("index.html", boards = board, options = options)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))