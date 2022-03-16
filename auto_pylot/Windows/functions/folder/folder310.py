from auto_pylot.CrashHandler import report_error


def folder_read_text_file(txt_file_path=""):

    # Description:
    """
    Reads from a given text file and returns entire contents as a single list
    """

    # import section
    # Response section
    status = False
    data = None

    try:
        if not txt_file_path:
            raise Exception("Text file path is empty")

        with open(txt_file_path) as f:
            file_contents = f.readlines()
        data = file_contents

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status]


def folder_write_text_file(txt_file_path="", contents=""):
    # Description:
    """
    Description of the function
    """

    # import section

    # Response section
    status = False
    data = None

    try:

        if not txt_file_path:
            raise Exception("Text file path is empty")

        if not contents:
            raise Exception("Contents is empty")

        f = open(txt_file_path, 'w', encoding="utf-8")
        f.writelines(str(contents))
        f.close()

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status]


def folder_create(strFolderPath=""):
    # Description:
    """
    while making leaf directory if any intermediate-level directory is missing,
    folder_create() method will create them all.

    Parameters:
        folderPath (str) : path to the folder where the folder is to be created.

    For example consider the following path:

    """

    # import section
    import os
    # Response section
    status = False
    data = None

    try:
        if not strFolderPath:
            raise Exception("Folder path is empty")

        if not os.path.exists(strFolderPath):
            os.makedirs(strFolderPath, exist_ok=True)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status]


def folder_create_text_file(textFolderPath="", txtFileName="", custom=False):
    # Description:
    """
        Creates Text file in the given path.
        Internally this uses folder_create() method to create folders if the folder/s does not exist.
        automatically adds txt extension if not given in textFilePath.

        Parameters:
            textFilePath (str) : Complete path to the folder with double slashes.
        """

    # import section
    import os
    from pathlib import Path
    # Response section
    status = False
    data = None

    try:
        if not textFolderPath:
            raise Exception("Text file path is empty")

        if not txtFileName:
            raise Exception("Text file name is empty")

        if not custom:
            if ".txt" not in txtFileName:
                txtFileName = txtFileName + ".txt"

        if not os.path.exists(textFolderPath):
            folder_create(textFolderPath)

        file_path = os.path.join(textFolderPath, txtFileName)
        file_path = Path(file_path)

        f = open(file_path, 'w', encoding="utf-8")
        f.close()
        data = file_path

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status]


def folder_get_all_filenames_as_list(strFolderPath="", extension='all'):
    # Description:
    """
    Get all the files of the given folder in a list.

    Parameters:
        strFolderPath  (str) : Location of the folder.
        extension      (str) : extention of the file. by default all the files will be listed regarless of the extension.

    returns:
        allFilesOfaFolderAsLst (List) : all the file names as a list.
    """

    # import section
    import os
    # Response section
    status = False
    data = None

    try:
        if not strFolderPath:
            raise Exception("Folder path is empty")

        if extension == "all":
            allFilesOfaFolderAsLst = [
                f for f in os.listdir(strFolderPath)]
        else:
            allFilesOfaFolderAsLst = [f for f in os.listdir(
                strFolderPath) if f.endswith(extension)]

        data = allFilesOfaFolderAsLst

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status]


def folder_delete_all_files(fullPathOfTheFolder="", file_extension_without_dot="all", print_status=True):

    # Description:
    """
    Deletes all the files of the given folder

    Parameters:
        fullPathOfTheFolder  (str) : Location of the folder.
        extension            (str) : extention of the file. by default all the files will be deleted inside the given folder 
                                    regarless of the extension.
    returns:
        count (int) : number of files deleted.
    """

    # import section
    import os
    from pathlib import Path
    # Response section
    status = False
    data = None

    try:
        if not fullPathOfTheFolder:
            raise Exception("Folder path is empty")

        count = 0
        if "." not in file_extension_without_dot:
            file_extension_with_dot = "." + file_extension_without_dot

        if file_extension_with_dot.lower() == ".all":
            filelist = [f for f in os.listdir(fullPathOfTheFolder)]
        else:
            filelist = [f for f in os.listdir(
                fullPathOfTheFolder) if f.endswith(file_extension_with_dot)]

        for f in filelist:
            file_path = os.path.join(fullPathOfTheFolder, f)
            file_path = Path(file_path)
            os.remove(file_path)
            count += 1

        if print_status:
            print(filelist)
        data = count

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status]


def file_rename(old_file_path='', new_file_name='', print_status=True):
    # Description:
    """
    Renames the given file name to new file name with same extension
    """

    # import section
    import os
    from pathlib import Path
    # Response section
    status = False
    data = None

    try:
        if not old_file_path:
            raise Exception("Old file path is empty")

        if not new_file_name:
            raise Exception("New file name is empty")

        if os.path.exists(old_file_path):
            if new_file_name:
                ext = old_file_path.split('\\')[-1].split('.')[-1]
                path_of_new_file = os.path.join('\\'.join(old_file_path.split('\\')[
                                                :-1]), '.'.join([new_file_name, ext]))

                os.rename(src=Path(old_file_path),
                          dst=Path(path_of_new_file))
                if print_status:
                    print("File renamed successfully")
                    print(path_of_new_file)
                data = path_of_new_file
            else:
                raise Exception('new_file_name can\'t be empty.')
        else:
            raise Exception(
                'Old_file_path is invalid. Please pass a valid path.')

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status]


def file_get_json_details(path_of_json_file='', section=''):
    # Description:
    """
    Returns all the details of the given section in a dictionary
    """

    # import section
    import json
    # Response section
    status = False
    data = None

    try:
        if not path_of_json_file:
            raise Exception("Path of json file is empty")

        if not section:
            raise Exception("Section is empty")

        # import json

        with open(path_of_json_file, 'r') as fp:
            data = json.load(fp)
        fp.close()

        if section in list(data.keys()):
            data = data.get(section)
        else:
            raise Exception(
                'Section can\'t be find in given json file.')

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    except Exception as e:
        report_error(e)

    else:
        status = True
    finally:
        if status == True and data != None:
            return [status, data]
        return [status]
