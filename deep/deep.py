def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything?")
    if user_input.lower().strip() in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")
main()
