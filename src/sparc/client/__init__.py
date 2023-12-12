#import importlib.metadata
from .client import SparcClient
from ._version import __version__ 
#from sparc.client._version import __version__ 

#from _version import __version__

__all__: tuple[str, ...] = [
    "SparcClient",
    # "services.pennsieve.PennsieveService"
]

#print('__version__')
#print(__version__)

#__version__ = importlib.metadata.version(__package__)
# import pkg_resources
# __version__ = pkg_resources.get_distribution("sparc.client").version


#from setuptools import setup
#import dynamic_versioning
#setup(cmdclass={"egg_info": dynamic_versioning.DynamicVersioningEggInfo})