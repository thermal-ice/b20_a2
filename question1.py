#Question 1

from flask import Flask

app = Flask(__name__)

@app.route('/<name>', methods=['GET'])
def generateResponse(name: str):
    parsedName = ""

    if not name.isalpha():
        parsedName = ''.join(filter(str.isalpha,name))

    else:
        if name.islower():
            parsedName = name.upper()
        elif name.isupper():
            parsedName = name.lower()
        else:
            parsedName = name

    return f"Welcome, {parsedName}, to my CSCB20 website!"