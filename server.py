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
from hashlib import sha256
from os.path import exists

app = flask.Flask(__name__)
username_and_password_hashes_file = "username_and_passwords.txt"


@app.route('/')
def index():
    return flask.send_file('index.html')


@app.route('/scripts.js')
def scripts():
    return flask.send_file('scripts.js')


@app.route('/authenticate')
def authenticate():
    given_username = flask.request.args.get('username')
    given_password_hash = sha256(flask.request.args.get('password').encode()).hexdigest()
    username_and_passwords_hash = []
    if exists(username_and_password_hashes_file):
        with open(username_and_password_hashes_file) as usernames_and_password_hashes:
            for line in usernames_and_password_hashes.readlines():
                if line != '\n':
                    username = line.split(' ')[0]
                    password_hash = line.split(' ')[1]
                    username_and_passwords_hash.append({'username': username, 'password_hash': password_hash})
    for username_and_password_hash in username_and_passwords_hash:
        if username_and_password_hash['username'] == given_username and username_and_password_hash['password_hash'] == given_password_hash:
            return 'Authenticated'
    return 'Not Authenticated'


@app.route('/signup')
def signup():
    username = flask.request.args.get('username')
    password_hash = sha256(flask.request.args.get('password').encode()).hexdigest()
    username_exists = False
    if exists(username_and_password_hashes_file):
        with open(username_and_password_hashes_file) as usernames_and_passwords:
            for line in usernames_and_passwords.readlines():
                if line != '\n':
                    if line.split(' ')[0] == username:
                        username_exists = True
                        break
    if username_exists:
        return 'Username already exists'
    else:
        with open(username_and_password_hashes_file, 'a+') as username_and_password_hashes:
            username_and_password_hashes.write(username + ' ' + password_hash + '\n')
        return 'Successful'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
