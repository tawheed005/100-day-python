def calculate_love_score(name1,name2):
    first_check = "true"
    second_check = "love"
    
    first_name_count = ""
    
    for letters in name1:
        if letters in first_check:
            first_name_count += letters
        if letters in second_check:
            first_name_count += letters
    lenght_of_1st_name = (len(first_name_count))

    second_name_count = ""

    for letters in name2:
        if letters in first_check:
            second_name_count += letters
        if letters in second_check:
            second_name_count += letters
    length_of_2nd_name  = len((second_name_count))
        
    love_score = str(lenght_of_1st_name) + str(length_of_2nd_name)

    print(love_score)
    
calculate_love_score("Kanye West", "Kim Kardashian")