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
@click.option('--export', '-e', type=click.Choice(["json"]))
def view(article_id, export):
    """
    View single article
    """
    GetArticles.get_single_article(article_id, export)


@cli.command()
@click.option("--limit", "-l", type=int, default=None)
@click.option(
        '--export', '-e',
        type=click.Choice(["csv", "json"]),
        default=None
        )
def list(limit, export):
    """
    Return list of all articles
    """
    GetArticles.get_all_articles(limit, export)


@cli.command()
@click.argument("search_query", type=str)
def search(search_query):
    """
    Search by tag/title/author
    """
    GetArticles.get_filtered_article(search_query)
