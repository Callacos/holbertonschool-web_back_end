#!/usr/bin/env python3
"""Function with type annotations for input and output."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Prend un itérable de séquences (comme des
    listes ou des chaînes de caractères) et
    retourne une liste de tuples. Chaque tuple
     contient une séquence de l'itérable
    et sa longueur.
    """
    return [(i, len(i)) for i in lst]
