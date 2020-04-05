# local
from helpers.utility import get_recipe, get_urls, writeFile

#TODO recipes with same name but different url

def main():
    filename = "recipes.txt"
    urls = get_urls(filename)
    for recipeName in urls:
        url = urls[recipeName]
        serves, nutrition, ingredient, method = get_recipe(url)
        writeFile(recipeName, serves, nutrition, ingredient, method)

#====================================================================================================

if __name__ == "__main__":
    main()
