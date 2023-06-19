# ========== BDD with behave framework =============

Link followed: https://www.youtube.com/watch?v=JIyvAFBx2Fw&t=2s

behaviour means how feature of sw operates. It is defines as a scenario of inputs, actions and outcomes. A product has countless behaviour.

Behaviour  driven development is an agile software development technique that encourages callobaration
between developers, QA, non-technical or business participant in software project.
Everyone can easily understand the framework workflow, but in other frameworks only technical person can understand.

why BDD?
better collaboration and better test automation.
1. Everyone can contribute, not just programmers
2. Do things properly from the start
3. Step reuse

book to flow: BDD in action by John Ferguson Smart

I BDD, we write first testcases which is in Gherkin. This helps to write best test code

# ========== Behave ====== ========================================

Just like we have cucumber for java, we have behave for python.
It operates on diff directories, which mainly contains feature files  and step definations

Feature files contains diff scenarios which we have to automate for our app. It is very simple and easy to read and understand as its mainly 
in english lang. We are using certain keywords, in order to write it and they are known as Gherkin keywords. 

Step defination-> Once feature is written, we have to implement them using for each step for scenarios written in feature file.

# =========== BDD Scenarios and Feature files in Gherkin ================


We have to focus in three components in BDD approach: 
1. Feature file-> One app can have multiple feature files and each feature files can have multiple scenarios. Extension is file_name.feature
2. scenario -> Each scenario has multiple steps to be performed
3. step defination -> This is done using python codes. For evry steps in scenarios, we have to make step defination/method using python

syntax for Gherkin: Indentation is very imp

Feature: feature name

	Scenario: title/short description
  		Given [A Precondition ie initail state]
  		When [Some event ie when action is taken]
  		Then [Some outcome ie when verify outcome]



Example: 1 feature file having multiple scenios and each scenarios having multiple steps
Feature: Orange HRM Login ie. name of the feature

	Scenario: Logo presence in OrangeHRM Home page
		Given I launch chrome browser
		When I open orange hrm homepage
		Then I verify logo present in the home page

	Scenario: Login to OrangeHRM
		Given I launch chrome browser
		When I open the orange hrm homepage
		And Enter un and pass
		And click on login button
		Then User must be login sucessfully


# ====================== BDD implemetation requirement ================================================
1. install python
2. IDE-> Pycharm
3. Selenium library-> As i like to automate Web App
4. Behave-> for writing Gherkin

# =========================== Process for begineers before writing step defination using py=====================

Create feature file and than execute it using: (venv) E:\inder_dont_delete>behave utilities_python\Capge\framework_selenium_test\features\orange_hrm.feature

It will give u implemented step defination in python format like below:

You can implement step definitions for undefined steps with these snippets:

@given(u'I launch chrome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I launch chrome browser')


@when(u'I open orange hrm homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I open orange hrm homepage')


@then(u'I verify logo present in the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I verify logo present in the home page')


@then(u'close the browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close the browser')

============= how to run =========================================


and after wrting step defination.
 Run the feature file like before>  (venv) E:\inder_dont_delete>behave utilities_python\Capge\framework_selenium_test\features\orange_hrm.feature

If u like to debug and print something in console use --no-capture like below:
 (venv) E:\inder_dont_delete>behave utilities_python\Capge\framework_selenium_test\features\orange_hrm_login.feature --no-capture

in case u like to run all feature files, just give feature directory: behave utilities_python\Capge\framework_selenium_test\features

And if u like have to reports for all features than: behave -f allure_behave.formatter:AllureFormatter -o reports\ features\   # reports is the folder path for reports and features folder

	above reports are generated in json format. To convert into html: allure serve reports\
and after running here is the result:

(venv) E:\inder_dont_delete>behave utilities_python\Capge\framework_selenium_test\features\orange_hrm.feature
Feature: Orange HRM Login ie. name of the feature # utilities_python/Capge/framework_selenium_test/features/orange_hrm.feature:1

  Scenario: Logo presence in OrangeHRM Home page  # utilities_python/Capge/framework_selenium_test/features/orange_hrm.feature:2
    Given I launch chrome browser                 # utilities_python/Capge/framework_selenium_test/features/steps/orange_verify_logo.py:8

DevTools listening on ws://127.0.0.1:63082/devtools/browser/bfb76ed8-67bb-4152-b181-cdec17913bef
    When I open orange hrm homepage               # utilities_python/Capge/framework_selenium_test/features/steps/orange_verify_logo.py:15
    Then I verify logo present in the home page   # utilities_python/Capge/framework_selenium_test/features/steps/orange_verify_logo.py:21
    And close the browser                         # utilities_python/Capge/framework_selenium_test/features/steps/orange_verify_logo.py:30

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
4 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m19.759s

====================  adding paramets to feature file ===================================================
VVI-> If any feature file has duplicate steps, than just need to write 1 step defination.
For example: lets say we 2 feature files and each feature file we have different scenarios but if any steps of them is identical(ie. if Given I launch chrome browser is found in feature 1
 and Given I launch chrome browser also found in feature 2, than we dont have to write 2 diff step definations.)

they have to be in double quaotes like below:
Feature: Orange HRM Login ie. name of the feature
	Scenario: Login to OrangeHRM
		Given I launch chrome browser
		When I open the orange hrm homepage
		And Enter un "admin" and pass "admin123"
		And click on login button
		Then User must be login sucessfully


=====================Scenario vs Scenario oputline ================================================
Scenario-> only one time execute
Scenario outline-> Will execute same scenario as many times, examples are given. This is Data Driven test

for example:

Feature: Orange HRM Login ie. name of the feature
	Scenario: Login to OrangeHRM
		Given I launch chrome browser
		When I open the orange hrm homepage
		And Enter un "admin" and pass "admin123"
		And click on login button
		Then User must be login sucessfully

	Scenario Outline: Login to OrangeHRM with multiple parameters
		Given I launch chrome browser
		When I open the orange hrm homepage
		And Enter un "<username>" and pass "<password>"
		And click on login button
		Then User must be login sucessfully

		Examples:
			| username | password |
			| admin    | admin123 |
			| admin2   | admin123 |
			| admin3   | admin123 |
			| admin4   | admin123 |
			| admin5   | admin123 |


==================== Background keyword use =============================================

As observed, we have multiple steps repeated in each scenarios. So, to make feature file more simpler and clean, background keyword is used.
Everysteps of background keyword will be exceuted first for each scenario. For example:

Feature: Orange HRM Login
	Scenario: Login to OrangeHRM
		Given I launch chrome browser
		When I open the orange hrm homepage
		And Enter un "admin" and pass "admin123"
		And click on login button
		Then User must be login to dashboard page

	Scenario: Serarch user
		Given I launch chrome browser
		When I open the orange hrm homepage
		And Enter un "admin" and pass "admin123"
		And click on login button
		When navigate to search page
		Then Search page sghould display

	Scenario: Advanced Serarch user
		Given I launch chrome browser
		When I open the orange hrm homepage
		And Enter un "admin" and pass "admin123"
		And click on login button
		When navigate to advanced search page
		Then advanced Search page sghould display

here, we can see 1st four steps of each scenario is repaeted. In such case we can use background keyword like below:

Feature: Orange HRM Login

	Background: Common steps running before each scenarios
		Given I launch chrome browser
		When I open the orange hrm homepage
		And Enter un "admin" and pass "admin123"
		And click on login button

	Scenario: Login to OrangeHRM
		Then User must be login to dashboard page

	Scenario: Serarch user
		When navigate to search page
		Then Search page sghould display

	Scenario: Advanced Serarch user
		When navigate to advanced search page
		Then advanced Search page sghould display


# ==================================== BDD with pytest framework =============================================================
 ===========================================================================================================
imp note: always create python package and not a directory, if u like to have py file inside it

book to learn more on pytest:
python testing with pytest by Brian Okken
pytest quick start guide by Bruno Olivertia

reason to choose pytest-bdd->>>>>  Its plugin for pytest, which is the best framework in  python. It comes with other plugin as well,
 html report, prallel execution.

to check all modules listed: pip list


we use pytest_bdd here and can be installed using: pip install pytest-bdd

basic workflow should be simmilar as above:

link to follow:  https://github.com/ashikkumar23/gherkin-bdd-api-test-framework
	https://github.com/AutomationPanda/tau-pytest-bdd/blob/master/tests/features/cucumbers.feature
	https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/
official doc: https://pytest-bdd.readthedocs.io/en/latest/

bdd-gherkin-test-automation-framework/
├─ .github/
│  ├─ workflows/
│  │  ├─ ci.yml
├─ tests/
│  ├─ data/
│  │  ├─ post_payload_1.json
│  │  ├─ post_payload_2.json
│  │  ├─ put_payload_1.json
│  │  ├─ put_payload_2.json
│  ├─ features/
│  │  ├─ sample.feature
│  ├─ lib/
│  │  ├─ terminal_report.py
│  ├─ step_definitions/
│  │  ├─ test_assertions.py
│  │  ├─ test_common.py
│  │  ├─ test_sample.py
│  ├─ utils/
│  │  ├─ __init__.py
│  │  ├─ custom_exceptions.py
│  │  ├─ logger_config.py
│  │  ├─ utils.py
│  ├─ .env
│  ├─ .gitignore
│  ├─ conftest.py
│  ├─ pytest.ini
│  ├─ requirements.txt
├─ LICENSE
├─ README.md


Both behave bdd and pytest bdd looks similar

In order to autogenerate step defination, run below command with generate(Pytest-BDD generate <Feature File Path>> <PY File Path>): 
(venv) E:\inder_dont_delete\utilities_python\Capge\framework_selenium_test\pytest_bdd>Pytest-BDD generate type_2\features\cucumbers.feature

and execution is done like normal pytest: (venv) E:\inder_dont_delete\utilities_python\Capge\framework_selenium_test\pytest_bdd>pytest -vs test_withdrawl.py

 pytest-bdd from writing feature files to step definitions, to tag filtering, and everything in between.



# ======= Prameterizing ====================================

in Gherkin file same synatx: inside ""
but in step defination, requires additional parsers module

like in step def
@given(parsers.cfparse('The basket has "{initail:Number}" cucumbers'))

and in feature:
Given The basket has "2" cucumbers


# ========== Scenario Outlines =====================

same as behave. Only diff is, we can do parameterization in stepd def also using pytest.mark.parameterize.

Recommeneded way is to way parameterize only in Gherking feature file and not in py file.


# ===========  Background ===================================
similar to behave bdd

# ============= add tags in feature file =================

feature level tage-> If it is present, than scenarios under it will also have that tag as they inherited
scenario level tag

and to run them, use tag like:

pytest -k  "1st_tag name"
or
pytest -k  "1st_tag name and 2nd_tag_name"
or
pytest -k  "not 1st_tag name"
or
pytest -m tag_name_or_marker

and many more tags


In our case go to step def folder and than run : pytest -k "duckduckgo"

