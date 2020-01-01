import argparse
import os
import subprocess

from .licenses import LICENSES, create_license
from .setup_config import create_setup_file


def parse_cli():
    parser = argparse.ArgumentParser(
        prog='pynit',
        description='A simple tool to standardize the creation of Python projects.'
    )

    parser.add_argument(
        'project_dir', help='The Python project directory'
    )

    prog_group = parser.add_argument_group('Program options')
    prog_group.add_argument(
        '-n', '--name', dest='project_name', help='The Python project name',
        default=''
    )
    prog_group.add_argument(
        '--author', dest='author', help='The project\'s author', default=''
    )
    prog_group.add_argument(
        '--description', dest='description', help='A brief project description', default=''
    )
    prog_group.add_argument(
        '--progv', dest='version', help='The program\'s version.', default='0.0.1'
    )

    setup_group = parser.add_argument_group('Setup options')
    setup_group.add_argument(
        '--setup', dest='setup', help='Add a setup.py file', action='store_true'
    )
    setup_group.add_argument(
        '--manifest', dest='manifest', help='Include a manifest file',
        action='store_true'
    )

    parser.add_argument(
        '--readme', dest='readme', help='Include a README file.', action='store_true'
    )
    parser.add_argument(
        '--license', dest='license', help='The project\'s license',
        choices=LICENSES, default=''
    )
    parser.add_argument(
        '--no-git', dest='git', help='Disable the git repository creation step.',
        action='store_false'
    )


    args = parser.parse_args()

    return args


def create_proj_dir(proj_dir, proj_name):
    if proj_name == '':
        proj_name = proj_dir.split(os.sep)[-1]

    proj_path = os.path.join(proj_dir, proj_name)
    os.makedirs(proj_path)

    with open(os.path.join(proj_path, '__init__.py'), 'a+') as f:
        f.write('')


def init_git_repo(proj_dir):
    current_dir = os.path.realpath(os.curdir)
    os.chdir(proj_dir)

    pipe = subprocess.Popen(
        ['git', 'init'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    _, _ = pipe.communicate()
    ret_val = pipe.poll()
    os.chdir(current_dir)

    if ret_val != 0:
        raise subprocess.SubprocessError()


    with open(os.path.join(proj_dir, '.gitignore'), 'a+') as f:
        f.write('')

    return True


def create_manifest(proj_dir):
    with open(os.path.join(proj_dir, 'MANIFEST.in'), 'a+') as f:
        f.write('')


def create_readme(proj_dir, proj_name, description):
    if proj_name == '':
        proj_name = proj_dir.split(os.sep)[-1]

    with open(os.path.join(proj_dir, 'README.md'), 'a+') as f:
        f.write('# {}\n\n## Description\n\n{}'.format(proj_name, description))


if __name__ == "__main__":
    args = parse_cli()

    proj_dir = args.project_dir
    proj_name = args.project_name

    create_proj_dir(proj_dir, proj_name)

    if args.git:
        init_git_repo(proj_dir)

    if args.manifest:
        create_manifest(proj_dir)

    if args.readme:
        create_readme(proj_dir, proj_name, args.description)

    if args.license != '':
        create_license(
            proj_dir, args.license,
            author=args.author, program=proj_name, description=args.description
        )

    if args.setup:
        create_setup_file(
            proj_dir,
            program=proj_name, author=args.author,
            version=args.version, description=args.description
        )
