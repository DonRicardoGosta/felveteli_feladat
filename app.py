from flask import Flask, session, request, redirect, url_for, render_template, jsonify
import crypter

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/login', methods=['POST', 'GET'])
def login():
    response = None
    if request.method == 'POST':
        if request.form['username'] != "" or request.form['password'] != "":
            if request.form['username'] in crypter.users and crypter.verify_password(request.form['password'],
                                                                                     crypter.users[
                                                                                         request.form['username']]):
                # session['username'] = request.form['username']
                # session['password'] = request.form['password']
                return_token = {"token": "7a55204fb9d7076b6d73b3bc5d8ed2849d86a26e"}
                return redirect("/data/x-api-key:7a55204fb9d7076b6d73b3bc5d8ed2849d86a26e")
            else:
                response = "401 Unauthorized"
        else:
            response = "401 Unauthorized, Please fill out all field"
    return render_template("login.html", responseMSG=response)


@app.route('/data/x-api-key:<api_key>')
def data(api_key):
    if api_key == "7a55204fb9d7076b6d73b3bc5d8ed2849d86a26e":
        response_data = {"id": 1, "name": "Dani", "age": 20}, {"id": 2, "name": "Jenő", "age": 21}, {"id": 3, "name": "Peti", "age": 22}
        return render_template("data.html", resp_data = response_data)
    return "401 Unauthorized"


def main():
    print("main")


if __name__ == '__main__':
    app.debug = True
    app.run()
