from flask import Flask, request, redirect, render_template


app = Flask(__name__)

app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Signup</title>
        <style type="text/css">
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
        <h1>Signup</h1>
        """

page_footer = """
    </body>
</html>
"""

user_name_form = """
    <form action ="/username" method ="post"
        <label for="username"> Username </label>
            <input type="text" name="username" value="">
    </form>
    """

password_form = """
    <form action ="/" method ="post"
        <label for ="password"> Password</label>
            <input type="text" name="password" value ="">
        <label for ="verify password">Verify Password</label>
            <input type="text" name="verify password" value="">
    </form>
    """

email_form = """
    <form action ="/" method ="post"
        <label for ="email"> Email (optional)</label>
            <input type="text" name="email" value="">
    </form>
    """

submit_query = """
    <form>
        <input type="submit">
    </form>
    """

@app.route("/")
def index():
    content = page_header + user_name_form + password_form + email_form + submit_query + page_footer
    return content 

@app.route("/username", methods=['POST'])
def user_name():
    username = request.form['username']

    username_error_msg = "Not a valid username; must be 3-20 characters in length"
    
    if username == "" or len(username) < 3 or len(username) > 20:
        return username_error_msg
    else:
        return username



app.run()