from flask import Flask, render_template, request, redirect
import tool
app = Flask(__name__)

@app.route('/')
def main_web():
    return render_template('main1.html', t_time=tool.time_tool())
@app.route('/href')
def href_web():
    return render_template('href.html')
@app.route('/class_schedule_card')
def class_schedule_card_web():
    return render_template('href2.html')
@app.route('/questionnaire')
def questionnaire():
    return render_template('href3.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login1')
def login1():
    return render_template('login1.html')
@app.route('/form1', methods=['POST'])
def form1():
    p = request.form['p']
    m = request.form['m']
    print(type(m))
    if tool.form1(p, m, 'r'):
        print(123)
        return render_template('login-href.html', t_name=p)
    else:
        return render_template('login.html', t_err='用户名或密码错误')
@app.route('/form2', methods=['POST'])
def form2():
    p = request.form['p']
    m = request.form['m']
    tool.form1(p, m, 'w')
    return render_template('login.html', t_err='用户名或密码错误')
@app.route('/form3', methods=['POST'])
def form3():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    tel = request.form['tel']
    tool.form2(name, age, gender, tel, 'w')
    return render_template('NotFound.html')
@app.route('/lhnp1')
def lhnp1():
    return render_template('lhNP.html')
@app.route('/lhnp2')
def lhnp2():
    request.form['']
@app.route('/ping')
def ping():
    return render_template('ping.html', t_ping=tool.ping())
@app.route('/ping_us', methods=['POST'])
def ping_us():
    tool.ping1({'content':request.form['ping-us']})
    return render_template('ping.html', t_ping=tool.ping())
if __name__ == '__main__':
    app.run(port=5071)