import sys
def ascii_to_binary(char):
    if len(char) != 1:
        return "Please enter a single ASCII character."
    if ord(char) < 0 or ord(char) > 127:
        return "Invalid ASCII character."
    binary = bin(ord(char))[2:].zfill(8)
    return binary

while True:
    try:
        char = input("Enter an ASCII character ('exit' to quit): ")
        if char == 'exit':
            break
        else:
            print(ascii_to_binary(char))
    except (EOFError, KeyboardInterrupt, TypeError, ValueError, NameError, UnicodeDecodeError) as e:
        print(f"An error occurred: {str(e)}. Please try again.")
        continue

print("Goodbye!")
