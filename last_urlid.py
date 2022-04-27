import sqlite3

from flask import request


class last_url():

    def lasturl(self):
        con = sqlite3.connect('urldatabase.db')
        print("successfully created database")

        cursorObj = con.cursor()

        cursorObj.execute("SELECT urlid FROM urltable ORDER BY urlid DESC LIMIT 1")
        result = cursorObj.fetchone()
        print(result[0])
        con.commit()
        cursorObj.close()
        con.close()

        print("got successfully")


        return result[0]





