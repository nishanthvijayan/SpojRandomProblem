import os
from flask import Flask, jsonify
import urllib2
from bs4 import BeautifulSoup
import random

app = Flask(__name__)


def getData():
    
    randomNumOne = random.randint(1, 2900)
    page = urllib2.urlopen("http://www.spoj.com/problems/classical/sort=0,start="+str(randomNumOne))
    soup = BeautifulSoup(page,"html.parser")
    probrows = soup.findAll("tr")
    randomNumTwo = random.randint(1,50)
    probrow = probrows[randomNumTwo]
    ID =    str(probrow.select("td")[0].text.strip().encode("ascii","ignore"))
    CODE = str(probrow.select("td")[1].a["href"].strip().encode("ascii","ignore"))
    NAME = str(probrow.select("td")[1].text.strip().encode("ascii","ignore"))
    USERS = str(probrow.select("td")[3].text.strip().encode("ascii","ignore"))
    ACCURACY = str(probrow.select("td")[4].text.strip().encode("ascii","ignore"))
    problem = {"ID":ID,"Code":CODE,"Name":NAME,"Users":USERS,"Accuracy":ACCURACY}
    return problem


@app.route('/')
def index():

    problem = getData()
    resp = jsonify(RandomProblemCode=problem)
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)