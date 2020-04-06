import csv
import requests
import json
from typing import List, Dict
from bs4 import BeautifulSoup as bs
import re
import os

# YELP_API_KEY = os.environ['YELP_API_KEY']
from scripts.YELP_API_KEY import YELP_API_KEY


def search_nested(nested_dictionary,
                  keys: List[str],
                  aliases=None,
                  result=[]) -> List[Dict[str, str]]:
    """
    Searches a nested dictionary for the given keys and returns a list of key
    and value pairs substituted with the aliases if given.
    :param nested_dictionary: nested dictionary to be searched
    :param keys: desired keys to be found in a list
    :param aliases: aliases for the keys as a dictionary
    :param result: a list of dictionaries
    :return: list of dictionaries
    """
    for key, value in nested_dictionary.items():
        if key in keys and aliases is not None and key in aliases:
            result.append({aliases[key]: value})
        elif key in keys:
            result.append({key: value})
        elif type(value) is dict:
            search_nested(value, keys, aliases, result)
    return result


def get_business_info(ids: List[str],
                      keys: List[str],
                      aliases=None):
    """
    Makes a request to the Yelp business api and gets the desired params.
    :param ids: a
    :param keys: the desired keys from the yelp business api
    :param aliases: dictionary of key value pairs to replace if found
    :return: List of dictionaries of the businesses
    """
    businesses: List[Dict] = []
    url = 'https://api.yelp.com/v3/businesses/'
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
    for id_ in ids:
        response = requests.get(f'{url}{id_}', headers=headers)
        business = {'id': id_}
        for key, value in response.json().items():
            if key in keys and aliases is not None and key in aliases:
                business[aliases[key]] = response.json()[key]
            elif key in keys:
                business[key] = response.json()[key]
            elif type(value) is dict:
                nested_keys = search_nested(value, keys, aliases)
                for result in nested_keys:
                    business.update(result)
        businesses.append(business)
    return businesses


def scrape_business_info(yelp_url):
    """
    Scrapes the url from the yelp page and returns the url.
    :param yelp_url: yelp url to scrape
    :return: the url scraped as a string
    """
    response = requests.get(yelp_url)
    soup = bs(response.text, 'html.parser')
    url = soup.find('a', href=re.compile("^\/biz_redir\?url="), role='link')
    if url is not None:
        return url.text
    return url


def main(csv_file: str, keys: List[str],
         aliases: Dict[str, str],
         create_json=False):
    """
    Reads ids from a csv file, grabs data from yelp and optionally generates a
    json file.
    :param csv_file: csv file path to pull ids from
    :param keys: keys to be grabbed from yelp api
    :param aliases: aliases to be used
    :param create_json: whether a json file should be created
    :return: List of businesses
    """
    ids: List[str] = []
    with open(csv_file, 'r') as csv_file:
        for row in csv.reader(csv_file):
            ids.append(row[0])

    businesses = get_business_info(ids, keys, aliases)
    for business in businesses:
        business['url'] = scrape_business_info(business['yelp_url'])
    if create_json is True:
        with open('scripts/businesses.json', 'w') as json_file:
            json.dump(businesses, json_file)
    return businesses


if __name__ == '__main__':
    from scripts.config import SOURCE, YELP_KEYS, ALIASES
    main(csv_file=SOURCE,
         keys=YELP_KEYS,
         aliases=ALIASES,
         create_json=False)
