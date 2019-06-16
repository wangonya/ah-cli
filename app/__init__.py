import click

from .get_articles import GetArticles


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("Welcome to the ah console app 🥳")
        click.echo("Run ah --help for options.")


@cli.command()
@click.argument("article_id")
def view(article_id):
    """
    View single article
    """
    GetArticles.get_single_article(article_id)


@cli.command()
@click.option("--limit", "-l", type=int, default=None)
def list(limit):
    """
    Return list of all articles
    """
    GetArticles.get_all_articles(limit)
