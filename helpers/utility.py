# helper functions
from bs4 import BeautifulSoup
import requests

#====================================================================================================

headers = {
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/47.0.2526.80 Safari/537.36"
}

#====================================================================================================

def nonblank_lines(f):
    """ python generator to get non-empty lines """
    for l in f:
        line = l.rstrip()
        if line:
            yield line

#====================================================================================================

def get_urls(file):
    """ get recipe urls from file """
    urls = {}
    with open(file, "r") as f:
        for line in nonblank_lines(f):
            if line.startswith("#"):
                continue
            lineString = line.strip("\n").split(",")
            name = lineString[0]
            url  = lineString[1]
            urls[name] = url
    return urls

#====================================================================================================

def get_recipe(source_url):
    """ get recipe - from main repo """
    webpage = requests.get(source_url, headers=headers)
    soup = BeautifulSoup(webpage.content, "lxml")
    serves = str(soup.find(
        "span",
        {"class": "recipe-details__text", "itemprop": "recipeYield"}).text
    )
    nutri_name = ["kcal", "fat", "saturates", "carbs"]
    nutri_name.extend(["sugars", "fibre", "protein", "salt"])
    kcal = str(soup.find(
        "span",
        {"itemprop": "calories"}).text
    )
    fat = str(soup.find("span", {"itemprop": "fatContent"}).text)
    saturates = str(soup.find(
        "span",
        {"itemprop": "saturatedFatContent"}).text
    )
    carbs = str(soup.find("span", {"itemprop": "carbohydrateContent"}).text)
    sugars = str(soup.find("span", {"itemprop": "sugarContent"}).text)
    fibre = str(soup.find("span", {"itemprop": "fiberContent"}).text)
    protein = str(soup.find("span", {"itemprop": "proteinContent"}).text)
    salt = str(soup.find(
        "span",
        {"itemprop": "sodiumContent"}).text
    )
    nutri_value = [kcal, fat, saturates, carbs, sugars, fibre, protein, salt]
    nutrition = str({k: v for k, v in zip(nutri_name, nutri_value)})
    x = 1
    method, ingredient = [], []
    for i in soup.find_all(
        "li", {"class": "method__item", "itemprop": "recipeInstructions"}
    ):
        for j in i:
            method.append(str(x) + " . " + j.text)
            x = x + 1
    for i in soup.find_all(
        "li",
        {"class": "ingredients-list__item", "itemprop": "ingredients"}
    ):
        for j in i:
            if j.name == 'span' or j.name == 'div':
                j.decompose()
            else:
                pass
        ingredient.append(i.text)
    return serves, nutrition, ingredient, method

#====================================================================================================

def formatMethod(method):
    """ Format method nicely.
        Method is provided as a dictionary of parts,
        with each part containing a single line string of sentences.
        Write each sentence per part on a new line,
        with a new line to separate the parts."""

    result = ""
    for part in range(len(method)):
        sentences = method[part].split(".")
        for sentence in sentences:
            result += sentence + "\n"
        result += "\n"
    return result

#====================================================================================================

def writeFile(recipeName, serves, nutrition, ingredient, method):
    recipe = method
    with open("output/{recipeName}.txt".format(recipeName = recipeName), "w") as f:
        f.write("================= ")
        f.write(recipeName)
        f.write(" =================")
        f.write("\n")

        f.write(serves + "\n")

        #f.write(nutrition + "\n")

        f.write("\n")
        f.write("Ingredients:" + "\n")
        for i in ingredient:
            f.write(i + "\n")

        f.write("\n")
        f.write("\n")
        f.write("Method" + "\n")
        f.write(formatMethod(recipe))

