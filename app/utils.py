import sys
import requests
import json
import csv

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


def export_json_csv(data, _format, limit):
    data = json.loads(data)

    if not limit:
        data = data["results"]

    if _format == "json":
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2)
    elif _format == "csv":
        with open('data.csv', 'w', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            count = 0
            for article_data in data:
                if count == 0:
                    header = article_data.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(article_data.values())

    spinner.succeed("Exported to {} 🚀".format(_format))
