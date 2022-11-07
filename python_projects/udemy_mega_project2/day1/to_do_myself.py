print("== Todo ==")
#all_entries = []

a=0
while 1:
    user_choice= input("Enter add, show, update or delete to get affected: ")
    print("You enetered: ", user_choice)
    
    with open("to_do.txt", "a+") as file_object:


        if user_choice == "add":
            a += 1
            add_input= input("Enter input to add: ")
            file_object.write(str(a) + ".  " + add_input + "\n" )
        #all_entries.append(add_input)

        elif user_choice == "show":
            content= file_object.readlines()
            print(content)

        elif user_choice == "update":
            #print(all_entries)
            enter_index= int(input("Enter the position u want to edit: "))
            enter_sentence= input("Enter the sentence u like to update with: ")
            all_entries[enter_index] = enter_sentence 

            #print(all_entries)

        elif user_choice == "delete":
            #print(all_entries)
            enter_index= int(input("Enter the position u want to delete: "))
        
            all_entries.remove[enter_index]

            #print(all_entries)

        else:
            exit()
