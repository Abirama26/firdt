
import random 
import array
print("Hello folks")
print("This is a password generator")
max_len=15
numbers=['0','1','2','3','4','5','6','7','8','9']
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
sym = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
group_every = numbers + low + up + sym
rand_numbers = random.choice(numbers)
rand_up = random.choice(up)
rand_low = random.choice(low)
rand_sym = random.choice(sym)
preview_word = rand_numbers + rand_up + rand_low + rand_sym
for x in range(max_len - 1):
    preview_word = preview_word + random.choice(group_every)
    preview_word_list = array.array('u', preview_word)
    random.shuffle(preview_word_list)
password=""
for x in preview_word_list:
        password = password + x
print("This is your password-"password)
