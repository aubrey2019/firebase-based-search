import pymysql
import json
import sys
import requests


def main():
    dbname = sys.argv[1]
    node = sys.argv[2]

    url = 'https://inf551project-8d971.firebaseio.com/' + node

    #con = pymysql.connect('localhost', 'root','zxw19951212', dbname)

    con = pymysql.connect("localhost","root","0808",dbname)

    with con:
        cur = con.cursor()
        cur.execute("show tables")

        tables = cur.fetchall()

        table_list = []

        for i in range(len(tables)):
            table_list.append(tables[i][0])

        # iterate each table
        for table in table_list:
            print(table)
            cur.execute("SELECT * FROM " + table)

            rv = cur.fetchall()
            json_data = []
            

            headers = [x[0] for x in cur.description]

            for result in rv:
                json_data.append(dict(zip(headers, result)))

            #print(json_data)
            
            fw = open(table+'.json', 'w', encoding='latin-1')

            json_res = json.dump(json_data,fw ,indent=4,default=str,sort_keys=True)
            fw.close()

            # table_url = url + '/' + table + '.json'
            # print(table_url)

            with open(table+".json", 'r') as f:
                    j =json.loads(f.read())
                    j =json.dumps(j)
            r=requests.put('https://inf551project-8d971.firebaseio.com/'+node+'/'+table+'.json',j)
            print(r)


            # response = requests.put(table_url, json_res)
            # print(response)


if __name__ == '__main__':
    main()