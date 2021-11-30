"""
MIT License

Copyright (c) 2021 B.Jothin kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: Jothin kumar (https://jothin-kumar.github.io)
Repository link: https://github.com/Jothin-kumar/login-form
"""
import flask
from os.path import exists

app = flask.Flask(__name__)
username_and_password_file = "username_and_passwords.txt"


@app.route('/authenticate')
def authenticate():
    given_username = flask.request.args.get('username')
    given_password = flask.request.args.get('password')
    username_and_passwords = []
    if exists(username_and_password_file):
        with open(username_and_password_file) as usernames_and_passwords:
            for line in usernames_and_passwords.readlines():
                if line != '\n':
                    username = line.split(' ')[0]
                    password = line.split(' ')
                    del password[0]
                    password = ''.join(password).replace('\n', '')
                    username_and_passwords.append({'username': username, 'password': password})
    for username_and_password in username_and_passwords:
        if username_and_password['username'] == given_username and username_and_password['password'] == given_password:
            return 'Authenticated'
    return 'Not Authenticated'


@app.route('/signup')
def signup():
    username = flask.request.args.get('username')
    password = flask.request.args.get('password')
    with open(username_and_password_file, 'a+') as username_and_passwords:
        username_and_passwords.write(username + ' ' + password + '\n')
    return 'Successful'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
