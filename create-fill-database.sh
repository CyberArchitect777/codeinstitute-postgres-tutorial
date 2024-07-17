
pip3 install sqlalchemy==1.4.46
pip3 install psycopg2
export PGHOSTADDR=127.0.0.1
psql -c "CREATE DATABASE chinook"
psql -d chinook -f Chinook_PostgreSql.sql
