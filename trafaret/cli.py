import click

from trafaret.config import Config
from trafaret.solution import iter_solutions
from typing import IO, Optional


@click.command(
    help='Show the code handout.')
@click.argument('exercise', type=click.File('r'))
def handout(exercise: IO[str]) -> None:
    config = Config.load(exercise)
    handout = config.todo_handout()
    print(handout)


@click.command(
    help='Show the exercise text and code handout.')
@click.argument('exercise', type=click.File('r'))
def markdown(exercise: IO[str]) -> None:
    config = Config.load(exercise)
    text = config.text()
    handout = config.html_handout()
    print(text)
    print()
    print(handout)


@click.command(
    help='Show the solution(s).')
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


main.add_command(handout)
main.add_command(markdown)
main.add_command(solution)

if __name__ == "__main__":
    main()
