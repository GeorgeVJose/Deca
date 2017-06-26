import urllib2
import json
from ConfigParser import ConfigParser

url = "https://ipinfo.io/json"
config_file = "./config_file.cfg"

def parse_response(response_json):
    del(response_json['ip'])
    # del(response_json['hostname'])
    response_json['City'] = response_json.pop('city')
    response_json['State'] = response_json.pop('region')
    response_json['Country'] = response_json.pop('country')
    if response_json['Country'] == 'IN':
        response_json['Country'] = 'India'

    latitude, longitude = response_json['loc'].split(',')
    response_json['Latitude'] = float(latitude)
    response_json['Longitude'] = float(longitude)
    del(response_json['loc'])
    del(response_json['postal'])
    del(response_json['org'])
    response_json['UnitPreference'] =  "METRIC"
    return response_json

response = 0

try:
    response = urllib2.urlopen(url)
    response_json = json.loads(response.read())

except Exception as e:
    print "Error : Error retieving location (Check Connection) , ", e

'''
Update the config file once the location is recieved.
'''
if response:
    config  = ConfigParser()
    config.read(config_file)
    requestinfo = parse_response(response_json)
    for key in response_json.keys():
        config.set('Location', key, response_json[key])

    config.set('RequestInfo', 'requestinfo', json.dumps(requestinfo))
    with open(config_file, 'w') as f:
        config.write(f)
    print "INFO : Location Updated."
