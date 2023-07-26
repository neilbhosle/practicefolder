# with open("write.txt", 'a') as file:
#     file.write("\nHere's new line")

with open("emails.txt",'r') as emails:

    for email in emails:
        if "gmail" in email:
            print(email.rstrip().rsplit())


