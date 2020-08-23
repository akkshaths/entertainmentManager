from flask import Flask, session
from flask import render_template
from flask import request, redirect

app = Flask(__name__)



@app.route('/')
def hello():
    return render_template("yoursubscriptions.html")

@app.route('/login')
def login():
    return render_template('signup.html')
    

@app.route('/price')
def findPrice():
    listOfSubTV = request.form['tv']
    forHtml = ''
    for i in listOfSubTV:
        forHtml += '''
        <input type="text" name="''' + i + '''" value="1">How much do you pay for ''' + i + ''' per month?</input>
        \n <input type="text" name="''' + i + '''" value="1">How many hours have you used this in the past week</input> \n'''

    return render_template('pay&hours.html', userInput = forHtml)

    
if __name__ == '__main__':
    app.run()