from components.store.history \
import see,save

while 1:
    commands = input(">_ ")
    save(commands)
    
    match commands:
        case 'history':
            print(see())
    