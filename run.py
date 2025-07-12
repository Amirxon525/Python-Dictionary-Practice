from data import randomuser_data
from randomusers import (
    get_full_names,
    get_users_by_country,
    get_users_by_country,
    count_users_by_gender
)


def run_functions() -> None:
    """
    Runs and prints results of all data processing functions for demonstration purposes.
    """
    # print("Full Names:", get_full_names(randomuser_data))
    # get_users_by_country(randomuser_data,'india')
   # print(get_users_by_country(randomuser_data,'India')
    print(count_users_by_gender(randomuser_data))
run_functions()