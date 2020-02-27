import pyramco
from datetime import datetime
from delorean import Delorean


# generate the current time and shift it to US/Eastern
def make_timestamp():
    output = Delorean().shift("US/Eastern").datetime.strftime('%A %B %d %Y, %I:%M:%S %p %Z')
    return output


# get all entities
def get_entity_types():

    output = pyramco.get_entity_types()
    return output 


# get entity detail
def get_entity_metadata(entity):

    output = pyramco.get_entity_metadata(entity)
    return output 


# get attribute detail
def get_attribute_details(entity, attribute):

    # fetch entity metadata
    entity_details = pyramco.get_entity_metadata(entity)

    # isolate attribute's metadata
    attribute_reply = entity_details['Data']['Attributes'][f'{attribute}']

    # create a blank dict 'attribute_details'
    attribute_details = {}

    # iterate over attribute metadata
    for option_type, option_set in attribute_reply.items():
        
        # for Type 'OptionSet' you need the option values
        if option_type == 'Type' and option_set == 'OptionSet':
            
            # fetch option values from api
            option_set_details = pyramco.get_option_set(entity, attribute)

            # sometimes option sets are lists, just because
            if type(option_set_details['Data']) == list:
                
                # create a blank dict 'options'
                options = {}

                # convert list to dict with val:val format
                for each in option_set_details['Data']:
                    options[f'{each}**']=f'{each}'

                # add option values to dict 'attribute_details'
                attribute_details['Options']=options

            # option sets are normally dicts
            else:

                # add option values to dict 'attribute_details'
                attribute_details['Options']=option_set_details['Data']
        
        # for all other entity types, add values to dict 'attribute_details'
        else:
            attribute_details[f'{option_type}']=f'{option_set}'

    return attribute_details


# get attribute detail
def get_relationship_details(entity, relationship):
        
    # fetch entity metadata
    entity_details = pyramco.get_entity_metadata(entity)

    # isolate replationship's metadata
    relationship_reply = entity_details['Data']['Relationships'][f'{relationship}']

    # create a blank dict 'relationship_details'
    relationship_details = {}

    # iterate over relationship metadata
    for option_type, option_set in relationship_reply.items():
        
        # for Type 'OptionSet' you need the option values
        if option_type == 'Type' and option_set == 'OptionSet':
            
            # fetch option values from api
            option_set_details = pyramco.get_option_set(entity, relationship)

            # add option values to dict 'relationship_details'
            relationship_details['Options']=option_set_details['Data']
        
        # for all other entity types, add values to dict 'relationship_details'
        else:
            relationship_details[f'{option_type}']=f'{option_set}'

    return relationship_details
