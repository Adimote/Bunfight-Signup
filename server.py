from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def sign_up():
    return render_template('sign_up.html')


@app.route('/signed_up', methods=['POST'])
def signed_up():
    with open('signups.txt', 'a') as f:
        name = request.form['name']
        email = request.form['email']
        f.write("{},{}\n".format(name, email))
    return "", 201

if __name__ == '__main__':
    app.debug = True
    app.run()
