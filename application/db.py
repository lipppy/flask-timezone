import psycopg2
import psycopg2.extras

from flask_sqlalchemy import SQLAlchemy

from application import app

# Connect to PostgreSQL database
db_postgresql = SQLAlchemy(app)

# Connect to PostGIS database
pg_host = app.config['PG_DB_HOST']
pg_port = app.config['PG_DB_PORT']
pg_name = app.config['PG_DB_NAME']
pg_username = app.config['PG_DB_USERNAME']
pg_password = app.config['PG_DB_PASSWORD']

db_postgis = psycopg2.connect(
    host=pg_host,
    port=pg_port,
    database=pg_name,
    user=pg_username,
    password=pg_password
)

def get_cursor():
    return db_postgis.cursor(cursor_factory=psycopg2.extras.DictCursor)