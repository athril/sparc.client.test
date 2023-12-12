#import importlib.metadata
from .client import SparcClient

__all__: tuple[str, ...] = [
    "SparcClient",
    # "services.pennsieve.PennsieveService"
]


#__version__ = importlib.metadata.version(__package__)

#import pkg_resources
# __version__ = pkg_resources.get_distribution("sparc.client").version


#from setuptools import setup
#import dynamic_versioning
#setup(cmdclass={"egg_info": dynamic_versioning.DynamicVersioningEggInfo})