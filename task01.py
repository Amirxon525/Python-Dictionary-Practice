def get_full_names(data):
    return [f"{u['name']['first']} {u['name']['last']}" for u in data["results"]]