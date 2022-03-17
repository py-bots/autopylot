from typing import Union
import os
import sys
import pathlib
import time
from my_autopylot import CrashHandler

from my_autopylot.CrashHandler import report_error


def playsound(sound: Union[str, pathlib.Path], block=True) -> None:
    from ctypes import c_buffer, windll
    from random import random

    sound = str(sound)
    if hasattr(sys.modules['__main__'], "__file__"):
        sound = os.path.join(os.path.dirname(
            sys.modules['__main__'].__file__), str(sound))

    def winCommand(*command):
        buf = c_buffer(255)
        command = ' '.join(command).encode(sys.getfilesystemencoding())
        errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
        if errorCode:
            errorBuffer = c_buffer(255)
            windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
            exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                                '\n        ' + command.decode() +
                                '\n    ' + errorBuffer.value.decode())
            report_error(Exception(exceptionMessage))
        return buf.value

    alias = 'playsound_' + str(random())
    winCommand('open "' + sound + '" alias', alias)
    winCommand('set', alias, 'time format milliseconds')
    durationInMS = winCommand('status', alias, 'length')
    winCommand('play', alias, 'from 0 to', durationInMS.decode())

    if block:
        time.sleep(float(durationInMS) / 1000.0)

    winCommand('close', alias)


def speech_to_text():

    # import section
    try:
        import pyaudio
    except Exception as ex:
        report_error(ex)
    import speech_recognition as sr
    import sys

    """
    Speech to Text using Google's Generic API
    """

    recognizer = sr.Recognizer()
    energy_threshold = [3000]

    unknown = False

    try:
        while True:
            with sr.Microphone() as source:
                recognizer.dynamic_energy_threshold = True
                if recognizer.energy_threshold in energy_threshold or recognizer.energy_threshold <= \
                        sorted(energy_threshold)[-1]:
                    recognizer.energy_threshold = sorted(
                        energy_threshold)[-1]
                else:
                    energy_threshold.append(
                        recognizer.energy_threshold)

                recognizer.pause_threshold = 0.8

                recognizer.adjust_for_ambient_noise(source)

                audio = recognizer.listen(source)

                try:
                    if not unknown:
                        print("Speak now !!!")
                    query = recognizer.recognize_google(audio)
                    print("You said :", query)
                    return query
                except AttributeError:
                    text_to_speech(
                        "Could not find PyAudio or no Microphone input device found. It may be being used by "
                        "another "
                        "application.")
                    sys.exit()
                except sr.UnknownValueError:
                    unknown = True
                except sr.RequestError as e:
                    print("Try Again")

                # Windows OS - Python 3.8
    except Exception as ex:
        report_error(ex)


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
        r = random.randint(1, 20000000)
        audio_file = 'auto_pylot_audio' + str(r) + '.mp3'
        tts.save(audio_file)  # save as mp3
        playsound(audio_file)  # play the audio file
        os.remove(audio_file)  # remove audio file

    except Exception as ex:
        report_error(ex)

    else:
        status = True
    finally:
        return status
