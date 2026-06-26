from pathlib import Path
import argparse

from .repository import Repository
from .exceptions import RepositoryAlreadyExistsError


def init_command(_args):
    repo = Repository(Path.cwd())

    try:
        repo.init()
        print(f"Initialized empty repository in {repo.git_dir}")

    except RepositoryAlreadyExistsError as e:
        print(e)
        return 1

    return 0


def build_parser():
    parser = argparse.ArgumentParser(
        prog="mygit",
        description="A tiny Git implementation written in Python."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser(
        "init",
        help="Initialize a new repository"
    )

    init_parser.set_defaults(func=init_command)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)