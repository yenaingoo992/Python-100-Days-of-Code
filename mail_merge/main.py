def get_letter_template():
    with open("./input/letters/starting_letter.txt") as letter:
        return letter.read()

def get_invited_names():
    with open("./input/names/invited_names.txt") as names:
        return names.readlines()

def prepare_invitation_letter(name):
    template = get_letter_template()
    letter = template.replace("[name]", name)
    return letter

def write_invitation_letter(to, letter):
    with open(f"./output/readytosend/letter_to_{to}", mode="w") as file:
        file.write(letter)

for invited in get_invited_names():
    stripped_name = invited.strip()
    invitation_letter = prepare_invitation_letter(stripped_name)
    write_invitation_letter(to=stripped_name, letter=invitation_letter)