from my_autopylot.CrashHandler import report_error


def mouse_click(x='', y='', left_or_right="left", no_of_clicks=1, type_of_movement="abs"):

    # Description:
    """
    Clicks at the given X Y Co-ordinates on the screen using single / double / triple click(s). Default clicks on current position.

    Args:
        x (int): x-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        y (int): y-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        left_or_right (str, optional): Which mouse button.
        Eg: right or left, Defaults: left.
        no_of_click (int, optional): Number of times specified mouse button to be clicked.
        Eg: 1 or 2, Max 3. Defaults: 1.

    Returns:
        bool: Whether the function is successful or failed.
    """

    # import section
    import pywinauto as pwa
    import win32api

    # Response section
    status = False
    data = None
    not_default = True

    try:

        if (not x or not y) and (type_of_movement == "abs" or type_of_movement == "rel"):
            x, y = win32api.GetCursorPos()
            not_default = False
        elif type_of_movement != "abs" and type_of_movement != "rel":
            raise Exception("Please check the type of movement.")

        if x and y:
            if type_of_movement == "abs":
                x, y = int(x), int(y)
            elif type_of_movement == "rel" and not_default:
                current_x, current_y = win32api.GetCursorPos()
                x, y = int(x), int(y)
                x, y = int(current_x + x), int(current_y + y)

            if no_of_clicks == 1:
                pwa.mouse.click(coords=(x, y), button=left_or_right)
            elif no_of_clicks == 2:
                pwa.mouse.double_click(coords=(x, y), button=left_or_right)
            else:
                for i in range(no_of_clicks):
                    pwa.mouse.click(coords=(x, y), button=left_or_right)

            status = True
        else:
            raise Exception("X and Y co-ordinates are required.")

    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status is True and data is not None:
            return [status, data]
        return [status]


def mouse_move(x="", y="", type_of_movement="abs"):

    # Description:
    """
    Moves the cursor to the given X Y Co-ordinates.

    Args:
        x (int): x-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        y (int): y-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        type_of_movement (str): Type of movement (Absolute or Relative to current Position).
        Eg: abs or rel, Defaults: abs.

    Returns:
        bool: Whether the function is successful or failed.
    """

    # import section
    import time
    import pywinauto as pwa
    import win32api

    # Response section
    status = False
    data = None

    try:

        if x and y:

            if type_of_movement:

                if type_of_movement == "abs":
                    x, y = int(x), int(y)
                    time.sleep(0.1)
                    # pg.moveTo(x, y)
                    pwa.mouse.move(coords=(x, y))
                    time.sleep(0.1)
                elif type_of_movement == "rel":
                    current_x, current_y = win32api.GetCursorPos()
                    x, y = int(current_x + x), int(current_y + y)
                    # pg.moveRel(x, y)
                    pwa.mouse.move(coords=(x, y))
                    time.sleep(0.1)
                else:
                    raise Exception(
                        "Please check the 'type of movement' value.")

            else:
                raise Exception("Type of movement is required.")

        else:
            raise Exception("X and Y co-ordinates are required.")

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


def mouse_drag_from_to(x1="", y1="", x2="", y2=""):
    # Description:
    """
    Clicks and drags from x1 y1 co-ordinates to x2 y2 Co-ordinates on the screen
    Args:
        x1 or x2 (int): x-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        y1 or y2 (int): y-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        delay (float, optional): Seconds to wait while performing action. 
        Eg: 1 or 0.5, Defaults to 0.5.
    Returns:
        bool: Whether the function is successful or failed.
    """

    # import section
    import time
    import pywinauto as pwa

    # Response section
    status = False
    data = None

    try:

        if x1 and y1 and x2 and y2:
            time.sleep(0.1)
            x1, y1 = int(x1), int(y1)
            x2, y2 = int(x2), int(y2)
            pwa.mouse.move(coords=(x1, y1))
            pwa.mouse.press(coords=(x1, y1))
            pwa.mouse.move(coords=(x2, y2))
            pwa.mouse.release(coords=(x2, y2))
            time.sleep(0.1)

        else:
            raise Exception("X and Y co-ordinates are required.")
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


def mouse_search_snip_return_coordinates_x_y(img="", wait=10):

    # import section
    import time
    import pyscreeze as ps

    # Response section
    status = False
    data = None
    i = 0

    try:
        if not img:
            raise Exception("Image path is required.")
        pos = ps.locateCenterOnScreen(img)
        while pos == None and i < int(wait):
            time.sleep(1)
            pos = ps.locateCenterOnScreen(img)
            i += 1
        if pos:
            data = (pos[0], pos[1])

    except Exception as e:
        report_error(e)
    else:
        if pos:
            status = True
        else:
            status = False
    finally:
        if status is True and data is not None:
            return [status, data]
        return [status]
