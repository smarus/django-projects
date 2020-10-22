
# write your code here
dictionary = dict()
with open('users.json','r') as file:
     dictionary = json.load(file)
     print(len(dictionary.get('users')))

