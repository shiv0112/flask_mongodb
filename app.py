from flask import Flask, request,render_template
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["db_shiv"]
mycol = mydb["students"]

app=Flask(__name__)

@app.route('/')
def myform():
    return render_template('basic.html')

@app.route('/data',methods=['POST'])
def mydata():
    if request.method=='POST':
       if request.form['submit'] == 'submit_a':
          data=request.form.get('x')
          data1=request.form.get('y')
          data2=request.form.get('z')
       
          db=[
            {
              "name": data,
              "class": data1,
              "section": data2
             }
            ]
          myclient['db_shiv']['students'].insert(db)
       
       elif request.form['submit'] == 'submit_b':
           return(view())

    return (myform())

@app.route('/view')
def view():
    s=""
    for i in mycol.find():
        s=s+str(i)+"<br/>"
    return(s)

if __name__ == '__main__':
    app.debug = True
    app.run(port=4595)

