from importlib.metadata import version
from .client import SparcClient

__all__: tuple[str, ...] = [
    "SparcClient",
    # "services.pennsieve.PennsieveService"
]


__version__ = version(__package__)

# import pkg_resources
# __version__ = pkg_resources.get_distribution("sparc.client").version
