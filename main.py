from flask import Flask, request, redirect, render_template
import os

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
        return render_template('inputs.html', username_error = username_error, email = email)

#Validating password
    if " " in password or len(password) < 3 or len(password) > 20:
        password_error = "Not a valid password; must be 3-20 characters in length with no spaces"
        password =""
        return render_template('inputs.html', username = username, 
        password_error = password_error, 
        email = email)
    
#Validating password verification
    if password != verify_password:
        verify_password_error = "Passwords do not match"
        verify_password = ""
        return render_template('inputs.html', username = username, 
        password_error = password_error, 
        verify_password_error = verify_password_error, 
        email = email)
    

#Validating email
    if not(email):
        pass
    else: 
        if email:
            count_1 = 0
            for char in email:
                if char == "@":
                    count_1 += 1

            if count_1 != 1:
                email_error = "Not a valid email:  make sure have only one '@' and one '.'"
                return render_template('inputs.html', username = username, password_error = password_error,
                verify_password_error = verify_password_error, email_error = email_error)

    
            count_2 = 0
            for char in email:
                if char == ".":
                    count_2 += 1

            if count_2 != 1:
                email_error = "Not a valid email:  make sure have only one '@' and one '.'"
                return render_template('inputs.html', username = username, password_error = password_error,
                verify_password_error = verify_password_error, email_error = email_error)
            
            if " " in email or len(email) < 3 or len(email) > 20:
                email_error = "Not a valid email:  make sure have only one '@' and one '.'"
                return render_template('inputs.html', username = username, password_error = password_error,
                verify_password_error = verify_password_error, email_error = email_error)
    
#If everything passes, then will redirect to 'Welcome' page, else:  errors will be displayed
    if not username_error and not password_error and not verify_password_error and not email_error:
        username = request.form['username']
        return render_template('welcome.html', username=username)

    else:
        return render_template('inputs.html', username_error = username_error, 
        password_error = password_error, 
        verify_password_error = verify_password_error,
        email_error = email_error)
 

app.run()