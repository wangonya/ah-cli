import click
import requests

from app.utils import (
        spinner,
        url,
        check_connection,
        json_formatter,
        )


class GetArticles:
    """
    Fetch articles from API
    """

    @staticmethod
    def get_single_article(article_id):
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

    @staticmethod
    def get_all_articles(limit):
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

        if limit:
            click.echo("Limited to {} articles".format(limit))

        articles = json_formatter(response.text, limit)
        click.echo(articles)
