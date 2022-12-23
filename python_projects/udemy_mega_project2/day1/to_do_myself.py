

print("====== Program to create Advanced To-do =============")

from datetime import datetime


while 1:
    user_choice= input("Enter add, show, update or delete or clear_all to get affected: ")
    #print("You enetered: ", user_choice)


    if user_choice == "add":
        try:
            now = datetime.now()
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open("to_do.txt", "r") as file_object_read:
                content= file_object_read.readlines()
                last_string= content[-1]
                list_of_words=  last_string.split()
                serial_number_with_dot= list_of_words[0]
                serial_no= serial_number_with_dot[:-1]

            with open("to_do.txt", "a+") as file_object_append:
                new_serial= int(serial_no) + 1
                add_input= input("Enter to do item to add into your list: ")
                file_object_append.write(str(new_serial) + ".  " + add_input + " " + dt_string + "\n" )

        except IndexError:
            print("There is no data in text file")
            with open("to_do.txt", "a+") as file_object_append:
                new_serial= 1
                add_input= input("Enter to do item to add into your list: ")
                file_object_append.write(str(new_serial) + ".  " + add_input + " " + dt_string + "\n" )

    elif user_choice == "show":
        with open("to_do.txt", "r") as file_object:
            content= file_object.readlines()
            print("***** To do items are as below ***************\n\n")
            for item in content:
                print(item[:-1])  #Removing \n (last chracter) from string
            print("\n\n******************************************\n\n")
            

    elif user_choice == "update":
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")        
        
        with open("to_do.txt", "r+") as file_object:
            content= file_object.readlines()
            enter_index= int(input("Enter the todo number u want to edit: "))

            if (enter_index > len(content)):
                print(f"Your entered index: {enter_index} which is > than length of your to do list: {len(content)}")
                print("Please recheck your to do items using show option. EXiting Now!! ")
                exit()

            else:
                enter_sentence= input("Enter the new to do item u like to update with: ")
                string_selected_is= content[enter_index-1]
                string_remove_last_char= string_selected_is[:-1]
             
                list_of_words=  string_remove_last_char.split()
            
                list_of_words_without_first_word= list_of_words[1:]    

                list_to_str= " ".join(item for item in list_of_words_without_first_word)
            
                new_sentence= enter_sentence + " " + dt_string
                new_content= [item.replace(list_to_str, new_sentence) for item in content]
            
                new_content_list_to_str= "".join(item for item in new_content)
                file_object.seek(0)
                file_object.truncate(0)
                file_object.write(new_content_list_to_str) #Writing expect only string

    elif user_choice == "delete":
        
        with open("to_do.txt", "r+") as file_object:
            content= file_object.readlines()
            enter_index= int(input("Enter the todo number u want to delete: "))
            
            if (enter_index > (len(content))):
                print(f"Your entered index: {enter_index} which is > than length of your to do list: {len(content)}")
                print("Please recheck your to do items using show option. EXiting Now!! ")
                exit()

            else:
                content.pop(enter_index-1)
            
                list_of_items_before_entered_index= content[:enter_index-1]
            
                list_of_items_after_entered_index= content[enter_index-1:]
            
                modified_serial_no_after_entered_index= [ str(int("".join(element for element in item.split()[0][:-1]))-1)+"."+ "  " + (" ".join(element for element in item.split()[1:])) + "\n"  for item in list_of_items_after_entered_index]
            
                adding_list_for_both_side_of_entered_index= list_of_items_before_entered_index + modified_serial_no_after_entered_index

                new_content_list_to_str= "".join(item for item in adding_list_for_both_side_of_entered_index)
            
                file_object.seek(0)
                file_object.truncate(0)
                file_object.write(new_content_list_to_str) #Writing expect only string

    elif user_choice == "clear_all":
        print("\n\n****** It will Reset your all to do items ************\n\n")
        user_input= input("Enter y to clear everthing else n: ")
        if (user_input == "y"):

            with open("to_do.txt", "w+") as file_object:
                content= file_object.readlines()
                file_object.seek(0)
                file_object.truncate()

        else:
            print("\n\nYou selected not to clear\n\n")
            
    else:
        print("===== You selected wrong choice ==========\n\n")
        exit()
