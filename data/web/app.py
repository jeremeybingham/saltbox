import os
import time
import logging
import sys
import json
import re
import pyramco
from datetime import datetime
from delorean import Delorean
from flask import Flask, render_template, request, jsonify, redirect, url_for, Response, session, abort

# local module imports
import api_explorer_functions

# instantiate flask app
app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']

# start logger
logging.basicConfig(filename='flask_error.log',level=logging.INFO)

# generate the current time and shift it to US/Eastern or your tz https://delorean.readthedocs.io/en/latest/ 
def make_timestamp():
    now = Delorean().shift("US/Eastern").datetime.strftime('%A %B %d %Y, %I:%M:%S %p %Z')
    return now

# serialize datetimes in output as strings
def datetime_to_str(input):
    if isinstance(input, datetime):
        return input.__str__()


### ramco api explorer ###

# root / starting page - displays all entities
@app.route('/', methods=['GET'])
def explorer_root():

    # fetch all entities 
    entities = api_explorer_functions.get_entity_types()

    # return them to the root template
    return render_template('explorer_root.html', entities=entities)


# list metadata for an entity - pass entity name like ?entity= in url args
@app.route('/explorer_entity/', methods=['GET'])
def explorer_entity():
    
    # get entity name from url
    entity = request.args.get('entity')

    # fetch entity metadata
    details = api_explorer_functions.get_entity_metadata(entity)

    # return metadata to the entity details template
    return render_template('entity_details.html', entity=entity, details=details)


# list metadata for an attribute - pass entity name and attribute name in url args as above
@app.route('/explorer_attribute/', methods=['GET'])
def explorer_attribute():
    
    # get entity and attribute names from url
    entity = request.args.get('entity')
    attribute = request.args.get('attribute')
    
    # fetch entity metadata
    attribute_details = api_explorer_functions.get_attribute_details(entity, attribute)

    # return metadata and parent info to the attribute details template 
    return render_template('attribute_details.html', entity=entity, attribute=attribute, attribute_details=attribute_details)


# list metadata for a relationship, pass entity name and relationship name in url args as above
@app.route('/explorer_relationship/', methods=['GET'])
def explorer_relationship():
    
    # get entity and relationship names from url
    entity = request.args.get('entity')
    relationship = request.args.get('relationship')
    
    # fetch entity metadata
    relationship_details = api_explorer_functions.get_relationship_details(entity, relationship)

    # return metadata and parent info to the relationship details template 
    return render_template('relationship_details.html', entity=entity, relationship=relationship, relationship_details=relationship_details)
