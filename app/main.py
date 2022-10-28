import string
from urllib import request, response
from flask import Flask, request
from flask_restful import Resource, Api
import csv

file = open('data.csv')

csvreader = csv.reader(file)
cities = []
latGlobal = []
lngGlobal = []
allin = []
for city in csvreader:
    cities.append(city[0])
    latGlobal.append(city[1])
    lngGlobal.append(city[2])
    allin.append([float(city[1]), float(city[2])])



app = Flask(__name__)
api = Api(app)
@app.route('/all', methods=['GET'])
def all():
    return (allin)

@app.route('/kota', methods=['GET'])
def kota():
    name = request.args.get("name") or ""
    matches = []
 
    for match in range(516):
        if name.lower() in cities[match].lower():
            matches.append(cities[match])

    return list(matches)

@app.route('/bellman', methods=['GET'])
def bellman():
    asal = request.args.get("asal") or ""
    tujuan = request.args.get("tujuan") or ""
    full = []
    file = open('Bellman/{}.csv'.format(asal))
    readercsv = csv.reader(file)
    i=0
    for cek in readercsv:
        i+=1
        if cek[0] == tujuan:
            li = list(cek[2].split(", "))
            a = li[0].replace('[','')
            li[0] = a
            a = li[len(li)-1].replace(']','')
            li[len(li)-1] = a
            li.append(i-2)
            for i in li:
                full.append([float(latGlobal[int(i)]), float(lngGlobal[int(i)])])
            break
    return list(full)

@app.route('/djikstraa', methods=['GET'])
def djikstraa():
    asal = request.args.get("asal") or ""
    tujuan = request.args.get("tujuan") or ""
    full = []
    file = open('Djikstraa/{}.csv'.format(asal))
    readercsv = csv.reader(file)
    i=0
    for cek in readercsv:
        i+=1
        if cek[0] == tujuan:
            li = list(cek[2].split(", "))
            a = li[0].replace('[','')
            li[0] = a
            a = li[len(li)-1].replace(']','')
            li[len(li)-1] = a
            li.append(i-2)
            for i in li:
                full.append([float(latGlobal[int(i)]), float(lngGlobal[int(i)])])
            break
    return list(full)

# if __name__ == "__main__":
#     app.run(debug=True)