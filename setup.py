from distutils.core import setup
from linearizator import Metadata

metadata = Metadata()

setup(
    name = 'linearizator',
    packages = ['linearizator'],
    version = metadata.get_version(),
    license = 'LGPL v3',
    description = 'Small library to solve linearization problems',
    author = metadata.get_author(),
    author_email = 'contact@rdch106.hol.es',
    url = 'https://github.com/RDCH106/linearizator',
    download_url = 'https://github.com/RDCH106/linearizator/archive/v'+metadata.get_version()+'.tar.gz',
    keywords = ['math', 'linearization'],
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)