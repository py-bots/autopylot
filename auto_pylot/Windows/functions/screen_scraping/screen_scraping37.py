import win32clipboard

from auto_pylot.CrashHandler import report_error


def scrape_save_contents_to_notepad(folderPathToSaveTheNotepad="", switch_to_window="", X=0, Y=0):

    # Description:
    """
    Copy pastes all the available text on the screen to notepad and saves it.
    """

    # import section
    from auto_pylot.Engine import window_activate_and_maximize_windows
    import time
    import pywinauto as pwa
    import pathlib as Path
    # import clipboard

    # Response section
    status = False
    data = None

    try:

        if not folderPathToSaveTheNotepad:
            raise Exception("Folder path to save the notepad is not provided.")

        if switch_to_window:
            window_activate_and_maximize_windows(switch_to_window)

        time.sleep(1)

        if X == 0 and Y == 0:
            from win32api import GetSystemMetrics
            X = int(GetSystemMetrics(0))/2
            Y = int(GetSystemMetrics(1))/2
        # pg.click(X, Y)
        pwa.mouse.click(coords=(X, Y), button='left')
        time.sleep(0.5)

        # pg.hotkey("ctrl", "a")
        pwa.keyboard.send_keys("{VK_LCONTROL down} a {VK_LCONTROL up}")
        time.sleep(1)

        # pg.hotkey("ctrl", "c")
        pwa.keyboard.send_keys("{VK_LCONTROL down} c {VK_LCONTROL up}")
        time.sleep(1)

        clipboard_data = get_data_from_clipboard()
        time.sleep(2)

        screen_clear_search()

        notepad_file_path = Path(folderPathToSaveTheNotepad)
        notepad_file_path = notepad_file_path / 'notepad-contents.txt'

        f = open(notepad_file_path, "w", encoding="utf-8")
        f.write(clipboard_data)
        time.sleep(2)
        f.close()

        clipboard_data = ''
        data = str(notepad_file_path)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status is True and data is not None:
            return [status, data]
        return [status]


def screen_clear_search(delay=0.2):

    # Description:
    """
    Clears previously found text (crtl+f highlight)
    """

    # import section
    # from clointfusion.clointfusion import text_to_speech
    import pywinauto as pwa
    import time
    # Response section
    status = False
    data = None

    try:
        # pg.hotkey("ctrl", "f")
        pwa.keyboard.send_keys("{VK_LCONTROL down} f {VK_LCONTROL up}")

        time.sleep(delay)
        # pg.typewrite("^%#")
        pwa.keyboard.send_keys("^%#")
        time.sleep(delay)
        # pg.hotkey("esc")
        pwa.keyboard.send_keys("{ESC}")
        time.sleep(delay)
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status is True and data is not None:
            return [status, data]
        return [status]


def search_highlight_tab_enter_open(searchText="", hitEnterKey="Yes", shift_tab='No'):

    # Description:
    """
    Searches for a text on screen using crtl+f and hits enter.
    This function is useful in Citrix environment
    """

    # import section
    import pywinauto as pwa
    import time
    # Response section
    status = False
    data = None

    try:

        if not searchText:
            raise Exception("Search text is not provided.")

        time.sleep(0.5)

        # pg.hotkey("ctrl", "f")
        pwa.keyboard.send_keys("{VK_LCONTROL down} f {VK_LCONTROL up}")

        time.sleep(0.5)

        # pg.write(searchText)
        pwa.keyboard.send_keys(searchText)

        time.sleep(0.5)

        # pg.hotkey("enter")
        pwa.keyboard.send_keys("{ENTER}")

        time.sleep(0.5)

        # pg.hotkey("esc")
        pwa.keyboard.send_keys("{ESC}")
        time.sleep(0.2)
        if hitEnterKey.lower() == "yes" and shift_tab.lower() == "yes":

            # pg.hotkey("tab"){TAB}
            pwa.keyboard.send_keys("{TAB}")
            time.sleep(0.3)

            # pg.hotkey("shift", "tab")
            pwa.keyboard.send_keys("{VK_LSHIFT down} {TAB} {VK_LSHIFT up}")

            time.sleep(0.3)

            # pg.hotkey("enter")
            pwa.keyboard.send_keys("{ENTER}")
            time.sleep(2)
        elif hitEnterKey.lower() == "yes" and shift_tab.lower() == "no":

            # pg.hotkey("enter")
            pwa.keyboard.send_keys("{ENTER}")
            time.sleep(2)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status is True and data is not None:
            return [status, data]
        return [status]


def find_text_on_screen(searchText="", delay=0.1, occurance=1, isSearchToBeCleared=False):

    # Description:
    """
    Clears previous search and finds the provided text on screen.
    """

    # import section
    import time
    import pywinauto as pwa
    # Response section
    status = False
    data = None

    try:
        screen_clear_search()  # default

        if not searchText:
            raise Exception("Search text is not provided.")

        time.sleep(delay)
        # pg.hotkey("ctrl", "f")
        pwa.keyboard.send_keys("{VK_LCONTROL down} f {VK_LCONTROL up}")
        time.sleep(delay)
        # pg.typewrite(searchText)
        pwa.keyboard.send_keys(searchText)
        time.sleep(delay)

        for i in range(occurance-1):
            # pg.hotkey("enter")
            pwa.keyboard.send_keys("{ENTER}")
            time.sleep(delay)

        # pg.hotkey("esc")
        pwa.keyboard.send_keys("{ESC}")
        time.sleep(delay)

        if isSearchToBeCleared:
            screen_clear_search()

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status is True and data is not None:
            return [status, data]
        return [status]

# Windows Specific Functions


def GetClipboardFormats():
    win32clipboard.OpenClipboard()
    available_formats = []
    current_format = 0
    while True:
        current_format = win32clipboard.EnumClipboardFormats(current_format)
        if not current_format:
            break
        available_formats.append(current_format)
    win32clipboard.CloseClipboard()
    return available_formats

# Windows Specific Functions


def get_data_from_clipboard(format_id=win32clipboard.CF_UNICODETEXT):
    if format_id not in GetClipboardFormats():
        raise RuntimeError("That format is not available")
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData(format_id)
        data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    finally:
        win32clipboard.CloseClipboard()
    return data
