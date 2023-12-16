with open("./Input/Names/invited_names.txt", mode="r") as file:
    name_list = file.readlines()
    new_list = []
    for name in name_list:
        cleaned_name = name.strip("\n")
        new_list.append(cleaned_name)

    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        lett = letter.read()
        for name in new_list:
            new_cont = lett.replace("[name]", name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
                new_letter.write(new_cont)
