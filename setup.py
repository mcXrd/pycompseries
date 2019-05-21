from setuptools import setup

ascii_snake = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""

setup(
    name='pycompseries',
    version='0.1',
    packages=['pycompseries'],
    install_requires=[],
    url='',
    license='BSD',
    author='mcXrd',
    author_email='',
    description=ascii_snake,
    long_description=open('README.md').read(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pycompseries = pycompseries:main',
        ],
    },
    tests_require=['pytest']
)
