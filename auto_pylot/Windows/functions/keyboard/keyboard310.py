from auto_pylot.CrashHandler import report_error
# # Functions Represent in this file
#  - key_press
#  - key_write_enter
#  - key_hit_enter

print("310 Keyboard Functions imported successfully.")

def key_press(key_1='', key_2='', key_3='', write_to_window=""):

    # Description:
    """
    Emulates the given keystrokes.

    Args:
        key_1 (str, optional): Enter the 1st key
        Eg: ctrl or shift. Defaults to ''.
        key_2 (str, optional): Enter the 2nd key in combination.
        Eg: alt or A. Defaults to ''.
        key_3 (str, optional): Enter the 3rd key in combination.
        Eg: del or tab. Defaults to ''.
        write_to_window (str, optional): (Only in Windows) Name of Window you want to activate. Defaults to "".

    Supported Keys:
        [{SCROLLLOCK}, {VK_SPACE}, {VK_LSHIFT}, {VK_PAUSE}, {VK_MODECHANGE},
        {BACK}, {VK_HOME}, {F23}, {F22}, {F21}, {F20}, {VK_HANGEUL}, {VK_KANJI},
        {VK_RIGHT}, {BS}, {HOME}, {VK_F4}, {VK_ACCEPT}, {VK_F18}, {VK_SNAPSHOT},
        {VK_PA1}, {VK_NONAME}, {VK_LCONTROL}, {ZOOM}, {VK_ATTN}, {VK_F10}, {VK_F22},
        {VK_F23}, {VK_F20}, {VK_F21}, {VK_SCROLL}, {TAB}, {VK_F11}, {VK_END},
        {LEFT}, {VK_UP}, {NUMLOCK}, {VK_APPS}, {PGUP}, {VK_F8}, {VK_CONTROL},
        {VK_LEFT}, {PRTSC}, {VK_NUMPAD4}, {CAPSLOCK}, {VK_CONVERT}, {VK_PROCESSKEY},
        {ENTER}, {VK_SEPARATOR}, {VK_RWIN}, {VK_LMENU}, {VK_NEXT}, {F1}, {F2},
        {F3}, {F4}, {F5}, {F6}, {F7}, {F8}, {F9}, {VK_ADD}, {VK_RCONTROL},
        {VK_RETURN}, {BREAK}, {VK_NUMPAD9}, {VK_NUMPAD8}, {RWIN}, {VK_KANA},
        {PGDN}, {VK_NUMPAD3}, {DEL}, {VK_NUMPAD1}, {VK_NUMPAD0}, {VK_NUMPAD7},
        {VK_NUMPAD6}, {VK_NUMPAD5}, {DELETE}, {VK_PRIOR}, {VK_SUBTRACT}, {HELP},
        {VK_PRINT}, {VK_BACK}, {CAP}, {VK_RBUTTON}, {VK_RSHIFT}, {VK_LWIN}, {DOWN},
        {VK_HELP}, {VK_NONCONVERT}, {BACKSPACE}, {VK_SELECT}, {VK_TAB}, {VK_HANJA},
        {VK_NUMPAD2}, {INSERT}, {VK_F9}, {VK_DECIMAL}, {VK_FINAL}, {VK_EXSEL},
        {RMENU}, {VK_F3}, {VK_F2}, {VK_F1}, {VK_F7}, {VK_F6}, {VK_F5}, {VK_CRSEL},
        {VK_SHIFT}, {VK_EREOF}, {VK_CANCEL}, {VK_DELETE}, {VK_HANGUL}, {VK_MBUTTON},
        {VK_NUMLOCK}, {VK_CLEAR}, {END}, {VK_MENU}, {SPACE}, {BKSP}, {VK_INSERT},
        {F18}, {F19}, {ESC}, {VK_MULTIPLY}, {F12}, {F13}, {F10}, {F11}, {F16},
        {F17}, {F14}, {F15}, {F24}, {RIGHT}, {VK_F24}, {VK_CAPITAL}, {VK_LBUTTON},
        {VK_OEM_CLEAR}, {VK_ESCAPE}, {UP}, {VK_DIVIDE}, {INS}, {VK_JUNJA},
        {VK_F19}, {VK_EXECUTE}, {VK_PLAY}, {VK_RMENU}, {VK_F13}, {VK_F12}, {LWIN},
        {VK_DOWN}, {VK_F17}, {VK_F16}, {VK_F15}, {VK_F14}]

    Returns:
        bool: Whether the function is successful or failed.
    """

    # import section
    import time
    import pywinauto as pwa
    # from auto_pylot.Engine import window_activate

    # Response section
    status = False
    data = None

    # Logic section
    try:
        if key_1 == '':
            raise Exception("Key 1 is empty.")
    
        supported_keys = ['{SCROLLLOCK}', '{VK_SPACE}', '{VK_LSHIFT}', '{VK_PAUSE}', '{VK_MODECHANGE}',
        '{BACK}', '{VK_HOME}', '{F23}', '{F22}', '{F21}', '{F20}', '{VK_HANGEUL}', '{VK_KANJI}',
        '{VK_RIGHT}', '{BS}', '{HOME}', '{VK_F4}', '{VK_ACCEPT}', '{VK_F18}', '{VK_SNAPSHOT}',
        '{VK_PA1}', '{VK_NONAME}', '{VK_LCONTROL}', '{ZOOM}', '{VK_ATTN}', '{VK_F10}', '{VK_F22}',
        '{VK_F23}', '{VK_F20}', '{VK_F21}', '{VK_SCROLL}', '{TAB}', '{VK_F11}', '{VK_END}',
        '{LEFT}', '{VK_UP}', '{NUMLOCK}', '{VK_APPS}', '{PGUP}', '{VK_F8}', '{VK_CONTROL}',
        '{VK_LEFT}', '{PRTSC}', '{VK_NUMPAD4}', '{CAPSLOCK}', '{VK_CONVERT}', '{VK_PROCESSKEY}',
        '{ENTER}', '{VK_SEPARATOR}', '{VK_RWIN}', '{VK_LMENU}', '{VK_NEXT}', '{F1}', '{F2}',
        '{F3}', '{F4}', '{F5}', '{F6}', '{F7}', '{F8}', '{F9}', '{VK_ADD}', '{VK_RCONTROL}',
        '{VK_RETURN}', '{BREAK}', '{VK_NUMPAD9}', '{VK_NUMPAD8}', '{RWIN}', '{VK_KANA}',
        '{PGDN}', '{VK_NUMPAD3}', '{DEL}', '{VK_NUMPAD1}', '{VK_NUMPAD0}', '{VK_NUMPAD7}',
        '{VK_NUMPAD6}', '{VK_NUMPAD5}', '{DELETE}', '{VK_PRIOR}', '{VK_SUBTRACT}', '{HELP}',
        '{VK_PRINT}', '{VK_BACK}', '{CAP}', '{VK_RBUTTON}', '{VK_RSHIFT}', '{VK_LWIN}', '{DOWN}',
        '{VK_HELP}', '{VK_NONCONVERT}', '{BACKSPACE}', '{VK_SELECT}', '{VK_TAB}', '{VK_HANJA}',
        '{VK_NUMPAD2}', '{INSERT}', '{VK_F9}', '{VK_DECIMAL}', '{VK_FINAL}', '{VK_EXSEL}',
        '{RMENU}', '{VK_F3}', '{VK_F2}', '{VK_F1}', '{VK_F7}', '{VK_F6}', '{VK_F5}', '{VK_CRSEL}',
        '{VK_SHIFT}', '{VK_EREOF}', '{VK_CANCEL}', '{VK_DELETE}', '{VK_HANGUL}', '{VK_MBUTTON}',
        '{VK_NUMLOCK}', '{VK_CLEAR}', '{END}', '{VK_MENU}', '{SPACE}', '{BKSP}', '{VK_INSERT}',
        '{F18}', '{F19}', '{ESC}', '{VK_MULTIPLY}', '{F12}', '{F13}', '{F10}', '{F11}', '{F16}',
        '{F17}', '{F14}', '{F15}', '{F24}', '{RIGHT}', '{VK_F24}', '{VK_CAPITAL}', '{VK_LBUTTON}',
        '{VK_OEM_CLEAR}', '{VK_ESCAPE}', '{UP}', '{VK_DIVIDE}', '{INS}', '{VK_JUNJA}',
        '{VK_F19}', '{VK_EXECUTE}', '{VK_PLAY}', '{VK_RMENU}', '{VK_F13}', '{VK_F12}', '{LWIN}',
        '{VK_DOWN}', '{VK_F17}', '{VK_F16}', '{VK_F15}', '{VK_F14}']
        
        def get_proper_key(key):
            if 'alt' in key.lower():
                key = 'MENU'
            for i in supported_keys:
                if str(key) in str(i):
                    return i
            return key

        special_keys = ['{VK_LCONTROL}', '{VK_RWIN}', '{VK_LMENU}','{VK_LSHIFT}', '{TAB}',]
        
        def make_down(key):
            return key.replace('}', ' down}')

        def make_up(key):
            return key.replace('}', ' up}')
        
        time.sleep(0.5)
        key_1 = get_proper_key(key_1.upper()) if len(key_1) > 1 else key_1
        key_2 = get_proper_key(key_2.upper()) if len(key_2) > 1 else key_2
        key_3 = get_proper_key(key_3.upper()) if len(key_3) > 1 else key_3
        
        case_1 = True if key_1 in special_keys and key_2 not in special_keys and key_3 not in special_keys else False # Only 1 Special Key
        case_2 = True if key_1 in special_keys and key_2 in special_keys and key_3 not in special_keys else False # 2 Special Keys

        if write_to_window:
            window_activate(write_to_window)
        
        if case_1:
            key_1_down = make_down(key_1)
            key_1_up = make_up(key_1)
            pwa.keyboard.send_keys(str(key_1_down + key_2 + key_3 + key_1_up))
        elif case_2:
            key_1_down = make_down(key_1)
            key_1_up = make_up(key_1)
            key_2_down = make_down(key_2)
            key_2_up = make_up(key_2)
            pwa.keyboard.send_keys(str(key_1_down + key_2_down + key_3 + key_2_up + key_1_up))
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

def key_write_enter(text_to_write="", write_to_window="", delay_after_typing=1, key="e"):

    # Description:
    """
    Writes/Types the given text.

    Args:
        text_to_write (str, optional): Text you wanted to type
        Eg: ClointFusion is awesone. Defaults to "".
        write_to_window (str, optional): (Only in Windows) Name of Window you want to activate
        Eg: Notepad. Defaults to "".
        delay_after_typing (int, optional): Seconds in time to wait after entering the text
        Eg: 5. Defaults to 1.
        key (str, optional): Press Enter key after typing.
        Eg: t for tab. Defaults to e

    Returns:
        bool: Whether the function is successful or failed.
    """

    # import section
    import time
    import pywinauto as pwa
    # from auto_pylot.Engine import window_activate
    # Response section
    status = False
    data = None

    # Logic section
    try:
        if not text_to_write:
            raise Exception("Text to write is empty.")

        if write_to_window:
            window_activate(write_to_window)

        time.sleep(0.2)
        pwa.keyboard.send_keys(text_to_write)
        if key.lower() == "e":
            pwa.keyboard.send_keys('{ENTER}')
        if key.lower() == "t":
            pwa.keyboard.send_keys('{TAB}')
        time.sleep(delay_after_typing)

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

def key_hit_enter(write_to_window=""):

    # Description:
    """
    Enter key will be pressed once.

    Args:
        write_to_window (str, optional): (Only in Windows)Name of Window you want to activate.
        Eg: Notepad. Defaults to "".

    Returns:
        bool: Whether the function is successful or failed.
    """

    # import section
    import time
    import pywinauto as pwa
    # from auto_pylot.Engine import window_activate
    
    # Response section
    status = False
    data = None

    # Logic section

    try:
        if write_to_window:
            window_activate(write_to_window)
        pwa.keyboard.send_keys('{ENTER}')
        status = True

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
