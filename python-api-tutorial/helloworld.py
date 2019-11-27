from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World'
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

def otherhello():
    return 'Other Hello';

@app.route('/hello/<name>')
def helloscore(name):
    return 'Hello : ' + name;

@app.route('/hello/score/<int:score>')
def hello(score):
    return render_template('hello.html', marks = score)


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

@app.route('/kuyadict/')
def result():
    dict = {'phy':50,'che':60,'maths':70}
    return render_template('kuyadict.html',result=dict)

@app.route('/redirect')
def redirected():
    return redirect(url_for('hellox',param="jake"))

@app.route('/secondary')
def secondary():
    return "secondary - ";

@app.route('/third/<student>')
def third(student):
    return "third - " +student;

@app.route('/test/<varx>')
def testing(varx):
    if varx == 'jake' :
        return redirect(url_for('secondary'));
    else:
        return redirect(url_for('third',student=varx))

@app.route('/success/<name>/<age>')
def success(name,age):
   return 'welcome %s' + name + " - " +age;



@app.route('/login/',methods=['POST','GET'])
def login():
    if(request.method =='POST'):
        user = request.form['nm'];
        agex = request.form['age'];
        return redirect(url_for('success',name=user,age=agex))
    else:
        user = request.get('nm');
        agex = request.get('age')
        return redirect(url_for('success',name=user,age=agex))



app.add_url_rule('/otherhello','otherhello',otherhello)
app.add_url_rule('/hellox/<param>','hellox',hellox)
if __name__ == '__main__':
    #app.run();
    app.run(debug=True);






