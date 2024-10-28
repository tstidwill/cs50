def convert(str):
    if ":)" in str:
        str = str.replace(":)", "🙂")
    if ":(" in str:
        str = str.replace(":(", "🙁")
    return str

def main():
    user_input= input("Enter a string:" )
    return convert(user_input)

print(main())
