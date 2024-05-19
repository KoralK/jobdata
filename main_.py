import pandas as pd
import requests

def fetch_usajobs_data(request):
    request_json = request.get_json(silent=True)
    keyword = request_json.get('Keyword', '')
    location = request_json.get('LocationName', '')

    response = requests.get(
        'https://data.usajobs.gov/api/search',
        headers={
            'User-Agent': 'koralk76@gmail.com',
            'Authorization-Key': 'wzwURejqNCHS+vH+Nrcz3EmTFl0cpwxZsIH71KcT+ZM='
        },
        params={
            'Keyword': keyword,
            'LocationName': location
        }
    )

    job_data = response.json()
    jobs = [job['MatchedObjectDescriptor'] for job in job_data.get('SearchResult', {}).get('SearchResultItems', [])]
    df = pd.DataFrame(jobs)
    
    return {'status': 'success', 'data': df.to_dict()}
