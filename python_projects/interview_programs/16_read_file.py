
with open("file_operation/read_file_input.txt", "r") as file:
    content_string= file.read()
    content_list= file.readlines()
print("1st way: ", content_string)
print("2nd way: ", content_list)
