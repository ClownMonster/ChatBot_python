from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.debug = True
app.static_folder = 'static'