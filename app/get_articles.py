import click
import requests

from app.utils import (
        spinner,
        url,
        check_connection,
        json_formatter,
        export_json_csv,
        )


class GetArticles:
    """
    Fetch articles from API
    """

    @staticmethod
    def get_single_article(article_id, export):
        """
        Returns article with matching article_id
        """
        check_connection()
        spinner.start()
        response = requests.get(url + "/articles/{}/".format(article_id))
        spinner.stop()
        spinner.clear()

        if response.status_code == 404:
            spinner.warn("The article requested was not found 😬")
            click.echo("Status code: {}".format(response.status_code))
        elif response.status_code == 200:
            spinner.succeed("Article found 🤓")
            click.echo("Status code: {}".format(response.status_code))
            article = json_formatter(response.text)
            click.echo(article)
            if export:
                #  limited to 1 article by default
                export_json_csv(article, export, limit=True)

    @staticmethod
    def get_all_articles(limit, export):
        """
        Returns article with matching article_id
        """
        check_connection()
        spinner.start()
        response = requests.get(url + "/articles/feed/")
        spinner.stop()
        spinner.clear()
        spinner.succeed("Done fetching articles")
        click.echo("Status code: {}".format(response.status_code))

        articles = json_formatter(response.text, limit)
        click.echo(articles)

        def get_next(limit, _next):
            if click.confirm("Would you like to see the next {} articles?"
                             .format(limit)):
                click.echo("fetching next {}...".format(limit))
                json_formatter(response.text, limit, _next)
                _next += limit
                get_next(limit, _next)

        if limit:
            click.echo("Limited to {} articles".format(limit))
            get_next(limit, _next=limit)

        if export:
            export_json_csv(articles, export, limit)

    @staticmethod
    def get_filtered_article(search_query):
        """
        Returns article with matching search_query
        """
        check_connection()
        spinner.start()
        response = requests.get(
                    url + "/articles/search?{}".format(search_query))
        spinner.stop()
        spinner.clear()

        if response.status_code == 400:
            spinner.warn("The article requested was not found 😬")
            click.echo("Status code: {}".format(response.status_code))
        elif response.status_code == 200:
            spinner.succeed("Article found 🤓")
            click.echo("Status code: {}".format(response.status_code))
            article = json_formatter(response.text)
            click.echo(article)
