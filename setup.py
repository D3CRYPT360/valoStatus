import setuptools

setuptools.setup(
    name='valoStatus',
    version='3.3.16',
    author='D3CRYPT360',
    description='A python module to check for Riot Games server status for VALORANT without an API key',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/D3CRYPT360/valoStatus',
    packages=setuptools.find_packages(exclude=("testkit")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>= 3.6',
    keywords=['valorant','gaming','gamers','riot','riotgames', 'VALORANT'], 
    include_package_data=True,
    install_requires=['http.client']
)
