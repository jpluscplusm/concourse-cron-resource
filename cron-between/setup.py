from setuptools import find_packages, setup


setup(
    name='between',
    version='0.1',

    description='List cron firing times',

    license='...',
    author='...',
    author_email='...',

    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': ['between=between:main'],
    },

    install_requires=[
        'croniter==1.0.15',
    ],
    python_requires='>=3.6',

    classifiers=[
        '...',
    ],
)
