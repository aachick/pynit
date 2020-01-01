import os


template = '''\
import setuptools


setuptools.setup(
    name='{program}',
    version='{version}',
    author='{author}',
    description='{description}',,
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3'
)
'''

def create_setup_file(proj_dir, program='', author='', version='', description=''):
    setup_py = template.format(
        program=program, author=author, version=version, description=description
    )

    with open(os.path.join(proj_dir, 'setup.py'), 'w') as f:
        f.write(setup_py)
