from flask import Flask, render_template, request, redirect, flash
import random


#Creating application
app = Flask(__name__)
app.config['Debug'] = True

numbers_chosen = []
def get_number(length):
    number = random.randint(0, length-1)
    while number in numbers_chosen:
        number = random.randint(0, length -1)
    numbers_chosen.append(number)
    return number

def generate_card(size):
    bingo_bank = open("bingo-texts.txt").read().splitlines()
    bingo_card_data = []
    numbers_chosen.clear()
    for i in range(size*size):
        index = get_number(len(bingo_bank))
        bingo_card_data.append(bingo_bank[index])
    print(bingo_card_data)
    return bingo_card_data


@app.route("/")
def index():
    size = 3;
    bingo_data = generate_card(size)
    print('below is data')
    print(bingo_data)
    print(numbers_chosen)
    return render_template("index.html", bingo_data = bingo_data, size = size)


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)

