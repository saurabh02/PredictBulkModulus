import pandas as pd
import sqlite3 as sql

if __name__ == '__main__':
    df = pd.read_pickle('rf_pred_BM.pkl')
    con = sql.connect('flask.db')
    df.to_sql(name='bulkmodulus', con=con)