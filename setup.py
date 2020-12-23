import setuptools

setuptools.setup(
    name='valoStatus',
    version='1.0.9',
    author='D3CRYPT360',
    author_email="lordomega360@gmail.com",
    description='A python library to check for Riot Games server status for VALORANT without an API key',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/D3CRYPT360/valStatus',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>= 3.6',
    keywords=['valorant','gaming','gamers'], 
    include_package_data=True,
    install_requires=['requests']
)