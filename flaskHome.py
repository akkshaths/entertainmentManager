from flask import Flask, session
from flask import render_template
from flask import request, redirect
from flask import session
from users import newUser

app = Flask(__name__)


app.secret_key = 'Bob'
@app.route('/')
def hello():
    session['usernamePWDList'] = [["user123@gmail.com", "ilovehackathons"], ["akkie567", "notebook!"], ["akul89", "waterbottle"]]
    return render_template("homepage.html")


@app.route('/signup')
def signup():
    return render_template('signup.html', existingInfo = "")

@app.route('/login')
def login():
    return render_template('login.html', wrongInfo = "")

@app.route('/suggestions')
def suggestions():
    #this is where you will get the lsit of recommendations
    suggestions = ''
    var_name = ''
    for i in var_name:
        sugestions += '''
        <ul>
            <li>''' + i + '''</li>
        </ul>
        '''
    return render_template('suggestions.html', suggestions = suggestions)

@app.route('/yoursubscriptions')    
def subscriptions():
    return render_template('yoursubscriptions.html')

@app.route('/price', methods = ['POST'])
def findPrice():
    listOfSubTV = request.form.getlist('tv')
    forHtml = ''
    for i in listOfSubTV:
        #forHtml += i
        forHtml += '''
        <br><input type="text" name="''' + i + '''" value="0">          How much do you pay for ''' + i + ''' per month?</input>
        <br><input type="text" name="''' + i + '''" value="0">          How many hours have you used this in the past week?</input> <br/> '''
        
    session['choices'] = listOfSubTV
    return render_template('pay&hours.html', userInput = forHtml)

@app.route('/temp', methods = ['POST'])
def checkEmail():
    username = request.form.get('email')
    
    password = request.form.get('pwd')
    for i in session['usernamePWDList']:
        if (username == i[0]) and (password == i[1]):
            session['username'] = username
            session['password'] = password
            return redirect('/profile')

        
    return render_template('login.html', wrongInfo = 'Invalid username or password')

    

@app.route('/temp2', methods = ['POST'])
def addEmail():
    username = request.form.get('email')
    password = request.form.get('pwd')
    for i in session['usernamePWDList']:
        if username == i[0] or password == i[1]:
            return render_template('signup.html', existingInfo = 'Existing username or password')
    x = newUser(username, password)
    

    session['username'] = username
    session['password'] = password
    session['usernamePWDList'].append([username, password])
    
    return render_template('yoursubscriptions.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run()