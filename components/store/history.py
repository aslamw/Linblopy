def see():
    """
        see history commands
        
    Returns:
        string: list commands
    """
    try:
        historys = open('data/history.txt','r').read()
        return historys
    except:
        return 'history not exist'
    
def save(commands):
    """
        save commands

    Args:
        commands : data history 
    """
    
    import time
    
    date = f'{time.localtime()[2]}/{time.localtime()[1]}/{time.localtime()[0]}'
    open('data/history.txt','a').write(f'{commands} {date}\n')