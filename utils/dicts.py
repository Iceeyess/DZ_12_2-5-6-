# файл dicts.py
def get_val(collection, key, default='git'):
    if collection:
        return collection.get(key, default)
    return collection.get(key, default)