import datetime
import os


_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'licenses')
LICENSES = [l.split('.')[0] for l in os.listdir(_path)]


def create_license(project_dir, license_name, author='', year='', program='', description=''):
    if license_name not in LICENSES:
        return

    if author == '':
        author = os.environ['USER']
    if year == '':
        year = datetime.datetime.now().year

    with open(os.path.join(_path, license_name + '.txt'), 'r') as f:
        license_ = f.read()

    if license_name == 'MIT':
        license_ = license_.format(author=author, year=year)
    elif license_name == 'GNU_GPLv3':
        if program == '':
            program = '<program>'
            print('No program name was specified. Applying default value in license.')
        if description == '':
            description = '<one line to give the program\'s name and a brief idea of what it does.>'
            print('No program description was specified. Applying default value in license.')

        license_ = license_.format(
            author=author, year=year, program=program, description=description
        )
    elif license_name == 'GNU_AGPLv3':
        if description == '':
            description = '<one line to give the program\'s name and a brief idea of what it does.>'
            print('No program description was specified. Applying default value in license.')

        license_ = license_.format(
            author=author, year=year, description=description
        )
    elif license_name == 'GNU_LGPLv3':
        license_ = license_
    elif license_name == 'MOZILLA_PLv2':
        license_ = license_
    elif license_name == 'APACHEv2':
        license_ = license_.format(author=author, year=year)

    with open(os.path.join(project_dir, 'LICENSE.txt'), 'w') as f:
        f.write(license_)
