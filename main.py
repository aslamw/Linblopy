import os

from assets.data_save.save import save_command

def command():
    """\
        first line command
                19/06/2022    
    """
    line_command : str = input('_>')
    save_command(line_command)
    
while True:
    command()