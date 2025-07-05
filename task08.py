def group_users_by_nationality(data):
    counts = {}
    for i in data["results"]:
        nat = i["nat"]
        counts[nat] = counts.get(nat, 0) + 1
    return counts