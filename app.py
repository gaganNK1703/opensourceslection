from flask import Flask

app = Flask(__name__)

try:
    from controller import *
except Exception as e:
    print(e)

