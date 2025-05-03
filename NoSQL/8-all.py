def list_all(mongo_collection):
    """
    Liste tous les documents d'une collection MongoDB.

    Args:
        mongo_collection: Objet collection pymongo.

    Returns:
        Liste de documents ou liste vide si la collection est vide.
    """
    return list(mongo_collection.find()) if mongo_collection else []
