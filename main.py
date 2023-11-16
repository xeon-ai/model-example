import argparse

from commands.init import init

def main():
    """The entrypoint for the script"""
    parser = argparse.ArgumentParser(description='Create and manage your computer vision models for the xeon platform')
    subparsers = parser.add_subparsers(required=True)

    init_parser = subparsers.add_parser('init', description='Initialize a new project')
    init_parser.add_argument('--force', help='Removes the existing project', action='store_true')
    init_parser.set_defaults(func=init)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()