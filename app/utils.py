import sys
import requests

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
