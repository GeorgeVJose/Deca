from ConfigParser import ConfigParser
import json

def get_config_location(config_file="config_file.cfg"):
    '''
    Returns the latitude and longitude.
    '''
    config = ConfigParser()
    config.read(config_file)
    latitude = config.getfloat('Location', 'Latitude')
    longitude = config.getfloat('Location', 'Longitude')
    return latitude, longitude

def get_config_request_info(config_file="config_file.cfg"):
    '''
    Returns the requestInfo json file.
    '''
    config = ConfigParser()
    config.read(config_file)
    requestInfo = json.loads(config.get('RequestInfo', 'requestinfo'))
    return requestInfo

def get_config_authentication(config_file="config_file.cfg"):
    '''
    Returns  client_id and client_key.
    '''
    config = ConfigParser()
    config.read(config_file)
    CLIENT_ID = config.get('Authentication', 'CLIENT_ID')
    CLIENT_KEY = config.get('Authentication', 'CLIENT_KEY')
    return CLIENT_ID, CLIENT_KEY

def get_tts(config_file="config_file.cfg"):
    '''
    Returns language format
    '''
    config = ConfigParser()
    config.read(config_file)
    lang = config.get('TTS', 'lang')
    return lang

def get_decoder_model(config_file="config_file.cfg"):
    '''
    Returns the Snowboy model
    '''
    config = ConfigParser()
    config.read(config_file)
    model = config.get('Decoder', 'model')
    return model

if __name__=="__main__":
    pass
    
