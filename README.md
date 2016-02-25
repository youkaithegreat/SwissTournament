# Swiss Tournament Project
This is a small project that creates a database of matches and assigns the matches to the players. 

## How to Run 
I'm running this in a Vagrant on Virtual Box. 

The vagrant file is included. You must install Virtual Box and Git for this to work. 
* Go to the Directory thaat the Vagrantfile is located
* Type in "Vagrant Up" to start the VM
* After it's done type in "Vagrant SSH" to connect to it
* Find the directory vagrant -> tournament 
* Set up the psql database by typing "psql"
* Type in "\i tournament.sql" enter
* You should see it create the database and tables 
* Afterwards type \q to exit. 
* In your original folder with the tournament.py run "python tournament_test.py" and you should see the results 

### Resources Uses for this: 
http://stackoverflow.com/questions/2596670/how-do-you-find-the-row-count-for-all-your-tables-in-postgres
http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format
http://www.tutorialspoint.com/postgresql/postgresql_views.htm
http://www.postgresql.org/docs/9.2/static/sql-createview.html
http://www.tutorialspoint.com/postgresql/postgresql_count_function.htm
https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true
http://rogerdudler.github.io/git-guide/