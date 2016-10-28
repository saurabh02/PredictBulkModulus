import sqlite3 as sql


# import pymongo
#
# client = pymongo.MongoClient()
# db = client.flask
# coll = db['bulkmodulus']
#
#
# def display(pretty_formula):
#     result_properties = coll.find_one({'pretty_formula': pretty_formula})
#     return result_properties


# import sqlite3 as sql
#
# def insert_customer(company,email):
#     with sql.connect("app.db") as con:
#         cur = con.cursor()
#         cur.execute("INSERT INTO customers (company,email) VALUES (?,?)", (company,email))
#         con.commit()
#

def display(pretty_formula):
    with sql.connect("GBR_pred_BM.db") as con:
    # with sql.connect("flask.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM GBR_pred_BMR WHERE lower(pretty_formula)=?",
                             (pretty_formula.lower(),)).fetchall()
        # result = cur.execute("SELECT * FROM bulkmodulus WHERE lower(pretty_formula)=?",
        #                      (pretty_formula.lower(),)).fetchall()
        print result
    return result
