
# Variables in Python
# no declaration of types
first_name = 'Elliot'
last_name = 'Park '
country = 'USA'
city = 'Irvine'
age = 32
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Elliot2',
    'lastname':'Park2',
    'country':'Korea',
    'city':'Seoul'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Elliot3', 'Park3', 'Denpasar', 32, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)