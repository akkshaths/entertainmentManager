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
    

@app.route('/price', methods = ['POST'])
def findPrice():
    listOfSubTV = request.form.getlist('tv')
    forHtml = ''
    for i in listOfSubTV:
        forHtml += '''
        <input type="text" name="''' + i.tv + '''" value="1">How much do you pay for ''' + i.tv + ''' per month?</input>
        \n <input type="text" name="''' + i.tv + '''" value="1">How many hours have you used this in the past week</input> \n'''

    return render_template('pay&hours.html', userInput = forHtml)

    
if __name__ == '__main__':
    app.run()