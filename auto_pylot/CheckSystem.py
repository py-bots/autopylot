import platform
import sys
import os

import auto_pylot.resources as data

user_name = os.getlogin()
windows_os = "windows"
linux_os = "linux"
mac_os = "darwin"
os_name = str(platform.system()).lower()
user_name = os.getlogin()
user_email = ""

python_version = str(sys.version_info.major) + "." + \
    str(sys.version_info.minor)
python_37 = "3.7"
python_38 = "3.8"
python_39 = "3.9"
python_310 = "3.10"
from auto_pylot import __version__

python_exe_path_ut = os.path.join(os.path.dirname(sys.executable), "python.exe")
pythonw_exe_path_ut = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")

python_exe_path = python_exe_path_ut.replace(" ", '" "')
pythonw_exe_path = pythonw_exe_path_ut.replace(" ", '" "')

data_folder = data.__path__[0]

# cf_icon_file_path = Path(os.path.join(data_folder, "Cloint-ICON.ico"))
# data_json_file = Path(os.path.join(data_folder, "data.json"))
# cf_icon_cdt_file_path = Path(os.path.join(data_folder, "Cloint-ICON-CDT.ico"))
# cf_logo_file_path = Path(os.path.join(data_folder, "Cloint-LOGO.PNG"))
# --------- Contribution Messages ---------

contribution_messages = ["We appreciate your contribution to a better tomorrow.", "Today's def (Python) creates tomorrow's software. Please contribute.", "A bug fix a day, keeps the Exceptions away. I'd be honored to have you as a contributor.",
                         "Contributors are the true givers of the modern age. Please make a contribution.", "Money can merely buy a server; contributors are the true wealth creators.", "Contributors are the backbone of Open Source Software. Please keep contributing."]


def _welcome_message():
    from pyfiglet import Figlet
    from rich.console import Console
    import datetime
    import random

    console = Console()
    """
    Internal Function to display welcome message & push a notification to ClointFusion Slack
    """

    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 16:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    messages_list = ['Where would I be without a friend like you?', 'I appreciate what you did.',
                     'Thank you for thinking of me.', 'Thank you for your time today.',
                     'I am so thankful for what you did here', 'I really appreciate your help. Thank you.',
                     "You know, if you're reading this, you're in the top 1% of smart people.",
                     'We know the world is full of choices. Yet you picked us, Thank you very much.',
                     'Thank you. We hope your experience was excellent and we can’t wait to see you again soon.',
                     'We hope you are happy with our tool, if not we are just an e-mail away at '
                     'support@pybots.ai. We will be pleased to hear from you.',
                     'Auto-Pylot would like to thank excellent users like you for your support. We couldn’t do it '
                     'without you!',
                     'Thank you for your business, your trust, and your confidence. It is our pleasure to work with '
                     'you.',
                     'We take pride in your business with us. Thank you!',
                     'It has been our pleasure to serve you, and we hope we see you again soon.',
                     'We value your trust and confidence in us and sincerely appreciate you!',
                     'Your satisfaction is our greatest concern!', 'Your confidence in us is greatly appreciated!',
                     'We are excited to serve you first!',
                     'Thank you for keeping us informed about how best to serve your needs. Together, we can make '
                     'this history.',
                     'Our brand innovation wouldn’t have been possible if you didn’t give us feedback about our '
                     'services.',
                     'Thank you so much for playing a pivotal role in our growth. We’ll make sure we continue to put '
                     'your needs first as our company expands and improves.',
                     'We are exceedingly pleased to find people we can always count on. Thank you for being one of '
                     'our loyal and trusted clients.', ]
    message = random.choice(messages_list)
    welcome_msg = f"\n{greeting} {str(user_name).title()} !  Welcome to Auto-Pylot {(__version__)}, Made in India with ❤️\n Python : {python_version}"
    print(welcome_msg)
    print()
    print(message)
    f = Figlet(font='small', width=150)
    console.print(f.renderText("Auto Pylot Community Edition"))


# check the system and return true if 64 bit, false if 32 bit
def is_supported():
    import struct
    import sys

    bit_size = struct.calcsize("P") * 8
    if bit_size == 32:
        print("We don't support 32-bit Architecture")
        print(
            "Please download 64-bit Architecture from the link down below. Press (ctrl + click) on link to download.\n")
        if os_name == "windows":
            print("https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe")
        if os_name == "darwin":
            print("https://www.python.org/ftp/python/3.9.7/python-3.9.7-macos11.pkg")
        sys.exit(0)
    else:
        return check_req()

def check_req():
    try:
        import pyaudio
    except ModuleNotFoundError:
        from auto_pylot.CrashHandler import install_pyaudio
        try:
            install_pyaudio()
        except Exception as e:
            return False
    try:
        scripts_verify()
    except Exception as ex:
        from auto_pylot.CrashHandler import report_error
        report_error(ex)
        return False
    
    return True

def scripts_verify():
    import subprocess
    Scripts_Path = os.path.join(sys.exec_prefix, "Scripts")
    user_path = (str(subprocess.run(
        ["powershell", "-Command", "[Environment]::GetEnvironmentVariable('Path','User')"], capture_output=True).stdout.decode('ascii')).replace(
        ';;', ';')).replace('\r\n', '')
    if Scripts_Path.lower() not in user_path.lower():
        user_path = user_path + ';' + Scripts_Path + ';' + '\r\n'
        subprocess.call('setx path "{}"'.format(user_path),
                        shell=True, stdout=subprocess.PIPE)
        print("Scripts Path Updated. We recommend you to restart your system for the changes to take effect.")

if os_name == windows_os:
    if not sys.argv[0].endswith(('ap_py.exe',)):
        # Add cli's here to skip the welcome msg twice
        _welcome_message()
else:
    sys.exit()

