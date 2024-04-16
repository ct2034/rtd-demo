

class DemoClass:
    """
    This is just a demo.
    """
    def __init__(self):
        self.__version__ = "0.0.1"

    def get_version(self):
        """
        Get the version of the package.
        """
        return self.__version__