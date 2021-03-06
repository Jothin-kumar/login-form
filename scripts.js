/*
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
*/
function httpGet(url){  // Source: https://stackoverflow.com/a/4033310/15923012
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false );
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function authenticate(username, password){
    var response = httpGet("/authenticate?username=" + username + "&password=" + password);
    if (response == "Authenticated"){
        return true;
    }
    else if (response == "Not Authenticated"){
        return false;
    }
}

function signup(username, password){
    var response = httpGet("/signup?username=" + username + "&password=" + password);
    if (response == "Successful"){
        return true;
    }
    else if (response == "Username already exists"){
        return false;
    }
}
