
export PGHOSTADDR=127.0.0.1
psql -c "CREATE DATABASE chinook"
psql -d chinook -f Chinook_PostgreSql.sql
