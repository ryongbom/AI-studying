# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.
people_0 = {'first_name': 'Kim', 'last_name': 'Yong Chol', 'age': 21, 'city': 'pyongyang'}
people_1 = {'first_name': 'Kang', 'last_name': 'Ji Yon', 'age': 20, 'city': 'hamhung'}
people_2 = {'first_name': 'So', 'last_name': 'Ta Gwon', 'age': 18, 'city': 'pyongsong'}

peoples = [people_0, people_1, people_2]

for people in peoples:
    for key, value in people.items():
        print(f"{key}: {value}")