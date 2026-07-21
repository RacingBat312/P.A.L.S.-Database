import itertools
import string

characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase

target_file = input("\nEnter target Python file name (or full path): ").strip()
min_length = int(input("\nEnter password min length: "))
max_length = int(input("Enter password max length: "))

if min_length > max_length or min_length <= 0:
    print("Invalid range. min must be ≤ max and > 0")
else:
    # Open target file in VS Code using proper subprocess syntax
    print(f"\nOpening {target_file} in VS Code...")
      
    count = 0
    print(f"Writing passwords to: {target_file}\n")

    with open(target_file, "a", encoding="utf-8") as f:
        for length in range(min_length, max_length + 1):
            for combo in itertools.product(characters, repeat=length):
                password = ''.join(combo)
                print(f"[{count+1}] {password}")
                f.write(password + "\n")
                f.flush()
                count += 1

    print(f"\n{'='*50}")
    print(f"Total passwords generated: {count}")
    print(f"Written to: {target_file}")
    print(f"{'='*50}")