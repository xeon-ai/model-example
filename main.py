import argparse

from commands.init import init
from commands.update import update
from commands.train import train

def main():
    """The entrypoint for the script"""
    parser = argparse.ArgumentParser(description='Create and manage your computer vision models for the xeon platform')
    subparsers = parser.add_subparsers(required=True)

    init_parser = subparsers.add_parser('init', description='Initialize a new project')
    init_parser.add_argument('--force', help='Removes the existing project', action='store_true')
    init_parser.set_defaults(func=init)

    update_parser = subparsers.add_parser('update', description='Update an existing project')
    update_parser.set_defaults(func=update)

    train_parser = subparsers.add_parser('train', description='Train a new model')
    train_parser.add_argument('--epochs', default=10, type=int, help='Number of epochs')
    train_parser.add_argument('--batch-size', default=8, type=int, help='Batch size')
    train_parser.set_defaults(func=train)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()