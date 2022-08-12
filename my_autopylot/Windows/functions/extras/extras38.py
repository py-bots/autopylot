from my_autopylot.CrashHandler import report_error, install_module, uninstall_module


def find(function_partial_name=""):
    # Description:
    """
    Description of the function
    """

    # import section
    import pyinspect as pi
    # Response section
    status = False
    data = None

    try:
        if function_partial_name:
            import my_autopylot.Engine as ap_docs
            pi.search(ap_docs, name=function_partial_name)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status, None]


def pause_program(seconds="5"):

    # Description:
    """
    Stops the program for given seconds
    """

    # import section
    import time

    # Response section
    status = False
    data = None

    try:
        seconds = int(seconds)
        time.sleep(seconds)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status, None]


def download_this_file(url="", output_folder_path="", notify=True):
    # Description:
    """
    Downloads a given url file to BOT output folder or Browser's Download folder
    """

    # import section
    import webbrowser
    import requests
    from pathlib import Path
    import os
    # Response section
    status = False
    data = None
    if not output_folder_path:
        clointfusion_directory = r"C:\Users\{}\ClointFusion".format(
            str(os.getlogin()))
        output_folder_path = Path(os.path.join(
            clointfusion_directory, "Output"))

    try:
        if not url:
            raise Exception("URL is required")

        if "export" in url:
            webbrowser.open_new(url)

        else:
            extension = str(url).rsplit(".", 1)[1]
            r = requests.get(url)
            download_file_path = output_folder_path / \
                "downloaded_cf.{}".format(extension)

            with open(download_file_path, 'wb') as f:
                f.write(r.content)

            if notify:
                import tkinter as tk
                root = tk.Tk()     # Create window
                root.withdraw()
                from tkinter import messagebox
                messagebox.showinfo(
                    "Download Complete", "Downloaded file saved at {}".format(download_file_path))

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status, None]


def clear_screen():
    # Description:
    """
    Clears Python Interpreter Terminal Window Screen

    """

    # import section
    import os
    # Response section
    status = False
    data = None

    try:
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status, None]


def show_emoji(strInput="", print_emoji=False):
    """
    Function which prints Emojis

    Usage: 
    print(show_emoji('thumbsup'))
    print("OK",show_emoji('thumbsup'))
    Default: thumbsup
    """
    import emoji

    # Response section
    status = False
    data = None

    try:
        if not strInput:
            data = emoji.emojize(":{}:".format(
                str('thumbsup').lower()), use_aliases=True, var="emoji_type")
            if print_emoji:
                print(data)
        else:
            data = emoji.emojize(":{}:".format(
                str(strInput).lower()), use_aliases=True, variant="emoji_type")
            if print_emoji:
                print(data)
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        return [status, data]


def print_with_magic_color(strMsg: str = "", magic: bool = False):
    """
    Function used for printing strings in color
    Args : Message (str): string which needs to be printed in color
        magic : (bool) :If each letter/character in the string is to be printed with different color
    Returns : None

    """
    import random
    from colored import fg, attr
    # Response section
    status = False
    data = None

    try:
        if magic == False:
            fg_random = random.randint(2, 255)

            while fg_random in [8, *range(15, 28), 22, 23, *range(51, 68), 77, *range(87, 99), 114, 149, *range(231, 250)]:
                fg_random = random.randint(2, 255)

            print('%s %s  %s' % (fg(fg_random), strMsg, attr(1)))
        else:
            for ch in strMsg:
                try:
                    fg_random = random.randint(2, 255)
                    while fg_random in [8, *range(15, 28), 22, 23, *range(51, 68), 77, *range(87, 99), 114, 149, *range(231, 250)]:
                        fg_random = random.randint(2, 255)
                    print('%s%s%s' %
                          (fg(fg_random), ch, attr(1)), sep='', end='')
                except:
                    print('%s' % (fg(1), attr('reset')), ch, sep='', end='')

        reset = attr('reset')
        print(reset)
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        return [status, data]


def install_package(package_name):
    """
    Function used to install python package
    Args : package_name (str): name of the package which needs to be installed
    Returns : None

    """
    import importlib

    # Response section
    status = False
    data = None

    try:
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            install_module(package_name)
        else:
            print("Package {} is already installed".format(package_name))
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        return [status, data]


def uninstall_package(package_name):
    """
    Function used to uninstall python package
    Args : package_name (str): name of the package which needs to be uninstalled
    Returns : None

    """
    import importlib

    # Response section
    status = False
    data = None

    try:
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            print("Package {} is not installed".format(package_name))
        else:
            uninstall_module(package_name)
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        return [status, data]


def api_request(url: str, method='GET', data: dict = None, headers: dict = None):
    """
    Function used to send generic api request
    Args : url (str): url of the api
        method (str): method of the api request
        data (dict): data to be sent in the request
        headers (dict): headers to be sent in the request
    Returns : None

    """
    import requests
    import json

    # Response section
    status = False
    data = None

    try:
        if headers is None:
            headers = {"charset": "utf-8", "Content-Type": "application/json"}

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers)
        elif method == 'POST':
            response = requests.post(
                url, data=json.dumps(data), headers=headers)
        elif method == 'PUT':
            response = requests.put(
                url, data=json.dumps(data), headers=headers)
        elif method == 'DELETE':
            response = requests.delete(
                url, data=json.dumps(data), headers=headers)
        else:
            raise Exception("Invalid method")

        if response.status_code in [200, 201, 202, 203, 204]:
            data = response.json()
        else:
            raise Exception(response.text)
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        return [status, data]


def image_to_text(image_path):

    status = False
    data = None

    try:
        import my_autopylot.Windows.functions.blackbox.BlackBox as BB
        status = True
        data = BB.Image_2_Text(image_path)
    except Exception as e:
        report_error(e)
    finally:
        return [status, data]
