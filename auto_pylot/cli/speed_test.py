import random
import os
import click

from auto_pylot.CheckSystem import os_name, windows_os, contribution_messages, python_exe_path
from auto_pylot.CrashHandler import report_error

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
def main():
    """CLI for testing internet bandwidth using speedtest.net"""
    try:
        if os_name == windows_os:
            import subprocess
            import sys
            print(subprocess.call([sys.executable, "-m", "speedtest"]))
        else:
            # try:
            #     print(os.system("speedtest-cli"))
            # except:
            print(
                "This feature is curently not supported on macOS. Please contribute to make the tomorrow better.")
            print(random.choice(contribution_messages))
    except Exception as ex:
        report_error(ex)
