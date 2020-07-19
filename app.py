from flask import Flask, redirect, url_for, render_template, request, session
import requests
import json
import re
import operator



app = Flask(__name__)
app.secret_key = "eddie"

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        dname = request.form["selectbar"]
        keyword = request.form["searchbar"]

        session["database"] = dname

        return redirect(url_for("search", dname= dname, key = keyword))
    else:
        return render_template("index.html")

@app.route("/search/<dname>/<key>")
def search(dname, key):

    data, count, table_list = getData(dname, key)

    return render_template("search.html", data= data, database = dname, count = count, table_list = table_list)

@app.route("/mysearch/<key>")
def mysearch(key):
    dname = session["database"]

    data, count, table_list = getData(dname, key)

    return render_template("search.html", data= data, database = dname, count = count, table_list = table_list)




@app.route("/explore/<table>/<key>")
def explore(table, key):
    dname = session["database"]

    keys_dict = {'GameId': 'Game',
     'TeamId': 'Team',
     'PlayerId': 'Player',
     'Team1Id': 'Team',
     'Team2Id': 'Team',
     'p_id': 'person',
     'p_id_dummy': 'person',
     'course_id': 'course',
     'ID': 'city',
     'Code': 'country',
     'CountryCode': 'countrylanguage'}

    table = keys_dict[table]

    data = exploreData(dname, key)

    table_list = [table]
    filtered_data = [[]]
    count = 0

    for tmp in data:
        for item in tmp:
            if item[0] == table:
                filtered_data[0].append(item[1])
                count += 1


    print(filtered_data)
    return render_template("search.html", data= filtered_data, count = count, table_list = table_list)


def getData(dname, key):
    word_list = split(key)

    dic = {}
    for word in word_list:
        r = find(dname, word)

        if r == None:
            return []

        for e in r:

            if dic.get(e['TABLE']) == None:
                dic[e['TABLE']] = [e['data']]
            else:
                dic[e['TABLE']].append(e['data'])

    myres = []
    count = 0
    table_list = []

    for item in dic.values():
        tmp = []
        res = []
        for d in item:
            tmp.append(str(d))
        tmp = list_sort(tmp)

        for i in tmp:
            res.append(eval(i))
            count += 1
        myres.append(res)

    for key in dic.keys():
        table_list.append(key)

    print(table_list)

    return myres, count, table_list


def exploreData(dname, key):
    word_list = split(key)

    dic = {}
    for word in word_list:
        r = find(dname, word)

        for e in r:

            if dic.get(e['TABLE']) == None:
                dic[e['TABLE']] = [e['data']]
            else:
                dic[e['TABLE']].append(e['data'])

    # (table, data)
    myres = []
    for (key, item) in dic.items():
        tmp = []
        res = []
        for d in item:
            tmp.append(str(d))
        for i in tmp:
            res.append((key, eval(i)))

        myres.append(res)

    return myres



def find(db,word):
    r=requests.get('https://inf551project-8d971.firebaseio.com/'+db+'/index/'+word+'/.json')
    result=json.loads(r.text)
    return result


def split(words):
    word_list = re.split(r'[-,/,\s]', words)
    word_list_1 = []
    for word in word_list:
        word = word.lower()
        word = re.sub(r'[^a-z0-9]', '', word)
        word_list_1.append(word)
    return word_list_1


def list_sort(L):
    set_L=set(L)
    count_set={}
    for i in set_L:
        count_set[i]=L.count(i)
    sorted_list= sorted(count_set.items(), key=operator.itemgetter(1))
    result=[]
    for item in sorted_list[::-1]:
        result.append(item[0])
    return result


if __name__ == "__main__":
    app.run(debug=True)