import time
import os
import logging
from flask import Flask, jsonify, request
import subprocess as sp

app = Flask(__name__)

hostName = sp.getoutput("hostname")

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

@app.route("/")
def root():
  return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
