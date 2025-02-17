def string_check():
    string = input("👉 Type an alphabetic string, quick! ")
    new_str = string[::-1]
    
    if new_str == string:
        print("😲 WOW! That’s a palindrome! You’re officially a palindrome master! 🎉")
        return True
    else:
        print("😢 Oof! Not a palindrome. Try again, buddy!")
        return False

# Run the function until a palindrome is entered
while not string_check():
    print("🤔 Give it another shot...")

print("🥳 Finally! You cracked the palindrome code!")
