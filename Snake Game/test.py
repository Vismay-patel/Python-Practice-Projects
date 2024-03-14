def save():
    with open("data.txt", "r") as file:
        return file.read()
    
print(int(save()))