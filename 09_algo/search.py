def search_email (email_list, search_email):
    found = False
    for email in email_list:
        if email== search_email:
            found= True
            break

    if found:
        print("You find email")
    else:
        print("You don't find email")

emais=["123@gmail.com", "234@gmail.com"]