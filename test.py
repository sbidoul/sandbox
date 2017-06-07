import os
import pprint
import psycopg2


pprint.pprint(dict(os.environ), width=1)


with psycopg2.connect() as conn:
    cr = conn.cursor()
