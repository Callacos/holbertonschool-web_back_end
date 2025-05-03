#!/usr/bin/env python3
"""Module pour insérer un document dans une collection MongoDB."""


def schools_by_topic(mongo_collection, topic):
    """
    Retourne la liste des écoles qui abordent un topic donné.

    Args:
        mongo_collection: Objet collection pymongo.
        topic (str): Le topic à rechercher.

    Returns:
        Une liste de documents correspondant.
    """
    return list(mongo_collection.find({ "topics": topic }))
