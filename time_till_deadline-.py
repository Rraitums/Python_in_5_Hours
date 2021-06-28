from datetime import datetime

user_input = input("Ievadi savu mērķi un tā sasniegšanas datumu, atdalot tos ar kolu ':' \n")
input_list = user_input.split(":")
goal = input_list[0]
end_date = input_list[1]

end_date_date = datetime.strptime(end_date, "%d.%m.%Y")
# aprēķināt cik dienas no šodienas ir līdz beigu termiņam

today_date = datetime.today()
time_till = end_date_date - today_date

print(f"Sveiki! Lai saniegtu savu mērķi: {goal} ir atlikušas {time_till.days} dienas")