def get_users_by_country(data, country_name):
    return [
        {"name": f"{u['name']['first']} {u['name']['last']}", "email": u["email"]}
        for u in data["results"] if u["location"]["country"] == country_name
    ]