from flask import Flask, render_template,flash,url_for
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jaideepreddych@gmail.com'
app.config['MAIL_PASSWORD'] = 'Shreeram007'
app.config['MAIL_DEFAULT_SENDER'] = 'jaideepreddych.gmail.com'
mail = Mail(app)
@app.route('/')
def index():
     return render_template('index.html')
@app.route('/send_email')
def send_email():
    try:
        msg = Message("Test Email", recipients=["jaideeproll7@gmail.com"])
        msg.body ="this is the body of the email"
        msg.html ="<b>this is the body of the email in html format"
        mail.send(msg)

        flash('email sent successfully!','success')
    except Exception as e:

        flash(f"an error occured:{e}",'danger')
    return redirect(url_for('index'))


if __name__=='__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
