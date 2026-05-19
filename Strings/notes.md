# Strings
### String Methods

There are many string methods which allow us to format strings. See some of the string methods in the following example: 
##### **capitalize():** Converts the first character of the string to capital letter
            challenge = 'thirty days of python'
            print(challenge.capitalize()) # 'Thirty days of python'
##### **count():** returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
            challenge = 'thirty days of python'
            print(challenge.count('y')) # 3
            print(challenge.count('y', 7, 14)) # 1, 
            print(challenge.count('th')) # 2`
##### **endswith():** Checks if a string ends with a specified ending
            challenge = 'thirty days of python'
            print(challenge.endswith('on'))   # True
            print(challenge.endswith('tion')) # False
##### **expandtabs():** Replaces tab character with spaces, default tab size is 8. It takes tab size argument
            challenge = 'thirty\tdays\tof\tpython'
            print(challenge.expandtabs())   # 'thirty  days    of      python'
            print(challenge.expandtabs(10)) # 'thirty    days      of        python'
##### **find():** Returns the index of the first occurrence of a substring from the left, if not found returns -1
            challenge = 'thirty days of python'
            print(challenge.find('y'))  # 5
            print(challenge.find('th')) # 0
##### **rfind():** Returns the index of the last occurrence of a substring from the right, if not found returns -1
            challenge = 'thirty days of python'
            print(challenge.rfind('y'))  # 16
            print(challenge.rfind('th')) # 17
##### **format():** formats string into a nicer output
            first_name = 'Asabeneh'
            last_name = 'Yetayeh'
            age = 250
            job = 'teacher'
            country = 'Finland'
            sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
            print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

            radius = 10
            pi = 3.14
            area = pi * radius ** 2
            result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
            print(result) # The area of a circle with radius 10 is 314
##### **index():** Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
            challenge = 'thirty days of python'
            sub_string = 'da'
            print(challenge.index(sub_string))  # 7
            print(challenge.index(sub_string, 9)) # error
##### **rindex():** Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
            challenge = 'thirty days of python'
            sub_string = 'da'
            print(challenge.rindex(sub_string))  # 7
            print(challenge.rindex(sub_string, 9)) # error
            print(challenge.rindex('on', 8)) # 19
##### **isalnum():** Checks alphanumeric character
            challenge = 'ThirtyDaysPython'
            print(challenge.isalnum()) # True

            challenge = '30DaysPython'
            print(challenge.isalnum()) # True

            challenge = 'thirty days of python'
            print(challenge.isalnum()) # False, space is not an alphanumeric character

            challenge = 'thirty days of python 2019'
            print(challenge.isalnum()) # False
##### **isalpha():** Checks if all string elements are alphabet characters (a-z and A-Z)
            challenge = 'thirty days of python'
            print(challenge.isalpha()) # False, space is once again excluded
            
            challenge = 'ThirtyDaysPython'
            print(challenge.isalpha()) # True

            num = '123'
            print(num.isalpha())      # False
##### **isdecimal():** Checks if all characters in a string are decimal (0-9)
            challenge = 'thirty days of python'
            print(challenge.isdecimal())  # False

            challenge = '123'
            print(challenge.isdecimal())  # True

            challenge = '\u00B2'
            print(challenge.isdigit())   # True 

            challenge = '12 3'
            print(challenge.isdecimal())  # False, space not allowed
##### **isdigit():** Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
            challenge = 'Thirty'
            print(challenge.isdigit()) # False
            
            challenge = '30'
            print(challenge.isdigit())   # True

            challenge = '\u00B2'
            print(challenge.isdigit())   # True
##### **isnumeric():**  Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
            num = '10'
            print(num.isnumeric()) # True
            
            num = '\u00BD' # ½
            print(num.isnumeric()) # True

            num = '10.5'
            print(num.isnumeric()) # False
##### **isidentifier():** Checks for a valid identifier - it checks if a string is a valid variable name
            challenge = '30DaysOfPython'
            print(challenge.isidentifier()) # False, because it starts with a number

            challenge = 'thirty_days_of_python'
            print(challenge.isidentifier()) # True
##### **islower():** Checks if all alphabet characters in the string are lowercase
            challenge = 'thirty days of python'
            print(challenge.islower()) # True

            challenge = 'Thirty days of python'
            print(challenge.islower()) # False
##### **isupper():** Checks if all alphabet characters in the string are uppercase
            challenge = 'thirty days of python'
            print(challenge.isupper()) #  False

            challenge = 'THIRTY DAYS OF PYTHON'
            print(challenge.isupper()) # True
##### **join():** Returns a concatenated string
            web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
            result = ' '.join(web_tech)
            print(result) # 'HTML CSS JavaScript React'
            
            web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
            result = '# '.join(web_tech)
            print(result) # 'HTML# CSS# JavaScript# React'
##### **strip():** Removes all given characters starting from the beginning and end of the string
            challenge = 'thirty days of pythoonnn'
            print(challenge.strip('noth')) # 'irty days of py'
##### **replace():** Replaces substring with a given string
            challenge = 'thirty days of python'
            print(challenge.replace('python', 'coding')) # 'thirty days of coding'
##### **split():** Splits the string, using given string or space as a separator
            challenge = 'thirty days of python'
            print(challenge.split()) # ['thirty', 'days', 'of', 'python']
            
            challenge = 'thirty, days, of, python'
            print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

##### **title():** Returns a title cased string
            challenge = 'thirty days of python'
            print(challenge.title()) # Thirty Days Of Python

##### **swapcase():** Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
            challenge = 'thirty days of python'
            print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
            
            challenge = 'Thirty Days Of Python'
            print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

##### **startswith():** Checks if String Starts with the Specified String
            challenge = 'thirty days of python'
            print(challenge.startswith('thirty')) # True

            challenge = '30 days of python'
            print(challenge.startswith('thirty')) # False


# Exercises 

##### 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
##### 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
##### 3. Declare a variable named company and assign it to an initial value "Coding For All".
##### 4. Print the variable company using print().
##### 5. Print the length of the company string using len() method and print().
##### 6. Change all the characters to uppercase letters using upper() method.
##### 7. Change all the characters to lowercase letters using lower() method.
##### 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
##### 9. Cut(slice) out the first word of Coding For All string.
##### 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
##### 11. Replace the word coding in the string 'Coding For All' to Python.
##### 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
##### 13. Split the string 'Coding For All' using space as the separator (split()) .
##### 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
##### 15. What is the character at index 0 in the string Coding For All.
##### 16. What is the last index of the string Coding For All.
##### 17. What character is at index 10 in "Coding For All" string.
##### 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
##### 19. Create an acronym or an abbreviation for the name 'Coding For All'.
##### 20. Use index to determine the position of the first occurrence of C in Coding For All.
##### 21. Use index to determine the position of the first occurrence of F in Coding For All.
##### 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
##### 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
##### 24.Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
##### 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
##### 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
##### 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
##### 28. Does 'Coding For All' start with a substring Coding?
##### 29. Does 'Coding For All' end with a substring coding?
##### 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
##### 31. Which one of the following variables return True when we use the method isidentifier(): 
            30DaysOfPython
            Thirty_days_of_python
##### 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
##### 33. Use the new line escape sequence to separate the following sentences.
            I am enjoying this challenge.
            I just wonder what is next.
##### 34. Use a tab escape sequence to write the following lines.
            Name      Age     Country   City
            Asabeneh  250     Finland   Helsinki
##### 35. Use the string formatting method to display the following:
            radius = 10
            area = 3.14 * radius ** 2
            The area of a circle with radius 10 is 314 meters square.
##### 36. Make the following using string formatting methods:
            8 + 6 = 14
            8 - 6 = 2
            8 * 6 = 48
            8 / 6 = 1.33
            8 % 6 = 2
            8 // 6 = 1
            8 ** 6 = 262144