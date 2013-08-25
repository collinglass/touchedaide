#!/bin/env python3
# -*- coding: utf-8 -*-

"""
   app
   ~~~

   Data interface for ToucheAide
"""

from flask import Flask, Blueprint, request, url_for, json, Response, abort
from convert import policy_l, getstuff

activities, activity_index = getstuff()

app = Flask(__name__)


api = Blueprint('api', 'api')


@api.route('/')
def api_index():
    index = {
        "resources": [
            {
                "name": "policies",
                "uri": url_for('.policies_index'),
            },
            {
                "name": "activities",
                "uri": url_for('.activities_index'),
            }
        ]
    }
    return Response(json.dumps(index), mimetype='application/json')


@api.route('/policies/')
def policies_index():
    lang = request.args.get('lang', 'en')
    return Response(json.dumps(policy_l(lang)), mimetype='application/json')


@api.route('/activities/')
def activities_index():
    lang = request.args.get('lang', 'en')
    return Response(json.dumps(activity_index), mimetype='application/json')


@api.route('/activities/<string:iati_code>')
def activity(iati_code):
    lang = request.args.get('lang', 'en')
    activity = activities.get(iati_code) or abort(404)
    return Response(json.dumps(activity), mimetype='application/json')


# fake_api = Blueprint('api', 'api')

# @fake_api.route('/')
# def fake_index():
#     return 'hellooooooooo'


# @fake_api.route('/activities/')
# def fake_activities_index():
#     with open('resources/samples.json') as fake_file:
#         return Response(fake_file.read(), mimetype='application/json')


# @fake_api.route('/activities/<string:iati_code>')
# def fake_activity(iati_code):
#     with open('resources/{}.json'.format(iati_code)) as fake_file:
#         return Response(fake_file.read(), mimetype='application/json')



app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)
