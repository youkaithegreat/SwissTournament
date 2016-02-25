#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def executeQuery(query, return_required):
    #runs the query to avoid duplicate code. 
    #if the function requires something to come back it will return 
    #otherwise it will comeback empty
    db = connect()
    c = db.cursor()
    c.execute(query)
    if return_required == True:
        table = c.fetchall()
        db.commit()
        db.close()
        return table
    else:
        db.commit()
        db.close()
        return None 


def deleteMatches():
    """Remove all the match records from the database."""
    executeQuery('DELETE FROM matches', False)


def deletePlayers():
    """Remove all the player records from the database."""
    executeQuery('DELETE FROM players', False)

def countPlayers():
    """Returns the number of players currently registered."""

    player_count_table = executeQuery('SELECT COUNT(player_id) FROM players;', True)
    #Returns the actual value of the count, since it comes back in a table 
    player_count = player_count_table[0][0]
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
 
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO players (player_name) VALUES (%s);', (name,))
    db.commit()
    db.close()



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    player_standings = []
    
    rankings_table = executeQuery('SELECT * FROM rankings ORDER BY wins desc', True)
    for rows in rankings_table:
        total_matches = int(rows[2]) + int(rows[3])
        player_tuple = (rows[0], rows[1], int(rows[2]), total_matches)
        player_standings.append(player_tuple)
    return player_standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s);', (winner, loser,))
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    player_standings = playerStandings()
    player_count = int(countPlayers())
    pairings = []

    if(player_count > 0 ):
        for player in range (player_count):
            if(player%2 == 0):
            #Checks if player count is even and pulls the data from the table
                id1 = player_standings[player][0]
                name1 = player_standings[player][1]
                id2 = player_standings[player+1][0]
                name2 = player_standings[player+1][1]
                pair = (id1, name1, id2, name2)
                pairings.append(pair)
        return pairings
