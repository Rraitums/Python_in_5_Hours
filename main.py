from helper import validate_and_execute
user_input = ""

while user_input != "exit":
    user_input = input("Ievadi dienu skaitu un parametru uz kuru pārveidot. Šādā formā: (dienu skaits:sekundes/minūtes/stundas) \n")
    days_and_unit = user_input.split(":")
    # print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    # print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)
