from data import randomuser_data
def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    results = data['results']

    names = []
    for user in results:
        name = user['name']     #'Molly King' Doeke Krikke.   Gregory Reid.  'Atilla Bennin
        full_name = name['first'] + " " + name['last']
        names.append(full_name)

    return names


def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """
    result = []
    for user in data['results']:
        if user['location']['country'] == country:
            result.append({
                'fullname':user['name']['first'] + " " + user['name']['last'],
                'email': user['email']
            }) 
    return result


def count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
    """
    
    male = 0
    female = 0
    for user in data ['results']:
        if user['gender'] == 'male':
            male += 1
        elif user['gender'] == 'female':
            female += 1
    users = {
        'male': male,
        'female': female
    }
    return users

def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    results = []
    for user in data["results"]:
        if user['dob']['age'] >= age:
            results.append(user['email'])
    return results


def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """
    pass


def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    results = []
    for user in data['results']:
        if user['login']['username'].startswith(letter,0):
            results.append(user['login']['username'])
    return results


def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    age_ygindi = 0
    users = 0
    for  user in data['results']:
        age_ygindi += user['dob']['age']
        users += 1
    return  age_ygindi / users


def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    result = dict()
    # count = 1
    for user in data['results']:
        result.setdefault(user['nat'],0)
        result[user['nat']] += 1

    return result


def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    coordinatalar = []
    for user in data['results']:
        coordinatalar.append(tuple(user['location']['coordinates'].values()))
    return coordinatalar


def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """
    pass


def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    result = []
    for user in data['results']:
        if user['location']['timezone']['offset'] == offset:
            person = {
                'name': user['name']['first'] + ' ' + user['name']['last'],
                'city': user['location']['city']
            }
            result.append(person)
    return result


def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    result = []
    for user in data['results']:
        regestrated_year = int(user['registered']['date'][0:4:1])
        if regestrated_year == year:
            s = {
                'name': user['name']['first'] + ' ' + user['name']['last'],
                'registered': str(user['registered']['date'][0:10])
            }
            result.append(s)
    return result



