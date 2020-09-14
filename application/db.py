import psycopg2
import psycopg2.extras

from application import app

# Connect to PostGIS database
pg_db_host = app.config['PG_DB_HOST']
pg_db_port = app.config['PG_DB_PORT']
pg_db_name = app.config['PG_DB_NAME']
pg_db_username = app.config['PG_DB_USERNAME']
pg_db_password = app.config['PG_DB_PASSWORD']

db_postgis = psycopg2.connect(
    host=pg_db_host,
    port=pg_db_port,
    database=pg_db_name,
    user=pg_db_username,
    password=pg_db_password
)

def get_cursor():
    return db_postgis.cursor(cursor_factory=psycopg2.extras.DictCursor)
