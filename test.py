import os
import pprint
import psycopg2


pprint.pprint(dict(os.environ), width=1)


with psycopg2.connect(database=os.environ['POSTGRES_DB']) as conn:
    cr = conn.cursor()
