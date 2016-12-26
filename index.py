import random
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/calculate', methods=['POST'])
def calculate():
  megasena_expense = 3.50

  money = float(request.form['money'])

  games_quantity = int(money / megasena_expense)

  games = []

  for i in range(0, games_quantity):
    a_game = set()

    while True:
      number = random.randrange(1, 61, 3)
      a_game.add(number)

      if len(a_game) == 6:
        games.append(a_game)
        break


  return render_template('calculate.html', money=money, games_quantity=games_quantity, games=games)

if __name__ == '__main__':
  app.run()
