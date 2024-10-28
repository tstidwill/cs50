def extract():
    user_input = input("File name: ").lower()
    extension = (user_input.partition(".")[2].strip())
    while "." in extension:
        extension = (extension.partition(".")[2].strip())
    return extension

def main():
    jpeg = ["jpg", "jpeg"]
    images = ["gif", "png"]
    application = ["zip", "pdf"]
    file_type = extract()

    if file_type in jpeg:
        print("image/jpeg")
    elif file_type in images:
        print("image/" + file_type)
    elif file_type in application:
        print("application/"+file_type)
    elif file_type == "txt":
        print("text/plain")
    else: print("application/octet-stream")

main()

