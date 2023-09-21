# Experimentation playground. One ready to go is at eol.py

import requests

CLIENT_ID = 'id'
CLIENT_SECRET = 'secret'

API_URL = 'https://api.getport.io/v1'

credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}

token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)

access_token = token_response.json()['accessToken']

# You can now use the value in access_token when making further requests

headers = {
    'Authorization': f'Bearer {access_token}'
}

blueprint_id = 'framework'
# entity_id = 'MY_ENTITY_IDENTIFIER'

response = requests.get(f'{API_URL}/blueprints/{blueprint_id}/entities', headers=headers)
response_repo = requests.get(f'{API_URL}/blueprints/{blueprint_id}/entities', headers=headers)
DATA_RESP = response.json()
print(DATA_RESP['entities'].count('EOL'))

# initialize counter for packages
count = 0

for d in DATA_RESP['entities']:
    print(d['title'] , d['properties']['state'])
    title = d['title']
    state = d['properties']['state']
    entity_identifier = d['identifier']

    # update counter for EOL packages
    if state == "EOL":
        count = count + 1
        print(count)


    # playing with updating entities some
    # entity_json = {
    #     'identifier': entity_identifier,
    #     'title': title,
    #     'properties': {
    #         'state': state,
    #     },
    #     'relations': {}
    # }

    # url = f'{API_URL}/blueprints/{blueprint_id}/entities/{entity_identifier}/{state}'

entity_json = {
    'identifier': '<some identifier>',
    'properties': {
        'number_of_eol_packages': count
    },
}
print(count)
url = f'{API_URL}/blueprints/{blueprint_id}/entities/?upsert=true'
update_query = requests.post(url, json=entity_json, headers=headers) # put or post option??
update_packages = requests.post(f'https://api.getport.io/v1/blueprints/repository/entities?upsert=true', json=entity_json, headers=headers)

# parse response here
# print(update_query.json())

update_packages.json()
print(update_packages.json())