import sys
import requests
import json

from halo import Halo

spinner = Halo(text='Loading', spinner='dots', text_color='cyan')
url = "https://ah-django-staging.herokuapp.com/api"


def check_connection(url="http://example.com/"):
    """
    Check internet connection
    Raise exception if none
    """
    try:
        requests.head(url)
        return True
    except requests.ConnectionError:
        spinner.warn("No internet connecction 🤭")
        sys.exit(1)


def json_formatter(data, limit=None):
    """
    Preetify the json data 💅
    """
    json_data = json.loads(data)

    if limit:
        limited_json_data = json_data["results"][:limit]
        return json.dumps(limited_json_data, indent=2)

    return json.dumps(json_data, indent=2)
