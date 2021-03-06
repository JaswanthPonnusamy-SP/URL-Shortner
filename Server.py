import sqlite3

from flask import request, Flask, render_template
from werkzeug.utils import redirect


from decodeurl import decode_url
from encodeurl import encode_url
from last_urlid import last_url

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
HOST = "127.0.0.1"
PORT = 8010

@app.route('/')
def homeToRedirect():
    return redirect("/urlshortner")

@app.route('/<some_url>')
def redirect2(some_url):
    print(some_url)
    redir="http://" + HOST + ":" + str(PORT) + "/"
    if(some_url[:3]=="JAz"):
        print(some_url)
        url = some_url
        decode = decode_url()
        dec = decode.decode(url)

        con = sqlite3.connect('urldatabase.db')
        print("successfully created database")

        cursorObj = con.cursor()

        cursorObj.execute('''SELECT url FROM urltable WHERE urlid=?''',(dec,))
        result = cursorObj.fetchone()
        print(result[0])
        con.commit()
        cursorObj.close()
        con.close()

        print("got successfully")
        print(result[0])
        redir=result[0]

    return redirect(redir)


@app.route('/urlshortner')
def url():
    return render_template("url_shorter.html")


@app.route('/u2')
def url_shorter():
    global message
    last = last_url()
    value_1 = last.lasturl()
    value_2=request.args.get("url_short")

    if(value_2 == ""):
        return redirect("/urlshortner")


    con = sqlite3.connect('urldatabase.db')
    print("successfully created database")
    cursorObj = con.cursor()

    entities=(value_1+1,value_2)
    cursorObj.execute('''INSERT INTO urltable(urlid, url) VALUES(?, ?)''', entities)
    message="successfully created"
    con.commit()
    cursorObj.close()
    con.close()

    encode=encode_url()
    enc=encode.encode()
    host="http://" + HOST + ":" + str(PORT) + "/"
    value_3=host+enc

    return render_template("url_shorter1.html",value_3=value_3)


if __name__ == "__main__":
    app.run(host=HOST,port=PORT,debug=True)
