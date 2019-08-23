import sqlite3

conn = sqlite3.connect('countries.db')
c = conn.cursor()

c.execute("CREATE TABLE factors_by_countries (country text, coefficient real)")

with open("countries.txt") as f:
    countries = f.readlines()
    for country in countries:
        c.execute("INSERT INTO factors_by_countries VALUES ('{}', '{}')".format(country, 0.8))

conn.commit()
conn.close()
