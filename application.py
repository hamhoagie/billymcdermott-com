import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return redirect("https://billy.xxx", code=302)

if __name__=="__main__":
	app.run()