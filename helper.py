# to_seconds = 24 * 60 * 60
# name_of_unt = "sekundes"


def days_to_units(num_of_days, convertion_unit):
    if convertion_unit == "stundas":
    #if num_of_days > 0:
        return f"{num_of_days} dienās ir {num_of_days * 24} stundas"
    elif convertion_unit == "minūtes":
        return f"{num_of_days} dienās ir {num_of_days * 24 * 60} minūtes"
    elif convertion_unit == "sekundes":
        return f"{num_of_days} dienās ir {num_of_days * 24 * 60 * 60} sekundes"
    else:
        return "Neatbalstām šādu mērvienību"
    #elif num_of_days == 0:
        #return "Nu nezinu vai 0 būs īstais cipariņš"
    # else:
    #     return "Tas nav pozitīvs cipariņš"

def validate_and_execute(days_and_unit_dictionary):
    try:
    #if user_input.isdigit():
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
           print("Nu nezinu vai 0 būs īstais cipariņš")
        else:
            print("Tas nav drīgs cipars vipār, vai tas nebūs negatīvs cipars?")
    except ValueError:
        print("Tas nav drīgs cipars vipār, vai tas nebūs kaut kas cits?")

#my_var = days_to_units(20)
#print(my_var)
# print("20 dienās ir " + str(20 * to_seconds ) + " sekundes")
# print(f"35 dienās ir {35*to_seconds} {name_of_unt}")
# print(f"50 dienās ir {50*to_seconds} sekundes")
# print(f"110 dienās ir {110*to_seconds} sekundes")

# def scope_check(num_of_days):
#     print(name_of_unt)
#     print(num_of_days)


# days_to_units(20, "Cool")
# days_to_units(35, "Cool")
# days_to_units(50, "Cool")
# days_to_units(110, "Cool")
# scope_check(20)
