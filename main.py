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
    template = jinja_env.get_template('inputs.html')
    return template.render()


@app.route("/validation", methods=['POST'])
def validate_username():
    username = request.form['username']

    username_error_msg = "Not a valid username; must be 3-20 characters in length"
    
    template = jinja_env.get_template('inputs.html')

    for char in username:
        if char in username == " ":
            return template.render(username_error_msg= username_error_msg) 

    if len(username) < 3 or len(username) > 20:
        username = ""
        return template.render(username_error_msg= username_error_msg)
    else:
        return template.render(username = username)



app.run()