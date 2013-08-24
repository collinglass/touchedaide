#!/bin/env python2
# -*- coding: utf-8 -*-

"""
   app
   ~~~

   Data interface for ToucheAide
"""

from flask import Flask

app = Flask(__name__)

@app.route('/api/')
def api_root():
    return "hellooooooo"

if __name__ == '__main__':
    app.run(debug=True)
