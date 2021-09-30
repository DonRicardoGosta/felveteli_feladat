from flask import Flask, session, request, redirect, url_for, render_template
import crypter

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/login', methods=['POST'])
def login():
    MSG = None
    if request.method == 'POST':
        if request.form['username'] != "" or request.form['password'] != "":
            if request.form['username'] in crypter.users and crypter.verify_password(request.form['password'],
                                                                                     crypter.users[
                                                                                         request.form['username']]):
                session['username'] = request.form['username']
                session['password'] = request.form['password']
                MSG = "7a55204fb9d7076b6d73b3bc5d8ed2849d86a26e"
                request.headers["x-api-key"] = MSG
                MSG = request.headers.get('x.api.key')
            else:
                MSG = "401 Unauthorized"
        else:
            MSG = "Please fill out all field"
        return render_template("login.html", errorMSG=MSG)
    return render_template("login.html")


@app.route('/data')
def data():
    if request.headers.get('x.api.key') != "401 Unauthorized" and request.headers.get('x.api.key') is not None:
        response_data = {
                        "id": 1,
                        "text": "Kacsa",
                        "year": 1964}

        return response_data
    else:
        return "401 Unauthorized"


def main():
    print("main")


if __name__ == '__main__':
    main()
