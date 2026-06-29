language = input("Do you Master Python Y/N : ").strip().capitalize()

if language == "N": print("Sorry! You aren't Qualified enough for this Job")

else :

    Exeperiense = int(input("Enter your Years of Exeperiense or Projects You worked on : "))
    Certificate = input("Do you have a Certificate or Complete a Bootcamb? Y/N : ").strip().capitalize()

    if Exeperiense >= 2 or Certificate == "Y":
        print("Congratulations! You are Moved to the Next Step for Interview")
    else:
        print("Sorry! You aren't Qualified enough for this Job")
