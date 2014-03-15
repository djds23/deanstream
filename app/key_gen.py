import uuid

def return_uuid():
    '''return a string with your secret key'''
    key = uuid.uuid1()
    return str(key)
