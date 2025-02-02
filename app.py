from flask import Flask

app=Flask(__name__)

@app.route('/')

def webout():

 return '<h1>Achham is amazing distric</h1>'
 return '<h2> rinku<h2>'

app.run(host='0.0.0.0',port=7000)
