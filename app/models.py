import pymongo

client = pymongo.MongoClient()
db = client.flask
coll = db['bulkmodulus']


def display(pretty_formula):
    result_properties = coll.find_one({'pretty_formula': pretty_formula})
    return result_properties


# import sqlite3 as sql
#
# def insert_customer(company,email):
#     with sql.connect("app.db") as con:
#         cur = con.cursor()
#         cur.execute("INSERT INTO customers (company,email) VALUES (?,?)", (company,email))
#         con.commit()
#
# def retrieve_customers():
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         result = cur.execute("select * from customers").fetchall()
#         print result
#     return result
