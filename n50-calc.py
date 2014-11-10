import os
from flask import Flask, request
app = Flask(__name__)


def n50_calc(list_of_lengths):
    result = 0
    sum_of_lengths = sum(list_of_lengths)
    for num in range(1, len(list_of_lengths)):
        current_sum = sum(list_of_lengths[0:num])
        if current_sum >= sum_of_lengths/2:
            result = list_of_lengths[num-1]
            break
    return result



@app.route('/')
def hello():
    request_nums = request.args.getlist('num')
    


    return str(n50_calc(map(int, request_nums)))


if __name__ == '__main__':
    app.run(debug=True)
