from time import localtime as date

def save_command(data_command : str) -> str:
    """\
        save commands at execution
    """
     
    with open("assets/data_save/data/history.txt","a") as new_history:
        new_history.write(f"{data_command}-------{date()[2]}/{date()[1]}/{date()[0]}_H-{date()[3]}:M-{date()[4]}:S-{date()[5]}\n")
        new_history.close()