import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--message', '-m', multiple=True, help="Auto Pylot Command Line Interface's basic command")
def main(message):
    """Auto Pylot Command Line Interface's basic command"""
    click.echo('\n'.join(message))
    click.echo(
        "Congratulations! You have successfully installed Auto Pylot Python Library!", color='green', )
    click.echo("\nAuto Pylot Python Library is a free and open-source software library that is designed to simplify the process of automating the development of Python projects.", color='green')
    # click.echo("Below commands are available for TERMINAL use :   ( W - Windows, U - Ubuntu )\n\n1)   dost         - [W,  ] || Build RPA Bots without Code.\n2)   bol          - [W, U] || Voice based assistant powered by ClointFusion.\n3)   cf_work      - [W,  ] || Get your computer usage report.\n4)   cf_tray      - [W,  ] || Launch ClointFusion tray icon.\n5)   cf_st        - [W, U] || Check your internet speed.\n6)   cf_wm        - [W,  ] || Sends WhatsApp messages by providing path of excel file having 3 columns: Mobile Number, Name, Message.\n7)   cf_py        - [W, U] || Opens a Python interpreter with 'import ClointFusion as cf' pre-loaded.\n8)   cf_like      - [W,  ] || CLI for auto liking CF's specific posts on Social Media.\n9)   cf_tour      - [W, U] || CLI for guided tour of ClointFusion.\n10)  cf_vlookup   - [W, U] || Performs excel_vlook_up on the given excel files for the desired columns.\n11)  cf_sm        - [W, U] || Opens all our ClointFusion's Social Media in Default Browser.")
