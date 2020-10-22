vowels = 'aeiou'
# create your list here
word = input()
new_list = [x for x in word if x in vowels]
print(new_list)