from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World'

def otherhello():
    return 'Other Hello';

@app.route('/hello/<name>')
def hello(name):
    return 'Hello : ' + name;

def hellox(param):
    return 'Hellox :' + param

@app.route('/hello/rev/<float:rev>')
def revisions(rev):
    return 'Revisions %f'  % rev

@app.route('/hello/rev/<float:rev>/<int:page>')
def revpages(rev,page):
    returnee = 'Hello %f revision'  %rev;
    returnee = returnee + " for page %d " %page
    return returnee;

@app.route('/redirect')
def redirected():
    return redirect(url_for('hellox',param="jake"))

app.add_url_rule('/otherhello','otherhello',otherhello)
app.add_url_rule('/hellox/<param>','hellox',hellox)
if __name__ == '__main__':
    #app.run();
    app.run(debug=True);



#https://www.tutorialspoint.com/flask/flask_url_building.htm


