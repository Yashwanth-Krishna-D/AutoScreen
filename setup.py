from setuptools import setup, find_packages

setup(
    name='autoscreen',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'requests',
        'transformers',
        'Pillow',
        'customtkinter',
        'fpdf',
    ],
    entry_points={
        'console_scripts': [
            'autoscreen-instagram=autoscreen.instagram_main:scrap',
        ],
    },
    include_package_data=True,
    description='AI-powered web application for digital investigations',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/autoscreen',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
) 