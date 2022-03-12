from auto_pylot.CheckSystem import os_name
from importlib import import_module

Platform = os_name.title()

mouse = import_module(f'auto_pylot.{Platform}.functions.mouse')
keyboard = import_module(f'auto_pylot.{Platform}.functions.keyboard')
voice = import_module(f'auto_pylot.{Platform}.functions.voice')
chrome = import_module(f'auto_pylot.{Platform}.functions.chrome')
folder = import_module(f'auto_pylot.{Platform}.functions.folder')
string = import_module(f'auto_pylot.{Platform}.functions.string')
windows = import_module(f'auto_pylot.{Platform}.functions.windows')
screen_scraping = import_module(
    f'auto_pylot.{Platform}.functions.screen_scraping')
extras = import_module(f'auto_pylot.{Platform}.functions.extras')


# ---------  Mouse Functions ---------


def mouse_click(x='5', y='5', left_or_right="left", no_of_clicks=1):
    """Clicks at the given X Y Co-ordinates on the screen using single / double / triple click(s). Default clicks on current position.
    Args:
        x (int): x-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        y (int): y-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        left_or_right (str, optional): Which mouse button.
        Eg: right or left, Defaults: left.
        no_of_click (int, optional): Number of times specified mouse button to be clicked.
        Eg: 1 or 2, Max 3. Defaults: 1.
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return mouse.Mouse.mouse_click(x, y, left_or_right, no_of_clicks)


def mouse_move(x="5", y="5"):
    """Moves the cursor to the given X Y Co-ordinates.
    Args:
        x (int): x-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        y (int): y-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return mouse.Mouse.mouse_move(x, y)


def mouse_drag_from_to(x1="5", y1="5", x2="10", y2="10", delay=0.5):
    """Clicks and drags from x1 y1 co-ordinates to x2 y2 Co-ordinates on the screen
    Args:
        x1 or x2 (int): x-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        y1 or y2 (int): y-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        delay (float, optional): Seconds to wait while performing action. 
        Eg: 1 or 0.5, Defaults to 0.5.
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return mouse.Mouse.mouse_drag_from_to(x1, y1, x2, y2)


def mouse_search_snip_return_coordinates_x_y(img="", wait=180):
    """Searches the given image on the screen and returns its center of X Y co-ordinates.
    Args:
        img (str, optional): Path of the image. 
        Eg: D:\Files\Image.png, Defaults to "".
        wait (int, optional): Time you want to wait while program searches for image repeatably.
        Eg: 10 or 100 Defaults to 180.
    Returns: [status,data]
        bool: If function is failed returns False.
        tuple (x, y): Image Center co-ordinates.
    """
    return mouse.Mouse.mouse_search_snip_return_coordinates_x_y(img, wait)


# ---------  Mouse Functions Ends ---------


# ---------  Keyboard Functions ---------

def key_press(key_1='', key_2='', key_3='', write_to_window=""):
    """Emulates the given keystrokes.
    Args:
        key_1 (str, optional): Enter the 1st key 
        Eg: ctrl or shift. Defaults to ''.
        key_2 (str, optional): Enter the 2nd key in combination. 
        Eg: alt or A. Defaults to ''.
        key_3 (str, optional): Enter the 3rd key in combination. 
        Eg: del or tab. Defaults to ''.
        write_to_window (str, optional): (Only in Windows) Name of Window you want to activate. Defaults to "".
    Supported Keys:
        ['\\t', '\\n', '\\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',')', '*', '+', ',', '-', '.', '/', 
        '0', '1', '2', '3', '4', '5', '6', '7','8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 
        'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
        'browserback', 'browserfavorites', 'browserforward', 'browserhome',
        'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
        'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
        'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
        'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
        'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
        'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
        'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
        'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
        'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
        'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
        'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
        'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
        'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
        'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
        'command', 'option', 'optionleft', 'optionright']
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return keyboard.Keyboard.key_press(key_1, key_2, key_3, write_to_window)


def key_write_enter(text_to_write="Clointfusion is awesome", write_to_window="", delay_after_typing=1, key="e"):
    """Writes/Types the given text.
    Args:
        text_to_write (str, optional): Text you wanted to type
        Eg: ClointFusion is awesone. Defaults to "".
        write_to_window (str, optional): (Only in Windows) Name of Window you want to activate
        Eg: Notepad. Defaults to "".
        delay_after_typing (int, optional): Seconds in time to wait after entering the text
        Eg: 5. Defaults to 1.
        key (str, optional): Press Enter key after typing.
        Eg: t for tab. Defaults to e
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return keyboard.Keyboard.key_write_enter(text_to_write, write_to_window, delay_after_typing, key)


def key_hit_enter(write_to_window=""):
    """Enter key will be pressed once.
    Args:
        write_to_window (str, optional): (Only in Windows)Name of Window you want to activate.
        Eg: Notepad. Defaults to "".
    Returns:[status]
        bool: Whether the function is successful or failed.
    """
    return keyboard.Keyboard.key_hit_enter(write_to_window)


# --------- Keyboard Functions Ends ---------


# ---------  Browser Functions ---------

ChromeBrowser = chrome.Chrome.ChromeBrowser

# ---------  Browser Functions Ends ---------


# ---------  Folder Functions Starts ---------

def folder_read_text_file(txt_file_path=""):
    """
    Reads from a given text file and returns entire contents as a single list
    Returns : [status,data]
    """
    return folder.Folder.folder_read_text_file(txt_file_path)


def folder_write_text_file(txt_file_path="", contents=""):
    """
    Writes given contents to a text file
    Returns : [status]
    """
    folder.Folder.folder_write_text_file(txt_file_path, contents)


def folder_create(strFolderPath=""):
    """
    while making leaf directory if any intermediate-level directory is missing,
    folder_create() method will create them all.
    Parameters:
        folderPath (str) : path to the folder where the folder is to be created.
    For example consider the following path:
    Returns :[status]
    """
    folder.Folder.folder_create(strFolderPath)


def folder_create_text_file(textFolderPath="", txtFileName=""):
    """
    Creates Text file in the given path.
    Internally this uses folder_create() method to create folders if the folder/s does not exist.
    automatically adds txt extension if not given in textFilePath.
    Parameters:
        textFilePath (str) : Complete path to the folder with double slashes.
    Returns:[status,data]
    """
    folder.Folder.folder_create_text_file(textFolderPath, txtFileName)


def folder_get_all_filenames_as_list(strFolderPath="", extension='all'):
    """
    Get all the files of the given folder in a list.
    Parameters:
        strFolderPath  (str) : Location of the folder.
        extension      (str) : extention of the file. by default all the files will be listed regarless of the extension.
    returns: [status,data]
        allFilesOfaFolderAsLst (List) : all the file names as a list.
    """
    return folder.Folder.folder_get_all_filenames_as_list(strFolderPath, extension)


def folder_delete_all_files(fullPathOfTheFolder="", file_extension_without_dot="all", print_status=True):
    """
    Deletes all the files of the given folder
    Parameters:
        fullPathOfTheFolder  (str) : Location of the folder.
        extension            (str) : extention of the file. by default all the files will be deleted inside the given folder
                                    regarless of the extension.
    returns:[status,data]
        count (int) : number of files deleted.
    """
    return folder.Folder.folder_delete_all_files(fullPathOfTheFolder, file_extension_without_dot, print_status)


def file_rename(old_file_path='', new_file_name='', print_status=True):
    '''
    Renames the given file name to new file name with same extension
    Returns : [status,data]
        Path to new file:str
    '''
    folder.Folder.file_rename(old_file_path, new_file_name, print_status)


def file_get_json_details(path_of_json_file='', section=''):
    '''
    Returns all the details of the given section in a dictionary
    [status,data]
    '''
    return folder.Folder.file_get_json_details(path_of_json_file, section)

# ---------  Folder Functions Ends ---------


# ---------  Window Operations Functions ---------

def window_show_desktop():
    """
    Minimizes all the applications and shows Desktop.
    Returns:
        [status:bool]
    """
    return windows.Windows.window_show_desktop()


def window_get_all_opened_titles_windows():
    """
    Gives the title of all the existing (open) windows.
    Returns: [status,data]
        allTitles_lst  (list) : returns all the titles of the window as list.
    """
    return windows.Windows.window_get_all_opened_titles_windows()


def window_activate_and_maximize_windows(windowName=""):
    """
    Activates and maximizes the desired window.
    Parameters:
        windowName  (str) : Name of the window to maximize.
    Returns: [status]
    """
    return windows.Windows.window_activate_and_maximize_windows(windowName)


def window_minimize_windows(windowName=""):
    """
    Activates and minimizes the desired window.
    Parameters:
        windowName  (str) : Name of the window to miniimize.
    Returns: [status]
    """
    return windows.Windows.window_minimize_windows(windowName)


def window_close_windows(windowName=""):
    """
    Close the desired window.
    Parameters:
        windowName  (str) : Name of the window to close.
    """
    return windows.Windows.window_close_windows(windowName)


def launch_any_exe_bat_application(pathOfExeFile=""):
    """Launches any exe or batch file or excel file etc.
    Args:
        pathOfExeFile (str, optional): Location of the file with extension
        Eg: Notepad, TextEdit. Defaults to "".
    Returns [status]
    """
    return windows.launch_any_exe_bat_application(pathOfExeFile)


def window_get_active_window():
    """
    Returns the active window title.
    Returns : [status,data]
    """
    return windows.Windows.window_get_active_window()

# ---------  Window Operations Functions Ends ---------


# ---------  String Functions ---------

def string_extract_only_alphabets(inputString=""):
    """
    Returns only alphabets from given input string
    Returns : [status,data]
    """
    return string.String.string_extract_only_alphabets(inputString)


def string_extract_only_numbers(inputString=""):
    """
    Returns only numbers from given input string
    Returns : [status,data]
    """
    return string.String.string_extract_only_numbers(inputString)


def string_remove_special_characters(inputStr=""):
    """
    Removes all the special character.
    Parameters:
        inputStr  (str) : string for removing all the special character in it.
    Returns : [status,data]
        outputStr (str) : returns the alphanumeric string
    """

    return string.String.string_remove_special_characters(inputStr)

# ---------  String Functions Ends ---------


# --------- Screenscraping Functions ---------

# "Full path to the folder (with double slashes) where notepad is to be stored"
def scrape_save_contents_to_notepad(folderPathToSaveTheNotepad="", switch_to_window="", X=0, Y=0):
    """
    Copy pastes all the available text on the screen to notepad and saves it.
    Returns : [status]
    """
    return screen_scraping.ScreenScraping.scrape_save_contents_to_notepad(folderPathToSaveTheNotepad, switch_to_window, X, Y)


def screen_clear_search(delay=0.2):
    """
    Clears previously found text (crtl+f highlight)
    Returns: [status]
    """
    screen_scraping.ScreenScraping.screen_clear_search(delay)


def search_highlight_tab_enter_open(searchText="", hitEnterKey="Yes", shift_tab='No'):
    """
    Searches for a text on screen using crtl+f and hits enter.
    This function is useful in Citrix environment
    Returns: [status]
    """
    screen_scraping.ScreenScraping.search_highlight_tab_enter_open(
        searchText, hitEnterKey, shift_tab)


def find_text_on_screen(searchText="", delay=0.1, occurance=1, isSearchToBeCleared=False):
    """
    Clears previous search and finds the provided text on screen.
    """
    screen_scraping.ScreenScraping.find_text_on_screen(
        searchText, delay, occurance, isSearchToBeCleared)


# --------- Screenscraping Functions Ends ---------


# --------- Utility Functions ---------

def find(function_partial_name=""):
    """Returns [status]"""
    # Find and inspect python functions
    extras.Extras.find(function_partial_name)


def pause_program(seconds="5"):
    """
    Stops the program for given seconds
    Returns:
        [status]
    """
    extras.Extras.pause_program(seconds)


def show_emoji(strInput="", print_emoji=False):
    """
    Function which prints Emojis
    Usage:
    print(show_emoji('thumbsup'))
    print("OK",show_emoji('thumbsup'))
    Default: thumbsup
    Returns: [status,data]
    """
    return extras.Extras.show_emoji(strInput, print_emoji)


def download_this_file(url="", output_folder_path=""):
    """
    Downloads a given url file to BOT output folder or Browser's Download folder
    Returns : [status,data]
        File path of downloaded file
    """
    return extras.Extras.download_this_file(url, output_folder_path)


def clear_screen():
    """
    Clears Python Interpreter Terminal Window Screen
    Returns: [status]
    """
    extras.Extras.clear_screen()


def print_with_magic_color(strMsg="", magic=False):
    """
    Prints the message with colored foreground font
    Returns: [status]
    """
    extras.Extras.print_with_magic_color(strMsg, magic)


def install_module(module_name=""):
    """
    Installs the module
    Returns: [status]
    """
    extras.Extras.install_module(module_name)


def uninstall_module(module_name=""):
    """
    Uninstalls the module
    Returns: [status]
    """
    extras.Extras.uninstall_module(module_name)

# --------- Utility Functions Ends ---------


# --------- Voice Interface ---------

def text_to_speech(audio, show=True, rate=170):
    """
    Text to Speech using Google's Generic API
    Rate is the speed of speech. Default is 150
    Actual default : 200

    """
    return voice.Voice.text_to_speech(audio, show, rate)


def speech_to_text():
    """
    Speech to Text using Google's Generic API
    """
    return voice.Voice.speech_to_text()


# --------- Voice Interface Ends ---------
