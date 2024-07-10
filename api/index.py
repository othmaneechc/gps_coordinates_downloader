# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/about')
# def about():
#     return 'About'

import csv
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save_coords', methods=['POST'])
def save_coords():
    data = request.json
    lat = data['lat']
    lng = data['lng']
    with open('coordinates.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([lat, lng])
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
