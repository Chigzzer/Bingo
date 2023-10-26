from flask import Flask, render_template, request, redirect, flash
import random


#Creating application
app = Flask(__name__)
app.config['Debug'] = True


numbers_chosen = []
bingo_bank = [i for i in range(20)]

def get_number():
    number = random.randint(0, len(bingo_bank)-1)
    while number in numbers_chosen:
        number = random.randint(0, len(bingo_bank) -1)
    numbers_chosen.append(number)
    return number

def generate_card():
    bingo_card_data = []
    numbers_chosen.clear()
    for i in range(9):
        index = get_number()
        bingo_card_data.append(bingo_bank[index])
    print(bingo_card_data)
    return bingo_card_data




@app.route("/")
def index():
    bingo_data = generate_card()
    print('below is data')
    print(bingo_data)
    print(numbers_chosen)
    return render_template("index.html", bingo_data = bingo_data)


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)

