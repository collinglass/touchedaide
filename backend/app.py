#!/bin/env python2
# -*- coding: utf-8 -*-

"""
   app
   ~~~

   Data interface for ToucheAide
"""

from flask import Flask, Blueprint, json, Response

app = Flask(__name__)





fake_api = Blueprint('api', 'api')

@fake_api.route('/')
def fake_index():
    return 'hellooooooooo'


@fake_api.route('/activities/')
def fake_activities_index():
    with open('resources/samples.json') as fake_file:
        return Response(fake_file.read(), mimetype='application/json')


@fake_api.route('/activities/<string:iati_code>')
def fake_activity(iati_code):
    with open('resources/{}.json'.format(iati_code)) as fake_file:
        return Response(fake_file.read(), mimetype='application/json')



app.register_blueprint(fake_api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)
