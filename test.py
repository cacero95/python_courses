import json
import requests

last_fifth = []
req = requests.get('https://s3.amazonaws.com/sgc.sites.gov.co/feed/v1.0/summary/thirty_days_importan.json')

if req.status_code == 200:
    results = req.json()
    features = [
        results['features'][0],
        results['features'][1],
        results['features'][2],
        results['features'][3],
        results['features'][4]
    ]
    print('partions')
    print(features)
    print('complete')
    print(results['features'])
