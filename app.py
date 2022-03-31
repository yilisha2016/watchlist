from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/index')
@app.route('/home')
def hello(): 
   return u'欢迎来到我的watchlist!'
@app.route('/test')
def test_url_for():
   print(url_for('hello'))
   return 'Test page'
