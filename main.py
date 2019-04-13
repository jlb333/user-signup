from flask import Flask, request, redirect, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('inputs.html')


@app.route("/validation", methods=['POST'])
def validate_inputs():
#Get info out of inputs 
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

#Set up error strings to capture any error statements to be used globally in this function
    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

#Validating username
    if " " in username or len(username) < 3 or len(username) > 20:
        username_error = "Not a valid username; must be 3-20 characters in length with no spaces"
        
#Validating password
    if " " in password or len(password) < 3 or len(password) > 20:
        password_error = "Not a valid password; must be 3-20 characters in length with no spaces"
        password =""

#Validating password verification
    if password != verify_password:
        verify_password_error = "Passwords do not match"
        verify_password = ""

#Validating email
    if len(email) < 3 or len(email) > 20 and "@" not in email and "." not in email:
        email_error = "Not a valid email:  make sure have only one '@' and one '.'"

#If everything passes, then will redirect to 'Welcome' page
    if not username_error and not password_error and not verify_password_error and not email_error:
        username = request.form['username']
        return render_template('welcome.html', username=username)
#If there are errors, will be displayed    
    else:
        return render_template('inputs.html', username_error = username_error, 
        password_error = password_error, verify_password_error= verify_password_error,
        email_error = email_error)
 

app.run()