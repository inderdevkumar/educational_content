import requests
import json
import jsonpath


def test_post():
    url= "https://thetestingworldapi.com/Help/Api/GET-api-studentsDetails"

    with open("/home/inder/my_data/educational_content/python_projects/api_testing/api_automation/for_pytest_use/testcases/my_json.json", "r") as file:
        file_read= file.read()

    in_json= json.loads(file_read)
    response= requests.post(url, in_json)
    print(response)
    
    # ===
    json_response= response.json()
    my_id= jsonpath.jsonpath(json_response, "id")
    print(my_id)
