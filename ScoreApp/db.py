import sqlite3
from flask import jsonify

DATABASE = 'game_data.db'

def get_db_connection():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    return con

def create_db_table():
    con = get_db_connection()
    
    create_players_query = ('''CREATE TABLE IF NOT EXISTS players (
                                player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                player_name TEXT NOT NULL,
                                created_at TEXT NOT NULL DEFAULT (datetime('now'))
                            );
                            ''')
    
    create_scores_query = ('''CREATE TABLE IF NOT EXISTS scores (
                                score_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                score INTEGER NOT NULL DEFAULT 0,
                                player_id INTEGER NOT NULL,
                                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                                FOREIGN KEY (player_id) REFERENCES players(player_id)
                            );
                            ''')
    
    con.execute(create_players_query)
    con.execute(create_scores_query)
    con.commit()
    con.close()

def add_player(player_name_data):
    con = get_db_connection()
    
    add_player_query = ('''
            INSERT INTO players (player_name)
            VALUES (?)
            ''')
    
    con.execute(add_player_query, [player_name_data])
    con.commit()
    con.close()

def get_player_id(player_name_data):
    con = get_db_connection()
    
    get_id_query = ('''
            SELECT *
            FROM players
            WHERE player_name = ?
            ORDER BY created_at DESC
            LIMIT 1
            ''')
    
    player = con.execute(get_id_query, [player_name_data]).fetchone()
    
    if player:
        player_id = player['player_id']
    else:
        add_player(player_name_data)
        next_player = con.execute(get_id_query, [player_name_data]).fetchone()
        player_id = next_player['player_id']
    
    con.close()
    
    return player_id

def add_score(score_data, player_name_data):
    con = get_db_connection()
    
    add_score_query = ('''
            INSERT INTO scores (score, player_id)
            VALUES (?, ?)
            ''')
    player_id = get_player_id(player_name_data)
    
    con.execute(add_score_query, [score_data, player_id])
    con.commit()
    con.close()

def add_data(score_data, player_name_data):
    add_player(player_name_data)
    add_score(score_data, player_name_data)
    
    score = score_data
    player_name = get_player_id(player_name_data)

def display_list():
    con = get_db_connection()
    
    get_list_query = ('''
            SELECT scores.score, players.player_name
            FROM scores INNER JOIN players
            WHERE scores.player_id = players.player_id
            ORDER BY scores.score DESC
            LIMIT 5
            ''')
    db_list = con.execute(get_list_query).fetchall()
    
    score_and_player = []
    for data in db_list:
        score_and_player.append({"score" : data['score'], "playerName" : data['player_name']})
    
    con.close()
    return jsonify(score_and_player)