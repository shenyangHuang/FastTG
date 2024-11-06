"""
fastTG - Python library for fast and efficient temporal graph learning. 
"""

__version__ = "0.1.0"

class TemporalGraph(object):
    pass


def discretize(graph):
    """
    Discretize the temporal graph.

    :param graph: The temporal graph object
    :type graph: TemporalGraph or None
    :raise ache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]




"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]