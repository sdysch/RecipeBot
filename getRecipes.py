# local
from helpers.utility import get_recipe, get_urls

#====================================================================================================

def main():
    filename = "recipes.txt"
    urls = get_urls(filename)
    for recipeName in urls:
        url = urls[recipeName]
        serves, nutrition, ingredient, method = get_recipe(url)
        print(method[0].split("."))

#====================================================================================================

if __name__ == "__main__":
    main()
