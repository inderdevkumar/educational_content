with open("/home/inder/my_data/educational_content/python_projects/interview_programs/all_questions/python/file_operation/read_file_input.txt", "r") as file:

    content= file.read()

print(content)

list1= content.split()
dict1= {}
print(list1)
for item in list1:

    if item in dict1.keys():
        dict1[item]= dict1[item]+ 1
    
    else:
        dict1[item]= 1

for key, value in dict1.items():
    if value > 1:
        print(f"{key}-> {value}")

