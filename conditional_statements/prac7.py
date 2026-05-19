person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']

    middle_index = len(skills) //2
    print(skills[middle_index])

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    has_python = 'Python' in skills
    print("it is having:", has_python)

#If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if skills == ['JavaScript','React']:
    print("He is a front end developer")

elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("He is a backend developer")

elif 'React'in skills  and 'Node'in skills and 'MongoDB' in skills:
    print("He is a full-stack developer")

else:
    print("unknown title")

#f the person is married and if he lives in Finland, print the information in the following format:
if person['is_married']  and person['country'] =='Finland':
    print (f"{person['first_name']} lives in {person['country']}. He is married ")