import click

from trafaret.config import Config
from trafaret.solution import iter_solutions
from typing import IO, Optional


@click.command(
    help='Show the exercise text and code handout in Markdown format.')
@click.argument('exercise', type=click.File('r'))
def show(exercise: IO[str]) -> None:
    config = Config.load(exercise)
    text = config.text()
    handout = config.handout()
    print(text)
    print()
    print(handout)


@click.command()
@click.argument('exercise', type=click.File('r'))
@click.option('--index', '-i', type=int)
def solution(exercise: IO[str], index: Optional[int]) -> None:
    config = Config.load(exercise)
    solutions = list(iter_solutions(config))
    if index:
        solutions[index]
    else:
        print("\n---- OR ----\n".join(solutions))


@click.group()
def main() -> None:
    pass


main.add_command(show)
main.add_command(solution)

if __name__ == "__main__":
    main()
