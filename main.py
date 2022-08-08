from flask import Flask, redirect #匯入模組
import random
import linecache

app = Flask('app') #建立網站

def rT(path):
    count = len(open(path, 'r').readlines())  #獲取行數
    num = random.randint(1, count)  #隨機數字(1~獲取行數)
    return linecache.getline(path, num)[:-1]  #回傳隨機行裡的資料(網址)

@app.route('/')
@app.route('/<n>')
@app.route('/<n>/.jpg/')
def pic(n = 0):
    path = "n.txt" #資料
    web = rT(path) #隨機資料函數
    print(web)
    return redirect(web) #回傳使用者網址

@app.route('/rei/')
@app.route('/rei/<n>')
@app.route('/rei/<n>/.jpg/')
def pic_rei(n = 0):
    path = "rei.txt" #資料
    web = rT(path) #隨機資料函數
    print(web)
    return redirect(web) #回傳使用者網址

app.run(host='0.0.0.0', port=8080)