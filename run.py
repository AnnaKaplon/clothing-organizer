import click

from organizer.app import make_app
from organizer.dal.db import session
from organizer.dal.model.user import User


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
def create_user(email, password):
    new_user = User(email=email, password=password)

    session.add(new_user)
    session.commit()
    session.close()

if __name__ == '__main__':
    cli()
