-- This file sets up the tournament database for use with the tournament.py 
-- 
-- Instructions for use can be found in the Readme.MD 
-- 
-- File Drops the Database tournament if it exists, so as to not have any runtime issues 
-- 
-- File creates new players and matches table

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;


-- Creates the player tables with ID and name. 

CREATE TABLE players  ( player_id serial primary key,
                        player_name varchar (40) not null );

-- Creates matches tables. 
-- Winner and Loser ID's are Foreign key references to the existing players

CREATE TABLE matches  ( match_id serial primary key,
                        winner_id int,
                        loser_id int,
                        foreign key (winner_id) references players(player_id),
                        foreign key (loser_id) references players(player_id) );

-- rankings is a view created with the info from players and matches 
CREATE VIEW rankings AS 
SELECT player_id, player_name, 
	(SELECT count(*) FROM matches WHERE player_id = winner_id) AS wins,
	(SELECT count(*) FROM matches WHERE player_id IN (winner_id, loser_id)) AS matches
FROM players
GROUP BY player_id;

/*

INSERT INTO players (player_name) VALUES ('kevin');
INSERT INTO players (player_name) VALUES ('John');
INSERT INTO players (player_name) VALUES ('bob');

insert into matches (winner_id, loser_id) values ('1', '2');

insert into matches (winner_id, loser_id) values ('1', '2');

insert into matches (winner_id, loser_id) values ('1', '2');

insert into matches (winner_id, loser_id) values ('1', '2');

insert into matches (winner_id, loser_id) values ('2', '3');

insert into matches (winner_id, loser_id) values ('2', '3');

insert into matches (winner_id, loser_id) values ('2', '3');

insert into matches (winner_id, loser_id) values ('2', '3');
	*/