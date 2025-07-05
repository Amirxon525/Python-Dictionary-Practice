def get_emails_of_older_than(data, age):
    return [u["email"] for u in data["results"] if u["dob"]["age"] > age]