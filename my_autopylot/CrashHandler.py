import traceback
import sys
import os
from typing import Union
import pathlib
import time


def _canonicalizePath(path):
    """
    Support passing in a pathlib.Path-like object by converting to str.
    """
    import sys
    if sys.version_info[0] >= 3:
        return str(path)
    else:
        # On earlier Python versions, str is a byte string, so attempting to
        # convert a unicode string to str will fail. Leave it alone in this case.
        return path


def playsound(sound, block=True):

    sound = '"' + _canonicalizePath(sound) + '"'

    from ctypes import create_unicode_buffer, windll, wintypes
    from time import sleep
    windll.winmm.mciSendStringW.argtypes = [
        wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.UINT, wintypes.HANDLE]
    windll.winmm.mciGetErrorStringW.argtypes = [
        wintypes.DWORD, wintypes.LPWSTR, wintypes.UINT]

    def winCommand(*command):
        bufLen = 600
        buf = create_unicode_buffer(bufLen)
        command = ' '.join(command)
        # use widestring version of the function
        errorCode = int(windll.winmm.mciSendStringW(
            command, buf, bufLen - 1, 0))
        if errorCode:
            errorBuffer = create_unicode_buffer(bufLen)
            # use widestring version of the function
            windll.winmm.mciGetErrorStringW(errorCode, errorBuffer, bufLen - 1)
            exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                                '\n        ' + command +
                                '\n    ' + errorBuffer.value)
            raise Exception(exceptionMessage)
        return buf.value

    try:
        winCommand(u'open {}'.format(sound))
        winCommand(u'play {}{}'.format(sound, ' wait' if block else ''))
    finally:
        try:
            winCommand(u'close {}'.format(sound))
        except Exception:
            # If it fails, there's nothing more that can be done...
            pass


def text_to_speech(audio, show=True):

    # import section
    import random
    from gtts import gTTS  # Google Text to Speech
    import os

    status = False

    try:
        if show:
            if type(audio) is list:
                print(' '.join(audio))
            else:
                print(str(audio))
        tts = gTTS(text=audio, lang='en', tld='co.in')  # text to speech(voice)
        r = random.randint(1, 20000000)  # random number
        audio_file = 'cloint_audio_' + str(r) + '.mp3'  # audio file name
        # path to save the audio file
        file_path = os.path.join(os.getcwd(), audio_file)
        tts.save(file_path)  # save as mp3
        playsound(file_path)  # play audio
        os.remove(file_path)  # remove audio file
    except Exception as ex:
        print(str(ex))
    else:
        status = True
    finally:
        return status


def install_module(module_name):
    try:
        import subprocess
        subprocess.call([sys.executable, "-m", "pip",
                        "uninstall", module_name])
    except:
        text_to_speech("Sorry, I could not install the module {}".format(
            module_name))


def uninstall_module(module_name):
    try:
        if module_name != "my_autopylot":
            import subprocess
            subprocess.call([sys.executable, "-m", "pip",
                            "uninstall", "-y", module_name])
        else:
            text_to_speech("You cannot uninstall my_autopylot from here.")
    except:
        text_to_speech("Sorry, I could not uninstall the module {}".format(
            module_name))


def install_pyaudio():
    import sys
    import subprocess
    _version_1 = str(sys.version_info.major) + str(sys.version_info.minor)

    if _version_1 == "37":
        _version_2 = "37m"
    else:
        _version_2 = _version_1

    _module = f"https://raw.githubusercontent.com/py-bots/my-autopylot/main/support/whls/PyAudio-0.2.11-cp{_version_1}-cp{_version_2}-win_amd64.whl"
    subprocess.call([sys.executable, "-m", "pip", "install", _module])


def report_error(ex: Exception):

    exception_name = type(ex).__name__
    exception_message = str(ex)

    if "SystemExit" in exception_name:
        text_to_speech("Exiting!")

    elif "KeyboardInterrupt" in exception_name:
        text_to_speech("Quitting ! you have hit the interrupt key. Look at line number {}".format(
            exception_line))

    elif "GeneratorExit" in exception_name:
        text_to_speech(
            "Seems the generator or coroutine is closed. Look at line number {}".format(
                exception_line))

    elif "StopIteration" in exception_name:
        text_to_speech(
            "There are no further items produced by the iterator. Look at line number {}".format(
                exception_line))

    elif "StopAsyncIteration" in exception_name:
        text_to_speech(
            "There are no further items produced by the asynchronous iterator. Look at line number {}".format(
                exception_line))

    elif "FloatingPointError" in exception_name:
        text_to_speech(
            "The value is not a floating point number. Look at line number {}".format(
                exception_line))

    elif "OverflowError" in exception_name:
        text_to_speech(
            "The value is too large to be stored in the data type. Look at line number {}".format(
                exception_line))

    elif "ZeroDivisionError" in exception_name:
        text_to_speech(
            "The second argument of a division or modulo operation is zero. Look at line number {}".format(
                exception_line))

    elif "AssertionError" in exception_name:
        text_to_speech("The assertion failed. Look at line number {}".format(
            exception_line))

    elif "AttributeError" in exception_name:
        text_to_speech("The attribute is not found. Look at line number {}".format(
            exception_line))

    elif "BufferError" in exception_name:
        text_to_speech("The buffer is too small. Look at line number {}".format(
            exception_line))

    elif "EOFError" in exception_name:
        text_to_speech(
            "The input function has hit an end-of-file condition without reading any data. Look at line number {}".format(
                exception_line))

    elif "ModuleNotFoundError" in exception_name:
        text_to_speech(
            "Sorry, module could not be located. Look at line number {}".format(
                exception_line))

    elif "IndexError" in exception_name:
        text_to_speech(
            "The sequence subscript is out of range. Look at line number {}".format(
                exception_line))

    elif "KeyError" in exception_name:
        text_to_speech(
            "Oops, mapping dictionary key is not found in the set of existing keys. Look at line number {}".format(
                exception_line))

    elif "MemoryError" in exception_name:
        text_to_speech(
            "Huh, operation is running out of memory. Look at line number {}".format(
                exception_line))

    elif "UnboundLocalError" in exception_name:
        text_to_speech(
            "The local variable has not been bound to an object. Look at line number {}".format(
                exception_line))

    elif "BlockingIOError" in exception_name:
        text_to_speech(
            "The I/O operation is in progress. Look at line number {}".format(
                exception_line))

    elif "ChildProcessError" in exception_name:
        text_to_speech(
            "The operation on a child process failed. Look at line number {}".format(
                exception_line))

    elif "BrokenPipeError" in exception_name:
        text_to_speech("The pipe has been broken. Look at line number {}".format(
            exception_line))

    elif "ConnectionAbortedError" in exception_name:
        text_to_speech(
            "The connection has been aborted by the peer. Look at line number {}".format(
                exception_line))

    elif "ConnectionRefusedError" in exception_name:
        text_to_speech(
            "The connection was refused by the peer. Look at line number {}".format(
                exception_line))

    elif "ConnectionResetError" in exception_name:
        text_to_speech(
            "The connection was reset by the peer. Look at line number {}".format(
                exception_line))

    elif "FileExistsError" in exception_name:
        text_to_speech(
            "The file or directory already exists. Look at line number {}".format(
                exception_line))

    elif "FileNotFoundError" in exception_name:
        text_to_speech(
            "The file or directory cannot be found. Look at line number {}".format(
                exception_line))

    elif "InterruptedError" in exception_name:
        text_to_speech("The operation was interrupted. Look at line number {}".format(
            exception_line))

    elif "IsADirectoryError" in exception_name:
        text_to_speech(
            "File operation is requested on a directory. Look at line number {}".format(
                exception_line))

    elif "NotADirectoryError" in exception_name:
        text_to_speech(
            "Directory operation is requested on a file. Look at line number {}".format(
                exception_line))

    elif "PermissionError" in exception_name:
        text_to_speech(
            "The operation is not permitted without the adequate access rights. Look at line number {}".format(
                exception_line))

    elif "ProcessLookupError" in exception_name:
        text_to_speech("The process cannot be found. Look at line number {}".format(
            exception_line))

    elif "TimeoutError" in exception_name:
        text_to_speech("The operation has timed out. Look at line number {}".format(
            exception_line))

    elif "ReferenceError" in exception_name:
        text_to_speech(
            "Oops, you are trying to access an attribute of the referent after it has been garbage collected. Look at line number {}".format(
                exception_line))

    elif "NotImplementedError" in exception_name:
        text_to_speech(
            "The operation is not implemented. Look at line number {}".format(
                exception_line))

    elif "RecursionError" in exception_name:
        text_to_speech(
            "Seems, maximum recursion depth is exceeded. Look at line number {}".format(
                exception_line))

    elif "IndentationError" in exception_name:
        text_to_speech(
            "The indentation of the code is incorrect. Look at line number {}".format(
                exception_line))

    elif "SystemError" in exception_name:
        text_to_speech(
            "Internal error, the system has failed. Look at line number {}".format(
                exception_line))

    elif "TypeError" in exception_name:
        text_to_speech(
            "The operation cannot be performed on the given data type. Look at line number {}".format(
                exception_line))

    elif "UnicodeEncodeError" in exception_name:
        text_to_speech(
            "The data cannot be encoded in the specified encoding. Look at line number {}".format(
                exception_line))

    elif "UnicodeDecodeError" in exception_name:
        text_to_speech(
            "The data cannot be decoded in the specified encoding. Look at line number {}".format(
                exception_line))

    elif "UnicodeTranslateError" in exception_name:
        text_to_speech(
            "The data cannot be translated to the specified encoding. Look at line number {}".format(
                exception_line))

    else:
        from my_autopylot.Windows.functions.BlackBox.BlackBox import Report_Developer
        try:
            Report_Developer(ex)
        except:
            pass
        text_to_speech("You got a {}. It describes as {}.".format(
            exception_name, exception_message))
