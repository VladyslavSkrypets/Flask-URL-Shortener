get_short_link_schema = {
    'type': 'object',
    'properties': {
        'uid': {'type': 'string'},
    },
    'required': ['uid']
}

add_link_schema = {
    'type': 'object',
    'properties': {
        'link': {'type': 'string'},
        'expire_days': {'type': ['string', 'integer']}
    },
    'required': ['link']
}