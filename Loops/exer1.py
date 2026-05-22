
print("--------------------------------------")
print("LEVEL-1")
print("--------------------------------------")
print(" ")
print("------------ 0 to 10 ---------------------")

#Iterate 0 to 10 using for loop, do the same using while loop.
n = 0
while n<=10:
    print(n)
    n+=1
print(" ")
print("--------------10 to 0-------------------")

#Iterate 10 to 0 using for loop, do the same using while loop.
n =10
while n>=0:
    print(n)
    n-=1 
print(" ")
print("---------------right angled triangle------------------")

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1,8):
    for j in range(i):
        print("*", end='')
    print()

print(" ")
print("---------------square------------------")

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(8):
    for j in range(8):
        print("*", end='')
    print()

print(" ")
print("---------------inverted right angled triangle------------------")

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(8):
    for j in range(8-i):
        print("*", end='')
    print()
print(" ")
print("---------------left - right angled triangle------------------")
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(8):
    for j in range(8-i):
        print(" ", end='')
    for k in range(i):
        print("*", end="")
    print()
print(" ")
print("--------------- inverted left - right angled triangle------------------")
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(8, 0 , -1):
    for j in range(8-i):
        print(" ", end='')
    for k in range(i):
        print("*", end="")
    print()
print(" ")
print("---------------table pattern------------------")

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(1, 11):
    print(f"{i} x {i} = {i*i} ")
print(" ")
print("---------------Iterate through the list------------------")

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

list1= ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in list1:
    print(i, end=", ")
print(" ")
print("\n--------------- iterate from 0 to 100 & print even------------------")

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.


for i in range(1,101):
    if i%2==0:
        print(i, end=", ")


print(" ")
print("\n--------------- iterate from 0 to 100 & print odd")
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.


for i in range(1,101):
    if i%2==1:
        print(i, end=", ")

print(" ")
print(" ")
print(" ")
print("--------------------------------------")
print("LEVEL-2")
print("--------------------------------------")
print(" ")
print("------------ 0 to 100 ---------------------")

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum=0
for i in range (0,101):
    sum+=i
print("The sum of all numbers is: ",sum)

print(" ")
print("------------ sum of all even num & odd num in 0 to 100 ---------------------")

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum1=0
sum2=0
for i in range (0,101):
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
print("The sum of all even numbers is: ",sum1)
print("The sum of all odd numbers is: ",sum1)




print(" ")
print(" ")
print(" ")
print("--------------------------------------")
print("LEVEL-3")
print("--------------------------------------")



print(" ")
print("------------ extract all the countries containing the word land. ---------------------")

#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]


for i in countries:
    if 'land' in i.lower():
        print(i)


print(" ")
print("------------ reverse the order using loop ---------------------")

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruit = ['banana', 'orange', 'mango', 'lemon']
rev_fruit=' '
for i in fruit:
    rev_fruit= i + ' , '+ rev_fruit

print(rev_fruit)

print(" ")
print("------------playing with list ---------------------")

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
print("1. ")


# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world