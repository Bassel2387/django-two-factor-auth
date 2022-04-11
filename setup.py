from setuptools import find_packages, setup

setup(
    name='django-two-factor-auth',
    version='1.13.1.3',
    description='Complete Two-Factor Authentication for Django',
    long_description=open('README.rst', encoding='utf-8').read(),
    author='Bouke Haarsma',
    author_email='bouke@haarsma.eu',
    url='https://github.com/Bouke/django-two-factor-auth',
    download_url='https://pypi.python.org/pypi/django-two-factor-auth',
    license='MIT',
    packages=find_packages(exclude=('example', 'tests')),
    install_requires=[
        'Django>=2.2',
        'django_otp>=0.8.0',
        'qrcode>=4.0.0,<6.99',
        'django-phonenumber-field>=1.1.0,<6',
        'django-formtools',
    ],
    extras_require={
        'call': ['twilio>=6.0'],
        'sms': ['twilio>=6.0'],
        'yubikey': ['django-otp-yubikey'],
        'phonenumbers': ['phonenumbers>=7.0.9,<8.99',],
        'phonenumberslite': ['phonenumberslite>=7.0.9,<8.99',],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ],
)
