import string #gör så att man kna indexera ur alfabetet 
#' O ' innebär Bom
#' X ' innebär träff
#' _ ' innebär vatten
#f' {siffra}{bokstav}' är en del av ett skepp där siffran representerar skeppets -
#- längd och bokstaven skiljer lika långa skepp åt
def splash():
    print()
    print(' /$$   /$$ /$$$$$$ /$$$$$$$  /$$$$$$$$      /$$$$$   /$$  /$$ /$$$$$$        /$$$$$  /$$$$$$ /$$   /$$ /$$   /$$')
    print('| $$  | $$|_  $$_/| $$__  $$| $$_____/     /$$___$$ | $$$| $$| $$_  $$      /$$_  $$|_  $$_/| $$$ | $$| $$  /$$/')
    print('| $$  | $$  | $$  | $$  \ $$| $$          | $$   \$$| $$$| $$| $$  \ $$    | $$ \__/  | $$  | $$$$| $$| $$ /$$/ ')
    print('| $$$$$$$$  | $$  | $$  | $$| $$$$$       | $$$$$$$$| $$$$ $$| $$  | $$    |  $$$$    | $$  | $$ $$ $$| $$$$$/  ')
    print('| $$__  $$  | $$  | $$  | $$| $$__/       | $$__  $$| $$ $$$$| $$  | $$     \__  $$   | $$  | $$  $$$$| $$  $$  ')
    print('| $$  | $$  | $$  | $$  | $$| $$          | $$  | $$| $$\ $$$| $$  | $$    /$$ | $$   | $$  | $$\  $$$| $$\  $$ ')
    print('| $$  | $$ /$$$$$$| $$$$$$$/| $$$$$$$$    | $$  | $$| $$ \ $$| $$$$$$$/    | $$$$$/  /$$$$$$| $$ \  $$| $$ \  $$')
    print('|__/  |__/|______/|_______/ |________/    |__/  |__/|__/  \_/|_______/      \____/  |______/|__/  \__/|__/  \__/')
    print()
    print('                                          -A TURN BASED  STRATEGY GAME-')
    print()
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⠀⠀⠀         ⠀⠀⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠇⠸⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣇⣀     ⠀ ⠀ ⠀⠀⠀⠀⠀⠀  ⠀⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇⠸⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣸⣇⣀⡀        ⠀     ⠀   ⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⡆⢰⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢹⡏⠉⠉        ⠀     ⠀   ⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡁⢠⣤⣤⣤⣤⡄⢈⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠀⠀⠀⠀ ⠀⠀⠀⠀⠸⢾⡟⠛⠛⠛⠛⢻⡷⠇     ⠀⠀         ⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠛⢋⣠⠀⠙⠛⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀ ⠀⠀⠀⠀  ⠀⠀⠀⠀⣾⣤⡴⠟⣿⣦⣤⣷       ⠀         ⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣴⡀⢈⣿ ⢸⣷  ⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      ⠀⠀  ⢰⡟⠋⢿⡷⠀⣿⡇⠈⣿⣿⡆   ⠀     ⠀⠀ ⠀ ⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⠀  ⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⠁⠀⠀ ⠀      ⠀   ⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀   ⠀ ⠀⠀⠀⠀⢻⡀⠀ ⠀⣿⣿⣿⣿⡟⠀⠀⠀⠀      ⠀  ⠀ ⢸')
    print('              ⣿⣿⣿⣿⣿⠿⠿⠿⠿⠟⠃⠘⠛⠛⠛⠀ ⠀⠀⣠⠛⠛⠿⠿⠿⠛⣿⣿⣿⣿⣿⠀⠀  ⠀⣀⣀⣀⣀⣠⣼⣧⣤⣤⣿⣿⣿⣿⣧⣤⣤⣤⣀⣀⣀⣤⠀⠀⠀   ⢸')
    print('              ⣿⣿⣧⣤⣤⣤⣶⣶⣶⣶⣦⣤⣤⣈⣉⡉⠙⠛⠛⠛⠋⢉⣀⣠⣤⣴⣾⣿⣿⣿⠀⠀ ⠘⠛⠛⠛⠉⠉⠉⠉⠙⠛⠛⠷⠶⢶⣦⣤⣤⣤⣴⡶⠿⠟⠛⠋⠁⠀⠀ ⢸')
    print('              ⣿⣿⣿⣿⣿⣤⣤⣤⣤⣄⣈⣉⣉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⢉⣉⣉⣿⣿⣿⣿⠀⠀ ⠀⠀⠀⠛⠛⠛⠛⠻⠷⠶⠶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⡶⠶⠶⠀⠀⠀  ⢸')
    print('              ⣿⡟⢉⣉⣉⣀⣤⣤⣄⣈⣉⡉⠛⠛⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀ ⢠⡶⠶⠶⠿⠛⠛⠻⠷⠶⢶⣤⣤⣤⣤⣤⡄⠀⠀      ⠀⠀⠀    ⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                          ⢸')
    print('              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀           ⠀   ⠀                   ⠀   ⢸')
    print()
    input('                                               Press enter to begin')
    print()

def print_player_won1():
    print("### ##   ####       ##     ##  ##   ### ###  ### ##               ##             ##   ##   ## ##   ###  ##")  
    print(" ##  ##   ##         ##    ##  ##    ##  ##   ##  ##             ###             ##   ##  ##   ##    ## ##")  
    print(" ##  ##   ##       ## ##   ##  ##    ##       ##  ##              ##             ##   ##  ##   ##   # ## #")  
    print(" ##  ##   ##       ##  ##   ## ##    ## ##    ## ##               ##             ## # ##  ##   ##   ## ##")   
    print(" ## ##    ##       ## ###    ##      ##       ## ##               ##             # ### #  ##   ##   ##  ##")  
    print(" ##       ##  ##   ##  ##    ##      ##  ##   ##  ##              ##              ## ##   ##   ##   ##  ##")  
    print("####     ### ###  ###  ##    ##     ### ###  #### ##             ####            ##   ##   ## ##   ###  ##")
    


def print_player_won2():
    print("### ##   ####       ##     ##  ##   ### ###  ### ##            ## ##             ##   ##   ## ##   ###  ##")  
    print(" ##  ##   ##         ##    ##  ##    ##  ##   ##  ##           ##  ##            ##   ##  ##   ##    ## ##")  
    print(" ##  ##   ##       ## ##   ##  ##    ##       ##  ##               ##            ##   ##  ##   ##   # ## #")
    print(" ##  ##   ##       ##  ##   ## ##    ## ##    ## ##               ##             ## # ##  ##   ##   ## ##")   
    print(" ## ##    ##       ## ###    ##      ##       ## ##              ##              # ### #  ##   ##   ##  ##") 
    print(" ##       ##  ##   ##  ##    ##      ##  ##   ##  ##            #   ##            ## ##   ##   ##   ##  ##")  
    print("####     ### ###  ###  ##    ##     ### ###  #### ##           ######            ##   ##   ## ##   ###  ##")

def game_over_splash():
     print(" ##      #    #   #  ####           ##    #  #   ####   ###")  
     print("#  #    # #   ## ##  #             #  #   #  #   #      #  #")  
     print("#      #   #  # # #  ###           #  #   #  #   ###    #  #")  
     print("# ##   #####  # # #  #             #  #   ####   #      ###")   
     print("#  #   #   #  #   #  #             #  #    ##    #      #  #")  
     print(" ##    #   #  #   #  ####           ##     ##    ####   #  #")  



#De båda spelarnas skepp. Funktionen tar fem argument, varje argument är en siffra som -
#- bestämmer hur många av en skeppstyp som ska läggas till i varje spelares inventarie. -
#- Skeppen ökar (i längd) från 1 till 5 från vänster till höger (första argumentet är för skepp av längd ett osv.
def player_inventory(shipslen2,shipslen3,shipslen4,shipslen5):
    p1inventory=[]
    p2inventory=[]
    for i in range(shipslen2):
        p1inventory=p1inventory+[f' 2{string.ascii_uppercase[i]}']
        p2inventory=p2inventory+[f' 2{string.ascii_uppercase[i]}']
    for i in range(shipslen3):
        p1inventory=p1inventory+[f' 3{string.ascii_uppercase[i]}']
        p2inventory=p2inventory+[f' 3{string.ascii_uppercase[i]}']
    for i in range(shipslen4):
        p1inventory=p1inventory+[f' 4{string.ascii_uppercase[i]}']
        p2inventory=p2inventory+[f' 4{string.ascii_uppercase[i]}']
    for i in range(shipslen5):
        p1inventory=p1inventory+[f' 5{string.ascii_uppercase[i]}']
        p2inventory=p2inventory+[f' 5{string.ascii_uppercase[i]}']
    return p1inventory,p2inventory

    
#De båda spelarnas spelplaner av valbar storlek. Funktionen tar ett positivt heltal som argument -
#- Detta heltal avgör antalet koordinater spelplanerna ska ha i x- samt y-led.
def make_maps(size):
    p1=[[' _ ' for _ in range(size)] for _ in range(size)]
    p2=[[' _ ' for _ in range(size)] for _ in range(size)]
    return p1,p2

#Gör om en spelplan till en lista där varje element representerar en rad i koordinatsystemet. -
#- kolumnerna på varje rad skrivs ihop till en sträng. i print_my_map() visas skeppen på kartan.
def print_my_map(player_map):
    y_coord_str=['' for _ in range(len(player_map))]
    for y in range(len(player_map)):
        for x in range(len(player_map)):
            y_coord_str[y]=y_coord_str[y]+player_map[y][x]
    return y_coord_str

# Denna funktion liknar print_my_map med skillnaden att båtar inte visas här
def print_map(player_map):
    y_coord_str=['' for _ in range(len(player_map))]
    for y in range(len(player_map)):
        for x in range(len(player_map)):
            if player_map[y][x]!=' X 'and player_map[y][x]!=' O 'and player_map[y][x]!=' _ ':
                y_coord_str[y]=y_coord_str[y]+' _ '
            else:
                y_coord_str[y]=y_coord_str[y]+player_map[y][x]
    return y_coord_str

#Skriver ut ett koordinatsystem av en spelplan där båtar INTE syns
def view_map(player_map):
    xrow=str()
    print('Enemy map')
    for nr in range(len(player_map)):
        if nr>8:
            xrow=xrow+(f' {nr+1}')
        else:
            xrow=xrow+(f' {nr+1} ')
    print(f'   {xrow}')
    for nr in range(len(player_map)):
        if nr>8:
            print(f'{nr+1} {print_map(player_map)[nr]}')
        else:
            print(f'{nr+1}  {print_map(player_map)[nr]}')

#Skriver ut ett koordinatsystem av en spelplan där båtar syns
def view_my_map(player_map):
    print('My map')
    xrow=str()
    for nr in range(len(player_map)):
        if nr>8:
            xrow=xrow+(f' {nr+1}')
        else:
            xrow=xrow+(f' {nr+1} ')
    print(f'   {xrow}')
    for nr in range(len(player_map)):
        if nr>8:
            print(f'{nr+1} {print_my_map(player_map)[nr]}')
        else:
            print(f'{nr+1}  {print_my_map(player_map)[nr]}')

#Denna funktion ändrar element i en spelplan beroende på om ett skepp finns i det elementet eller inte.
def shoot_coord(prompt,player_map,x,y):
    if player_map[y][x]==' X 'or player_map[y][x]==' O ':
        next_frame()
        print('You can not shoot at the same coordinate twice. Try again.')
        return guess_coord(prompt,player_map)
    if player_map[y][x]==' _ ':
        player_map[y][x]=' O '
        return 'Miss!'
    else:
        träff=player_map[y][x]
        player_map[y][x]=' X '
        for y in range(len(player_map)):
            for x in range(len(player_map)):
                if player_map[y][x]==träff:
                    return 'Hit!'
        return 'Ship sunken!'

#Funktionen sorterar bort input som inte är siffror
def parse_coord(string):            
    if string.isnumeric()==True:
        return(int(string))
    else:
        return None

#Låter spelaren skriva in en koordinat och kontrollerar mha parse_coord() och coord_on_map() att -
#- koordinaten är giltig, anropar isf shoot_coord()
def guess_coord(prompt,player_map):
    x=parse_coord(input(f'{prompt} x-coordinate: '))
    y=parse_coord(input(f'{prompt} y-coordinate: '))
    if x==None or y==None:
        next_frame()
        print('Invalid coordinate input')
        print('Try again')
        return guess_coord(prompt,player_map)
    if coord_on_map(x,y,player_map)==True:
        next_frame()
        print(f'{x,y}')
        x=x-1
        y=y-1
        return shoot_coord(prompt,player_map,x,y)
    else:
        next_frame()
        print('Invalid coordinate input')
        print('Try again')
        return guess_coord(prompt,player_map)

#Kontrollerar om spelaren har skepp kvar att placera ut 
def have_ship(inventory):
    return len(inventory)>0

#Genom att kolla vilken siffra skeppet har berättar den här funktionen hur lång ett skepp är
def len_ship(inventory):
    if len(inventory)==1 and inventory[0]==' 1A':
        return 0
    else:
        return int(inventory[-1][1])
    
#Avgör om en koordinat är på en karta/spelplan.
def coord_on_map(x,y,player_map):
    return 0<=x-1<len(player_map) and 0<=y-1<len(player_map)

#Avgör om en koordinat redan har ett skepp på sig
def coord_empty(x,y,player_map):
    return player_map[y-1][x-1]==' _ '

#Avgör om skeppet i fråga får plats åt något håll i x-led utifrån startkoordinaten
def room_for_shipx(x,y,inventory,player_map):
    if player_map[y-1][x-1:x-1+len_ship(inventory)]==[' _ ' for _ in range(len_ship(inventory))]or player_map[y-1][x-(len_ship(inventory)):x]==[' _ ' for _ in range(len_ship(inventory))]:
        return True
    else:
        return False

#Avgör om skeppet i fråga får plats nedåt i y-led utifrån startkoordinaten
def room_for_ship_pos_y(x,y,inventory,player_map):
    for _ in range(y-1,y-1+len_ship(inventory)):
        if player_map[_][x-1]!=' _ ':
            return False
        else:
            return True
        
#Avgör om skeppet i fråga får plats uppåt i y-led utifrån startkoordinaten
def room_for_ship_neg_y(x,y,inventory,player_map):
    for _ in range(y-1,y-1-(len_ship(inventory))):
        if player_map[_][x-1]!=' _ ':
            return False
        else:
            return True

#Hard work pays of! Denna funktion låter dig placera skepp av längder över 1, lodrätt och diagonalt
def place_ship(prompt,inventory,player_map):
    view_my_map(player_map)
    while have_ship(inventory):
        print(f"Remaining ships: {inventory}")
        ship=inventory[-1]
        xstart=parse_coord(input(f'{prompt} start of {ship} at x-coordinate: '))
        ystart=parse_coord(input(f'{prompt} start of {ship} at y-coordinate: '))
        if xstart==None or ystart==None:                                       #kollar om input är en siffra
            next_frame()
            print('Invalid coordinate input. Try again.')
            return place_ship(prompt,inventory,player_map)
        if coord_on_map(xstart,ystart,player_map)==True:                       #kollar om koordinaten finns på spelplanen
            if coord_empty(xstart,ystart,player_map)==True:                    #kollar så att platsen är ledig
                if room_for_shipx(xstart,ystart,inventory,player_map)==True or room_for_ship_pos_y(xstart,ystart,inventory,player_map)==True or room_for_ship_neg_y(xstart,ystart,inventory,player_map)==True:  #kollar om skeppet får plats åt något håll
                    print(f'({xstart},{ystart})')
                else:
                    next_frame()
                    print('The ship you are trying to place does not fit. Try again.')
                    return place_ship(prompt,inventory,player_map)
            else:
                next_frame()
                print('A ship is already placed at this coordinate. Try again.')
                return place_ship(prompt,inventory,player_map)
        else:
            next_frame()
            print('Invalid coordinate input. Try again.')
            return place_ship(prompt,inventory,player_map)
        xend=parse_coord(input(f'{prompt} end of {ship} at x-coordinate: '))
        yend=parse_coord(input(f'{prompt} end of {ship} at y-coordinate: '))
        if xend==None or yend==None:
            next_frame()
            print('Invalid coordinate input')
            print('Try again')
            return place_ship(prompt,inventory,player_map)
        if coord_on_map(xend,yend,player_map)==True:
            if yend==ystart or xend==xstart:            #En av dessa måste stämma, annars har skeppet placerats diagonalt vilket fakkar koden
                if xstart==xend:                        #om båten är placerad lodrätt
                    if abs(ystart-yend)==len_ship(inventory)-1:   #om avståndet (absolutbeloppet) mellan start- och slutkoordinat är samma som skeppets längd
                        print(f'({xend},{yend})')
                        ship=inventory.pop()                   #Här poppas skeppet av från inventariet och tilldelas till variabeln ship
                        if ystart<yend:
                            for y in range(ystart-1,yend):        #Varje koordinat mellan och inkl start- till slutkoordinat får värdet av variabeln ship 
                                player_map[y][xstart-1]=ship
                        else:
                            for y in range(yend-1,ystart):        
                                player_map[y][xstart-1]=ship
                        view_my_map(player_map)
                    elif abs(ystart-yend)<len_ship(inventory)-1:
                        next_frame()
                        print('The given coordinates are too close together. Try again.')
                        return place_ship(prompt,inventory,player_map)
                    elif abs(ystart-yend)>len_ship(inventory)-1:
                        next_frame()
                        print('The given coordinates are too far apart. Try again.')
                        return place_ship(prompt,inventory,player_map)
                if ystart==yend:                                   #om båten är placerad vågrätt
                    if abs(xstart-xend)==len_ship(inventory)-1:    #om avståndet mellan start- och slutkoordinat är samma som skeppets längd
                        if room_for_shipx(xstart,ystart,inventory,player_map): #kolla om skeppet får plats i x-led
                            print(f'({xend},{yend})')
                            ship=inventory.pop()                   #Här poppas skeppet av från inventariet och tilldelas till variabeln ship
                            if xstart<xend:
                                for x in range(xstart-1,xend):         #Varje koordinat mellan och inkl start- till slutkoordinat får värdet av variabeln ship 
                                    player_map[ystart - 1][x]=ship
                            else:
                                for x in range(xend-1,xstart):
                                    player_map[ystart - 1][x]=ship
                            view_my_map(player_map)
                        else:
                            next_frame()
                            print('The ship you are trying to place does not fit. Try again.')
                            return place_ship(prompt,inventory,player_map)
                    elif abs(xstart-xend)<len_ship(inventory)-1:
                        next_frame()
                        print('The given coordinates are too close together. Try again.')
                        return place_ship(prompt,inventory,player_map)
                    elif abs(xstart-xend)>len_ship(inventory)-1:
                        next_frame()
                        print('The given coordinates are too far apart. Try again.')
                        return place_ship(prompt,inventory,player_map)
            else:
                next_frame()
                print('Ship can not ba placed diagonally. Try again.')
                return place_ship(prompt,inventory,player_map)
        else:
            next_frame()
            print('Invalid coordinate input. Try again.')
            return place_ship(prompt,inventory,player_map)
    print('No more ships to place.')
    return False

def anti_cheating():
    input("Press enter to end turn: ")
    next_frame()
    input("Press enter to begin turn: ")
    next_frame()

def has_player_lost(player_map):
    valid_elements = [" _ ", " X ", " O "]

    for row in player_map:
        for element in row:
            if element not in valid_elements:
                return None
    
    return "Player_has_won"


    
def play_again():
    yes_no = input("Do you want to play again?: (yes/no) ").lower()
    
    if yes_no == "yes":
        return True
    if yes_no == "no":
        return False
    next_frame()
    return play_again()

def ship_input(shipsize,mapsize):
    ship=parse_coord(input(f'Choose amount of ships with length {shipsize}: '))
    if ship==None or ship>(mapsize**2)/2:
        next_frame()
        print('Invalid size input')
        print('Try again')
        return ship_input(shipsize)
    return ship

def shots_input(mapsize):
    shots=parse_coord(input('Choose shots per round: '))
    if shots==None or shots<1 or shots>(mapsize**2)/2:
        next_frame()
        print('Invalid amount')
        print('Try again')
        return shots_input(mapsize)
    return shots

def custom():
    input("Press enter to start game")
    print()
    while True:
        print("Map size can't be over 20")
        mapsize=parse_coord(input('Choose map size: '))
        if mapsize==None or mapsize>20:
            next_frame()
            print('Invalid size input')
            print('Try again')
            return custom()
        p1,p2=make_maps(mapsize)
        view_map(p1)
        print()
        print("The total area coverd by ships can't be more than 50% of the map")
        b2=ship_input(2,mapsize)
        b3=ship_input(3,mapsize)
        b4=ship_input(4,mapsize)
        b5=ship_input(5,mapsize)
        p1inventory,p2inventory=player_inventory(b2,b3,b4,b5)
        print(p1inventory)
        print(p2inventory)
        print()
        print("The amount of shots per round can't be more than 50% of the map")
        shots=shots_input(mapsize)
        print()
        place_ship('Place', p1inventory, p1)
        anti_cheating()
        place_ship('Place', p2inventory, p2)
        play = True
        
        while play == True:
            anti_cheating()
            for x in range(shots):
                print("Player 1")
                view_my_map(p1)
                view_map(p2)
                print(guess_coord('Shoot at',p2))
                if has_player_lost(p2)=="Player_has_won" :
                    game_over_splash()
                    print_player_won1()
                    play = False  
                    return None
            anti_cheating()
            for x in range(shots):
                print("Player 2")
                view_my_map(p2)
                view_map(p1)
                print(guess_coord('Shoot at',p1))
                if has_player_lost(p1)== "Player_has_won":
                    game_over_splash()
                    print_player_won2()
                    play = False
                    return None
        break
        
def normal():
    while True:
        input("press enter to start game")
        p1,p2=make_maps(10)
        p1inventory,p2inventory=player_inventory(1,2,1,1)
        print('Player 1')
        place_ship('Place', p1inventory, p1)
        anti_cheating()
        print('Player 2')
        place_ship('Place', p2inventory, p2)
        
        play = True
        while play == True:
            anti_cheating()
            print("Player 1")
            view_my_map(p1)
            view_map(p2)
            print(guess_coord('Shoot at',p2))
            view_my_map(p1)
            view_map(p2)
            
            if has_player_lost(p2)== "Player_has_won" :
                game_over_splash()
                print_player_won1()
                play = False
                break
                    
            anti_cheating()
            print("player 2")
            view_my_map(p2)
            view_map(p1)
            print(guess_coord('Shoot at',p1))
            view_my_map(p2)
            view_map(p1)
            
            if has_player_lost(p1)== "Player_has_won":
                game_over_splash()
                print_player_won2()
                play = False
                break
        break
    
def speed():
    while True:
        input("press enter to start game")
        p1,p2=make_maps(10)
        view_map(p1)
        p1inventory,p2inventory=player_inventory(1,2,1,1)
        place_ship('Place', p1inventory, p1)
        anti_cheating()
        place_ship('Place', p2inventory, p2)
        play = True
        while play == True:
            anti_cheating()
            for x in range(5):
                print("Player 1")
                view_my_map(p1)
                view_map(p2)
                print(guess_coord('Shoot at',p2))
                if has_player_lost(p2)== "Player_has_won" :
                    game_over_splash()
                    print_player_won1()
                    play = False  
                    return None
            anti_cheating()
            for y in range(5):
                print("Player 2")
                view_my_map(p2)
                view_map(p1)
                print(guess_coord('Shoot at',p1))
                if has_player_lost(p1)== "Player_has_won":
                    game_over_splash()
                    print_player_won2()
                    play = False
                    return None
        break

def next_frame():
    for x in range(70):
        print()

def menu(title, prompt, options):
    print(title)
    print()
    for key, value in options.items():
        print(f'{key}) {value}')
    print()
    while True:
        inp=input(prompt)
        if inp in options:
            print()
            print(f'You selected option {inp}) {options[inp]}')
            break
    print()
    return inp

playagain={'y':'Yes','n':'No'}
gamemodes={'n':'Normal','s':'Speed','c':'Custom'}

def main():
    splash()
    while True:
        mode = menu('Choose game mode','Game mode: ',gamemodes)
        if mode == "n":
            normal()
        elif mode == "s":
            speed()
        elif mode == "c":
            custom()

        reboot=menu('Do you want to play again?','',playagain)
        if reboot == "n":
            break
    print("Thank you for playing Hide and sink")
    print("See you later")

main()