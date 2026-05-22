from countries_data import countries
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data


print("1. ")
lang_count={}
for i in countries:
    for lang in i["languages"]:
        if lang in lang_count:
            lang_count[lang]+=1
        else:
            lang_count[lang] = 1   
print(lang_count)

# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world