"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr9j9euhlq287daakg-a.singapore-postgres.render.com",
        database="jin_db",
        user="jin_db_user",
        password="qpWO24Db3gg0hPFLynpTEXxJcnv9QSw8")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
