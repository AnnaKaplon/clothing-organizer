import click

from organizer.app import make_app
from organizer.models.user import User


@click.group()
def cli():
    pass


@cli.command()
def run():
    app = make_app()
    app.run(host='0.0.0.0')


@cli.command()
@click.option('-e', '--email', required=True)
@click.option('-p', '--password', required=True)
def add_user(email, password):
    User.create_user(email, password)


if __name__ == '__main__':
    cli()
