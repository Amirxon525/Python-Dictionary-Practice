def get_average_age(data):
    ages = [i["dob"]["age"] for i in data["results"]]
    return sum(ages) / len(ages)