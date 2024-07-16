from flask import Flask,request,jsonify
from ScoreApp import app
from ScoreApp import db

@app.route('/')
def index():
    print('client connected!')
    return 'hello manager!'

@app.route('/sendData', methods=['POST'])
def sendData():
    data = request.json
    score = data.get('score')
    player_name = data.get('playerName')
    
    db.add_data(score, player_name)
    print(f'success : /sendData\nscore : {score}\nplayer_name : {player_name}')
    return(jsonify({'score': score, 'player_name': player_name}))

@app.route('/getData', methods=['GET'])
def getData():
    data = db.display_list()
    print('success : /getData')
    return data