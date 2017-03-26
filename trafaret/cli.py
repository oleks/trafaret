import click

from trafaret.config import Config
from typing import IO


@click.command()
@click.argument('exercise', type=click.File('r'))
def show(exercise: IO[str]) -> None:
    config = Config.load(exercise)
    text = config.text()
    print(text)
    print()


@click.group()
def main() -> None:
    pass


main.add_command(show)

if __name__ == "__main__":
    main()
