#!python3
from flask import Flask, render_template, request, make_response, json
#import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/author',methods=['GET'])
def author():

    vuri1 = "https://jsonplaceholder.typicode.com/users"
    vuri2 = "https://jsonplaceholder.typicode.com/posts"
#    try:
#        vResponse1 = requests.get(vuri1)
#    except requests.ConnectionError:
#       return "Connection Error"

#    vauthor = json.load(vResponse1.data)

    #vposts = json.load(open('https://jsonplaceholder.typicode.com/posts.json'))
 #   vusers = {vauth['id']:{'name':vauth['name'],'count':0} for vauth in vauthor}
#    for vpost in vposts:
#        vusers[vpost['userId']]['count']+=1
#    return render_template('authors.html', users=vusers)
    return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        vuser = request.form['NameV']
        vage = request.form['AgeV']

    vresp = make_response(render_template('getcookies.html'))
    vresp.set_cookie('User', vuser )
    vresp.set_cookie('Age', vage)
    return vresp

@app.route('/getcookies')
def getcookies():
   vname = request.cookies.get('User')
   vage = request.cookies.get('Age')
   return '<h1>Name: '+vname+'. and Age:'+vage+'.</h1>'

@app.route('/html')
def html():
    return(render_template('htmlfile.html'))

@app.route('/input')
def inputdata():
    return(render_template('inputdata.html'))

@app.route('/displaydata', methods = ['POST'])
def displaydata():
   if request.method == 'POST':
       vdata = request.form['Tb']
       vselections = request.form['selection']
       if vselections == 'html':
        return (render_template('display.html',name = vdata))
       elif vselections == 'console':
        print(vdata)
   return 'Output is on server terminal'

# Handling all other request and robots.txt request
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run()