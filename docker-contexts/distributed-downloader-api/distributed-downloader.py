"""API for driving a distributed download system.

Manager/Monitor - webpage with file list etc
  - start a download by specifying url list? and dest bucket
  - can be specified to bring up workers
  - schedule downloads among workers
  - check status of workers
Download worker - server that does:
  - /download (file list, dest bucket) -> status id
  - /status (status id) -> status
"""
import requests

#from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

STATUS = {
    'job_list': [],
}


@app.route('/')
def index():
    """Base index."""
    return "Hello, World!"


@app.get('/downloader/status')
def status():
    """Return status."""
    return jsonify(STATUS)

@app.get('/hi/<int>')
def hi_func(int x):
    return 'hi there!' + str(x)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
