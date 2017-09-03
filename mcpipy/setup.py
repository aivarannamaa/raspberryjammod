import os.path
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

# Dynamically fetch version
setupdir = os.path.dirname(__file__)
with open(os.path.join(setupdir, 'raspberryjammod', 'VERSION'), encoding="ASCII") as f:
    version = f.read().strip()

setup(
    name="raspberryjammod",
    version=version,
    description="A Mod Forge Minecraft mod implementing most of Raspberry Juice/Pi API",
    long_description="""TODO: long desc""",
    url="https://github.com/arpruss/raspberryjammod",
    author="Alexander R. Pruss (uploaded by Aivar Annamaa)",
    #author_email="...",
    license="MIT",
    
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: Freeware",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",   # TODO: check this
        "Programming Language :: Python :: 2.7", # TODO: check this
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Education",
        "Topic :: Games/Entertainment",
    ],
    keywords="Minecraft mods",
    platforms=["Windows", "macOS", "Linux"],
    python_requires=">=2.7,>=3.2", # TODO: check this
    
    packages=["mcpi", "raspberryjammod"],
    py_modules=["mine"],
    
    # non-Python files
    package_data={
        'raspberryjammod': ['VERSION'],
        #'mcpi' : ['*.txt', 'README.md']
    },
)

