"""
    3. WAP to remove all characters from a string except alphabets and digits
"""
input_str = "Hello! Welcome to 2025!"
output_str = ""
for ch in input_str:
    if ch.isalnum():
        output_str += ch
print(output_str)