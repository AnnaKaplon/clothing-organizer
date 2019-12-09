import click

from organizer.app import make_app


@click.group()
def cli():
    pass


@cli.command()
def run():
    app = make_app()
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    cli()
