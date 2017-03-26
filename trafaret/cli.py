import click

from trafaret.config import Config
from typing import IO


@click.command(help='Show the exercise text and code handout in Markdown format.')
@click.argument('exercise', type=click.File('r'))
def show(exercise: IO[str]) -> None:
    config = Config.load(exercise)
    text = config.text()
    handout = config.handout()
    print(text)
    print()
    print(handout)


@click.group()
def main() -> None:
    pass


main.add_command(show)

if __name__ == "__main__":
    main()
