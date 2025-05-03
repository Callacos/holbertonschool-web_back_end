#!/usr/bin/env python3
"""Module pour lister tous les documents d'une collection MongoDB."""


def list_all(mongo_collection):
    """
    Liste tous les documents présents dans une collection MongoDB.

    Args:
        mongo_collection: Objet collection de pymongo.

    Returns:
        Une liste contenant tous les documents de la collection,
        ou une liste vide si la collection est vide ou None.
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
