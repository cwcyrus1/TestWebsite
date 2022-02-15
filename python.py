from flask import Flask, render_template, request, session, redirect
app = Flask('app')
app.secret_key = '12345678987654321'

@app.route("/")

def index():
    return render_template("index.html")
    
app.run(host = '0.0.0.0', port = 8080)