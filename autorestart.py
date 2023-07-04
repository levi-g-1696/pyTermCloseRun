from subprocess import run
from time import sleep

# Path and name to the script you are trying to start
file_path = "test.py"

restart_timer = 2
def start_script():
    try:
        # Make sure 'python' command is available
       # run("python "+file_path, check=True)
       run (r"notepad 'C:\Users\office22\Desktop\zmani\1212.txt'")
    except:
        # Script crashed, lets restart it!
        handle_crash()

def handle_crash():
    sleep(restart_timer)  # Restarts the script after 2 seconds
    start_script()

start_script()

######  test.py  ##########
#
# from time import sleep
# while True:
#     sleep(1)
#     print("Hello")
#     raise Exception("Hello exception")