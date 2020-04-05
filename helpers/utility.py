# helper functions

def get_urls(file):
    """ get recipe urls from file """
    urls = []
    with open(file, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue
            urls += [line.strip("\n")]
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
