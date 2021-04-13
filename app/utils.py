import sys
import requests
import json
import csv
import sqlite3 as sq

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


def json_formatter(data, limit=None, _next=None):
    """
    Preetify the json data 💅
    """
    json_data = json.loads(data)

    if limit:
        limited_json_data = json_data["results"][:limit]
        if _next:
            print("{}:{}".format(_next, limit))
            print(json_data["results"][2:2])
            next_json_data = json_data["results"][_next:limit]
            return json.dumps(next_json_data, indent=2)
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
    elif _format == "sqlite":
        conn = sq.connect('data.db')
        c = conn.cursor()
        columns = list(data[0].keys())
        columns.remove('tagList')
        columns.remove('comments')
        c.execute("""
                    CREATE TABLE IF NOT EXISTS
                    articles (
                    id integer primary key,
                    likes integer,
                    dislikes integer,
                    like_popularity integer,
                    description text,
                    rating integer,
                    title text,
                    slug text,
                    body text,
                    created text,
                    updated text,
                    reading_time text,
                    reads integer,
                    views integer,
                    image text,
                    author integer
                    )
                    """)
        query = """
                INSERT OR REPLACE INTO articles values
                (?{})
                """.format(",?" * (len(columns)-1))

        for article_data in data:
            article_data = tuple(article_data[c] for c in columns)
            c.execute(query, article_data)
            conn.commit()
        c.close()

    spinner.succeed("Exported to {} 🚀".format(_format))
