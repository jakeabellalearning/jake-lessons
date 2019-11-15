from flask import Flask
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


app.add_url_rule('/otherhello','otherhello',otherhello)
app.add_url_rule('/hellox/<param>','hellox',hellox)
if __name__ == '__main__':
    #app.run();
    app.run(debug=True);

