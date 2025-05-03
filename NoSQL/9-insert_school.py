#!/usr/bin/env python3
"""Module pour insérer un document dans une collection MongoDB."""


def insert_school(mongo_collection, **kwargs):
    """
    Insère un nouveau document dans une collection MongoDB.

    Args:
        mongo_collection: Objet collection pymongo.
        **kwargs: Champs du document à insérer.

    Returns:
        L'identifiant (_id) du nouveau document inséré.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
