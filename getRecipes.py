# python
from bs4 import BeautifulSoup
import requests

# local
from helpers.utility import get_recipe, get_urls

#====================================================================================================

def main():
    filename = "recipes.txt"
    urls = get_urls(filename)
    print(urls)
    #serves, nutrition, ingredient, method = get_recipe(source_url)
    #print(method[0].split("."))

    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/47.0.2526.80 Safari/537.36"
    }


#====================================================================================================

if __name__ == "__main__":
    main()
