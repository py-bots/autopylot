from my_autopylot.CrashHandler import report_error


def _window_find_exact_name(windowName=""):
    """
    Gives you the exact window name you are looking for.

    Parameters:
        windowName  (str) : Name of the window to find.

    Returns:
        win (str)              : Exact window name.
        window_found (boolean) : A boolean TRUE if the window is found
    """
    import pygetwindow as gw
    win = ""
    window_found = False

    if not windowName:
        raise ValueError("Window name cannot be empty")

    lst = gw.getAllTitles()

    for item in lst:
        if str(item).strip():
            if str(windowName).lower() in str(item).lower():
                win = item
                window_found = True
                break
    return win, window_found


def window_show_desktop():

    # Description:
    """
    Minimizes all the applications and shows Desktop.
    """

    # import section
    import time
    import pywinauto as pwa

    # Response section
    status = False
    data = None

    try:
        time.sleep(0.5)
        pwa.keyboard.send_keys('{VK_RWIN down} d {VK_RWIN up}')

        time.sleep(0.5)

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


def window_get_active_window():

    # Description:
    """
    Returns the title of the active window.
    """

    # import section
    import win32gui

    # Response section
    status = False
    data = None

    try:
        data = win32gui.GetWindowText(win32gui.GetForegroundWindow())

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


def window_activate_window(window_title=''):

    # Description:
    """
    Activates the given window.
    """

    # import section
    import time
    import pygetwindow as gw

    # Response section
    status = False
    data = None

    try:
        if not window_title:
            raise Exception('Window title name is empty.')

        item, window_found = _window_find_exact_name(window_title)
        if window_found:
            windw = gw.getWindowsWithTitle(item)[0]

            try:
                windw.activate()
            except:
                windw.minimize()
                windw.maximize()
            time.sleep(1)

        else:
            raise Exception('Window title name not found.')

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


def window_get_all_opened_titles_windows():

    # Description:
    """
    Gives the title of all the existing (open) windows.
    Returns:
        allTitles_lst  (list) : returns all the titles of the window as list.
    """

    # import section
    import pygetwindow as gw

    # Response section
    status = False
    data = None

    try:
        allTitles_lst = []
        lst = gw.getAllTitles()
        for item in lst:
            if str(item).strip() != "" and str(item).strip() not in allTitles_lst:
                allTitles_lst.append(str(item).strip())
        data = allTitles_lst

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


def window_activate_and_maximize_windows(windowName=""):

    # Description:
    """
    Activates and maximizes the desired window.
    Parameters:
        windowName  (str) : Name of the window to maximize.
    """

    # import section
    import time
    import pygetwindow as gw

    # Response section
    status = False
    data = None

    try:
        if not windowName:
            raise Exception('Window title name is empty.')

        item, window_found = _window_find_exact_name(windowName)
        if window_found:
            windw = gw.getWindowsWithTitle(item)[0]

            try:
                windw.activate()
                windw.maximize()
            except:
                windw.minimize()
                time.sleep(1)
                windw.maximize()
            time.sleep(1)

        else:
            raise Exception('Window title name not found.')

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


def window_minimize_windows(windowName=""):

    # Description:
    """
    Activates and minimizes the desired window.
    Parameters:
        windowName  (str) : Name of the window to miniimize.
    """

    # import section
    import time
    import pygetwindow as gw

    # Response section
    status = False
    data = None

    try:
        if not windowName:
            raise Exception('Window title name is empty.')

        item, window_found = _window_find_exact_name(windowName)
        if window_found:
            windw = gw.getWindowsWithTitle(item)[0]
            windw.minimize()
            time.sleep(1)
        else:
            raise Exception('Window title name not found.')

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


def window_close_windows(windowName=""):

    # Description:
    """
    Close the desired window.
    Parameters:
        windowName  (str) : Name of the window to close.
    """

    # import section
    import time
    import pygetwindow as gw

    # Response section
    status = False
    data = None

    try:
        if not windowName:
            raise Exception('Window title name is empty.')

        item, window_found = _window_find_exact_name(windowName)
        if window_found:
            windw = gw.getWindowsWithTitle(item)[0]
            windw.close()
            time.sleep(1)
        else:
            raise Exception('Window title name not found.')

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


def launch_any_exe_bat_application(pathOfExeFile=""):

    # Description:
    """
    Launches any exe or batch file or excel file etc.
    Args:
        pathOfExeFile (str, optional): Location of the file with extension 
        Eg: Notepad, TextEdit. Defaults to "".
    """

    # import section
    import win32gui
    import win32con
    import subprocess
    import os
    import time

    # Response section
    status = False
    data = None

    try:
        if not pathOfExeFile:
            raise Exception('Path of the exe file is empty.')

        try:
            subprocess.Popen(pathOfExeFile)
            time.sleep(2)
            hwnd = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
            status = True
        except Exception:
            os.startfile(pathOfExeFile)

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
