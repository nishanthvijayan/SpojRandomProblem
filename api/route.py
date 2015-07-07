import os
from flask import Flask, jsonify
import urllib2
from bs4 import BeautifulSoup
import random

app = Flask(__name__)


def get_data():
    
    random_num_one = random.randint(1, 2900)
    page = urllib2.urlopen("http://www.spoj.com/problems/classical/sort=0,start="+str(random_num_one))
    soup = BeautifulSoup(page,"html.parser")
    
    probrows = soup.findAll("tr")
    random_num_two = random.randint(1,50)
    probrow = probrows[random_num_two]
    td = probrow.select("td")
    
    id =        str(td[0].text.strip().encode("ascii","ignore"))
    code =      str(td[1].a["href"].strip().encode("ascii","ignore"))
    name =      str(td[1].text.strip().encode("ascii","ignore"))
    users =     str(td[3].text.strip().encode("ascii","ignore"))
    accuracy =  str(td[4].text.strip().encode("ascii","ignore"))

    problem = {"ID":id,"Code":code,"Name":name,"Users":users,"Accuracy":accuracy}
    return problem


@app.route('/')
def index():

    problem = get_data()
    resp = jsonify(RandomProblemCode=problem)
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)