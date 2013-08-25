#!/bin/env python3
# -*- coding: utf-8 -*-

"""
   app
   ~~~

   Data interface for ToucheAide
"""

from flask import Flask, Blueprint, request, url_for, json, Response, abort
from convert import policy_l, getstuff

activities, activity_index = {}, {}

for lang in ('en', 'fr'):
    activities[lang], activity_index[lang] = getstuff(lang)

app = Flask(__name__, static_folder='../frontend/static')


api = Blueprint('api', 'api')


@api.route('/')
def api_index():
    lang = request.args.get('lang', 'en')
    index = {
        {'en': "resources", 'fr': "resources"}[lang]: [
            {
                "name": {'en': "policies", 'fr': "politiques"}[lang],
                "uri": url_for('.policies_index'),
            },
            {
                "name": {'en': "activities", 'fr': "activites"}[lang],
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
    return Response(json.dumps(activity_index[lang]), mimetype='application/json')


@api.route('/activities/<string:iati_code>')
def activity(iati_code):
    lang = request.args.get('lang', 'en')
    activity = activities[lang].get(iati_code) or abort(404)
    return Response(json.dumps(activity), mimetype='application/json')


app.register_blueprint(api, url_prefix='/api')



if __name__ == '__main__':
    @app.route('/')
    def main():
        return open('../frontend/index.html').read()

    app.run(debug=True)
