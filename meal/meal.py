def main():
    user_input = input("What time is it? ")

    if "a.m." in user_input:
        time_extract = (user_input.partition(" ")[0])
        time = convert(time_extract)
    elif "p.m." in user_input:
        time_extract = (user_input.partition(" ")[0])
        time = convert(time_extract) + 12
    else:
        time = convert(user_input)

    if 7.00 <= time <= 8.00:
            print("breakfast time")
    elif 12.00 <= time <= 13.00:
            print("lunch time")
    elif 18.00 <= time <=19.00:
            print("dinner time")


def convert(time):
    hour = float((time.partition(":")[0]))
    minutes = float((time.partition(":")[2]))/60
    converted = hour + minutes
    return(converted)



if __name__ == "__main__":
    main()


