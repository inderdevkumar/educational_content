"""
link to follow: https://www.youtube.com/watch?v=R4E4IOIC63s
                https://betterprogramming.pub/use-pywinauto-to-automate-programs-in-windows-7d4a7eb082a5
1. Import
2. Start the app
3. connect the app
4. start automating:  using control identifiers
"""
import time
from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard

# start the app
app = Application(backend= "uia").start("Notepad.exe") # Give full path for other app ->  win32

# connect the app with title as it is in the app and timeout(this is similar to implict wait in selenium)
app = Application(backend= "uia").connect(title= "Untitled - Notepad", timeout= 20)


# You need to identify the available windows of your process:
print("windows are : ",app.windows())

dlg = app['Untitled - Notepad']
# get control identifiers
# print(dlg.print_control_identifiers())  # This is very useful, will be diff for diff windows

def write_in_editor():
    # Simulated using keyword
    text_to_write= "Boston Scientific module number 2 is pywinauto"
    #dlg.set_focus()
    dlg.type_keys(text_to_write, with_spaces=True)
    #keyboard.send_keys(text_to_write, with_spaces= True)


def open_new_file_Save_as():
    # using control identifiers
    # child_window(title="File", control_type="MenuItem") -> copy as it is from control identifiers
    dlg = app['*Boston Scientific module number 2 i - Notepad']  # Its little unique in notepad of win11. This you will get once u have error
    """
    Could not find 'Untitled - Notepad' in 'dict_keys([' * Boston Scientific module number 2 i - Notepad', '
    Dialog',
     ' * Boston Scientific module number 2 i - NotepadDialog'
     ])'
    """
    dlg.maximize()
    click_file= dlg.child_window(title="File", control_type="MenuItem").wrapper_object()
    click_file.click_input()

    click_save_as= dlg.child_window(title="Save as", control_type="MenuItem").wrapper_object()
    click_save_as.click_input()

    file_name= dlg.child_window(title="Save as", auto_id="TextBlock", control_type="Text").wrapper_object()
    file_name.send_keys("test123.txt")
    #print(dlg.print_control_identifiers())

def close_notepad_without_saving():
    pass

time.sleep(3)
write_in_editor()
open_new_file_Save_as()
