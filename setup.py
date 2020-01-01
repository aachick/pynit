import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='pynit',
    version='1.0.0a1',
    author='aachick',
    description='pynit is a package designed to facilitate the creation of Python projects.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aachick/pynit',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3',
    include_package_data=True
)
