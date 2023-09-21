# to do: Write a script in Python that queries the different repository entities and frameworks, 
# and updates the value of the number of EOL packages property on each repository entity with the correct value.

import requests

CLIENT_ID = '<client-id>'
CLIENT_SECRET = '<client-secret>'

API_URL = 'https://api.getport.io/v1'

credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}

token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)

access_token = token_response.json()['accessToken']

# You can now use the value in access_token when making further requests

headers = {
    'Authorization': f'Bearer {access_token}'
}

# Query Repositories
repository_id = 'repository'
blueprint_id = 'framework'

response_repo = requests.get(f'{API_URL}/blueprints/{repository_id}/entities', headers=headers)
REPO_RESPONSE = response_repo.json()

response = requests.get(f'{API_URL}/blueprints/{blueprint_id}/entities', headers=headers)
DATA_RESP = response.json()

# Sanity check
print(DATA_RESP['entities'].count('EOL'))

# Checking Logic
for d in REPO_RESPONSE['entities']:
    print(d['title'], d['identifier'])
    count = 0

    for d in DATA_RESP['entities']:
        print(d['title'] , d['properties']['state'])
        title = d['title']
        state = d['properties']['state']
        entity_identifier = d['identifier']

        # Update counter for EOL packages
        if state == "EOL":
            count = count + 1
            print(count)

        # Entity
        entity_json = {
            'identifier': d['identifier'],
            'properties': {
                'number_of_eol_packages': count # update count for EOL packages here
            },
        }
        url = f'{API_URL}/blueprints/{blueprint_id}/entities/?upsert=true'

        update_query = requests.post(url, json=entity_json, headers=headers) 
        update_packages = requests.post(f'https://api.getport.io/v1/blueprints/repository/entities?upsert=true', json=entity_json, headers=headers)

        # Run query and print response options
        update_packages.json()
        print(update_packages.json())
