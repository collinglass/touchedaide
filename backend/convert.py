#!/bin/env python2
# -*- coding: utf-8 -*-

"""
   convert
   ~~~~~~~

   Convert IATI xml to python data structure.
"""

DFATD_IATI = 'resources/dfatd-activities.xml'
XMLNS = '{http://www.w3.org/XML/1998/namespace}'

from lxml import etree

policies = [
    {'code': 1, 'name': {'en': 'Gender Equality',
                         'fr': 'Egalité des sexes'}},
    {'code': 2, 'name': {'en': 'Aid to Environment',
                         'fr': "Aide à l'environnement"}},
    {'code': 3, 'name': {'en': 'Good Governance',
                         'fr': 'Bonne Gouvernance'}},
    {'code': 4, 'name': {'en': 'Trade Development',
                         'fr': 'Developpement de Commerce'}},
    {'code': 5, 'name': {'en': 'Bio-Diversity',
                         'fr': 'Biodiversité'}},
    {'code': 6, 'name': {'en': 'Climate Change',
                         'fr': 'Changements Climatiques'}},
    {'code': 8, 'name': {'en': 'Anti Desertification',
                         'fr': 'Contre la Désertification'}},
]

tree = etree.parse(DFATD_IATI)
root = tree.getroot()

activities = []


def attrify(els, attr, vattr=None, verify=True):
    ified = {}
    for el in els:
        k = el.attrib[attr]
        if verify:
            assert k not in ified, 'integrittyyyyyyyyyyyy'
        v = el.attrib[vattr] if vattr else el.text
        ified[k] = v
    return ified


def polify(els):
    ified = []
    for el in els:
        fied = dict(code=el.get('code'), significance=el.get('significance'))
        n = [p['name'] for p in policies if str(p['code']) == fied['code']]
        fied.update(name=n[0] if n else None)
        ified.append(fied)
    return ified


def countrify(els):
    ished = attrify(els, 'percentage', 'code', verify=False)
    if ished:
        return ished.get(max(ished))


def getstuff():
    stuff = {}
    listuff = []
    for activity in (thing for n, thing in enumerate(tree.getroot())):
        a_id = activity.find('iati-identifier').text
        title = attrify(activity.findall('title'), '{}lang'.format(XMLNS))
        date = attrify(activity.findall('activity-date'), 'type', 'iso-date')
        policy = polify(activity.findall('policy-marker'))
        country = countrify(activity.findall('recipient-country'))
        organizations = attrify(activity.findall('participating-org[@role="Implementing"]'), '{}lang'.format(XMLNS))
        description = attrify(activity.findall('description[@type="1"]'), '{}lang'.format(XMLNS))
        # result = attrify(activity.findall('result[@type="2"]'), '{}lang'.format(XMLNS))
        stuff[a_id] = dict(
            id=a_id,
            title=title['en'],
            start=date.get('start-expected', date.get('start-actual')),
            end=date.get('end-expected', date.get('end-actual')),
            policy=[{'code': p['code'], 'name': p['name']['en'] if p['name'] else None} for p in policy],
            country=country,
            organizations = organizations['en'],
            description=description['en']
        )
        listuff.append(dict(
            uri='/api/',
            start=stuff[a_id]['start'],
            end=stuff[a_id]['end'],
            policy=[p['name'] for p in stuff[a_id]['policy']],
            country=stuff[a_id]['country'],
            organizations=stuff[a_id]['organizations']
        ))
    return stuff, listuff

print getstuff()
    
