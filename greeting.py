import click


def docker_greeting(user_name):
    """Return formatted string by input user_name"""
    return f'Hello, {user_name}, this is the docker greeting application'


@click.command()
@click.option('--name', default='DefaultUser', help='Name of greeting user')
def greeting_user(name):
    click.echo(docker_greeting(name))


if __name__ == '__main__':
    greeting_user()
