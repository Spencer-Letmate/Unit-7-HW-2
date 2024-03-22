from pathlib import Path


# Excercise 1
path = Path("guest_book.txt")
names = ""
while True:
    namef = input("What is your first name?: ")
    if namef.lower() == "exit":
        break
    namel = input("What is your last name?: ")
    if namel.lower() == "exit":
        break
    full = namef.title().strip() + " " + namel.title().strip()
    names += full + "\n"

path.write_text(names)

# Excercise 2
class_test_data={
        "Billy Bot":{"Test 1":95,"Test 2":90,"Test 3":87},
        "Samantha Smith":{"Test 1":85,"Test 2":88,"Test 3":91},
        "John Doe":{"Test 1":78,"Test 2":82,"Test 3":79},
        "Emily Jones":{"Test 1":92,"Test 2":95,"Test 3":96},
        "Michael Brown":{"Test 1":88,"Test 2":84,"Test 3":90}
}

def grade_book_creator(dict):
    for i in dict:
        newpath = Path(f"{i}.txt")
        text = f"Name: {i}"
        for x in dict[i]:
            text += f"\n{x}: {dict[i][x]}"
        newpath.write_text(text)

grade_book_creator(class_test_data)