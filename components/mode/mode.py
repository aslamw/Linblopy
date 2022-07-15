def mode_type(commands):
    """
        type mode

    Args:
        commands (_type_): _description_
    """
    try:
        mode = open('data/mode.dll','r').read()
        
        match mode:
            case 'easy':
                text = dict(
                    home = '-digite um comando na dúvida manda um help- >_ ',
                    mode = '-escolha o modo na dúvida manda um help- >_ ',
                    job = '-manda a boa na dúvida manda um help >_ -'
                )
            case 'r':
                text = '>_ '
    except:
        print('mode not exist')