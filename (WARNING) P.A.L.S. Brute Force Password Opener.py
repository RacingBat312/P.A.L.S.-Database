import itertools
import string
import time

def brute_force(length = 4):
    chars = string.ascii_lowercase + string.digits + string.digits
    attempts = 0
    s_time = time.time()

    for password_length in range(1, length + 1):
        for guess in itertools.product(chars, repeat = password_length):
            attempts += 1
            guess = ''.join(guess)
            print(f"Trying: {guess}")

        
        if guess == real_password:
            e_time = time.time()
            return True, guess, attempts, e_time - s_time
        
    return False, None, attempts, time.time() - s_time

real_password = "f45"

success, password, attempts, time_takes = brute_force(3)

if success:
    print(f"\nPassword found : {password}")
    print(f"Total attempts : {attempts}")
    print(f"Time taken : {time_takes}")

else:
    print("Password not found")


