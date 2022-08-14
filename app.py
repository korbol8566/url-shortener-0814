from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import hashlib
import json
# import validators

app = Flask(__name__)

def short_url(longURL):
    # if validators.url(longURL):
        # return (hex(binascii.crc32(longURL.encode('utf8')))[:7])
    return (hashlib.md5(longURL.encode('utf-8')).hexdigest())[:4]
    # else:
    #     print("No URL has been passed")

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/', methods = ['POST', 'GET'])
def shorten():

    if request.method == 'POST':
        longURL = json.dumps(request.get_json())

        # custom = request.get_json()
        shortURL = short_url(longURL[0])

        # longURL = request.form['long']
        # custom = request.form['custom']

        # if custom == "":
        #     shortURL = short_url(longURL)
        # else:
        #     shortURL = custom

        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT shortURL FROM urls WHERE shortURL = (?)", ((shortURL,)) )

            check_fetch = cur.fetchone()

            if (check_fetch is None):
                cur.execute("INSERT INTO urls (longURL, shortURL) VALUES (?, ?)", (longURL, shortURL) )
                con.commit()
            #     msgBody = "Here's your URL: "
            #     msg = shortURL
                return jsonify(shortURL)

            else:
                return {"message": "Already in the DB"}
                # msgBody = "Already in the DB"
                # #msg = str(check_fetch)[2:6]
                # msg = ""


@app.route('/<shortURL>', methods = ['POST', 'GET'])
def reroute(shortURL):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT longURL FROM urls WHERE shortURL = (?)", ((shortURL,)) )

    try:
        new_url = cur.fetchone()[0]
        return jsonify(new_url)
        # return redirect(new_url)

    except:
        return {"message": "Failed to fetch"}
        # return render_template('404.html'), 404

if __name__ == '__main__':
   app.run(debug = True)