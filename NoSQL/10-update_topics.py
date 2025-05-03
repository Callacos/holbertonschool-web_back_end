#!/usr/bin/env python3
"""Module pour insérer un document dans une collection MongoDB."""


def update_topics(mongo_collection, name, topics):
    """
    Met à jour les topics d'un document école selon son nom.

    Args:
        mongo_collection: Objet collection pymongo.
        name (str): Nom de l'école à mettre à jour.
        topics (list): Nouvelle liste de topics à attribuer.
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
