import time
import random
# the player and weapons section
WEAPONS = {'knife': (3, 10), 'none': (1, 5), 'stick' : (0, 1)}
player = {'weapon': None, 'health': None}
player['weapon'] = WEAPONS['knife']

#the functions
def ask(question):
 answer = raw_input(question + " [y/n]")
 return answer in ['y', 'Y', 'Yes', 'yes', 'YES']

def ask_leftright(question):
    answer = raw_input(question + " [L/R]")
    return answer in ['L', 'l', 'Left', 'left', 'LEFT'] #if = left. else = right

def combat(player, enemy):
    global player_damage
    global enemy_damage
    global player_win
    global enemy_win
    player_damage = random.randrange(*player['weapon'])
    enemy_damage = random.randrange(*enemy['attack'])

    player_win = player_damage > enemy['health']
    enemy_win = enemy_damage > player['health']

    return player_damage, player_win, enemy_damage, enemy_win


def combat_describe(player, enemy, fightdescription):
    player_damage, player_win, enemy_damage, enemy_win = combat(player, enemy)

    print fightdescription ['player_damage'] % (enemy['name'], player_damage)
    print fightdescription ['enemy_damage'] % (enemy['name'], enemy_damage)

    if player_win:
        print fightdescription['player_win'] % (enemy['name'])
        return True
    if enemy_win:
        print fightdescription['enemy_win'] % (enemy['name'])
        return False

    return False


#the enemy's and the enemy fight description
GUARD_FIGHT = {'player_damage' : "You hit the %s for %i damage",
              'enemy_damage' : "The %s hits you for %i damage",
              'player_win' : "The %s is killed ",
              'enemy_win' : "The %s killed you"}

firstguard = {'name': 'Prison guard', 'health': 5, 'attack': (1, 5)}

#some booleans for checkpoint choices
skeletonkey_taken = None
door_opened = None
letter_read = None
stealth_mode = None

#the main game
def game():
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Welcome to the broken prison!")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(2)
    if ask("You wake up looking down and you see an object lying in front of you, do you take the object?"):
        print "You took the object."
        skeletonkey_taken = True
        player['health'] = 10

    else:
       # print "You did not take the object"
        skeletonkey_taken = False

    time.sleep(2)

    if skeletonkey_taken == True:

        if ask("Do you want to inspect the object?"):
            print "It seems to be some kind of key,made from a skeleton bone."
            time.sleep(2)
            print "You put the object away and decide to look around."
            time.sleep(2)

        else:
            print "You put the object away and decide to look around."
            time.sleep(2)
    else:
        print "You leave the object there and decide to look around."
        time.sleep(2)

    print "You seem to be in some kind of holding cell."
    time.sleep(2)

    if ask("You hear some noise at the door, are you going to check it out?"):
        print "You walk towards the door and hear some people in the distance, they do not sound like they're close."
        time.sleep(2)

        if skeletonkey_taken == True:
            if ask("There is some kind of keyhole in the door, will you try the object from before?"):
                time.sleep(2)
                print "Click...... the door opens."
                time.sleep(2)
                door_opened = True
            else:
                print "You do not use the key."
                time.sleep(2)
                door_opened = False
        else:
            print "You realise you can't do anything and you decide to go back to the center of the cell."
            time.sleep(2)
            door_opened = False
    else:
        print "You stay in place."
        time.sleep(2)
        door_opened = Falsey


    if door_opened == False and skeletonkey_taken == True:
        print "You start  thinking that maybe you should use the object on the door."
        time.sleep(2)
        print "You walk towards the door and use the object."
        time.sleep(2)
        print "Click..... The door opens..."
        time.sleep(2)
        door_opened = True
    elif door_opened == False and skeletonkey_taken == False:
        print "You start to think that maybe you could use the object for something"
        time.sleep(2)
        print "You walk towards the door and use the object."
        time.sleep(2)
        print "Click..... The door opens..."
        time.sleep(2)
        door_opened = True
    if door_opened == True and skeletonkey_taken ==True:
        if ask("The light hurts your eyes. You could walk outside the door. Do you want to?"):
            time.sleep(2)
            print "As you step outside your cell you see that you are in a prison, yet there are no guards around."
            time.sleep(2)
            print "Right before your doorstep there is a small letter, almost invisible."
            time.sleep(2)
            if ask("you want to read it?"):
                time.sleep(2)
                print """Dear Frank, though you do not know who I am, I am a friend.
                         There is a bag in the corner of this hallway which contains
                         a weapon and more instructions. Please do as they say and
                         escape this madness. I will be waiting outside,

                         A friend."""
            else:
                print "You dont read it. "
                time.sleep(2)
        else:
            print "You stay inside but after a while your curiosity gets the upper side of you and you do walk outside."
            time.sleep(2)
            print "As you step outside your cell you see that you are in a prison, yet there are no guards around."
            time.sleep(2)
            print "Right before your doorstep there is a small letter, almost invisible."
            time.sleep(2)
            if ask("you want to read it?"):
                time.sleep(2)
                print """           \t\t Dear Frank,\n

                                     though you do not know who I am, I am a friend.
                                     There is a bag in the corner of this hallway which contains
                                     a weapon and more instructions. Please do as they say and
                                     escape this madness. I will be waiting outside,

                                     A friend."""
                time.sleep(2)
                letter_read = True
            else:
                print "You dont read it. "
                time.sleep(2)
                letter_read = False
    if ask_leftright("On the leftside there is a dead end, on the right side there is a hallway turn. Which way do you want to go?"):
        time.sleep(2)
        print "You can check the left corner and the right one."
        if ask_leftright("Which corner do you want to check?"):
            time.sleep(2)
            print "There seems to be nothing here."
            time.sleep(1)
            print "You now check the right corner..."
            time.sleep(3)
            print "You've found the bag. There is a knife and some instructions."
            time.sleep(2)

        else:
            time.sleep(2)
            print "You've found the bag. There is a knife and some instructions in there."
            time.sleep(2)
    else:
        time.sleep(2)
        print "As you peek around the turn you can see a guard with his back towards you."
        time.sleep(1)
        print "You decide not to go there yet and check the other side."
        time.sleep(2)
        print "You can check the left corner and the right one."
        if ask_leftright("Which corner do you want to check?"):
            time.sleep(2)
            print "There seems to be nothing here."
            time.sleep(1)
            print "You now check the right corner..."
            time.sleep(3)
            print "You've found the bag. There is a knife and some instructions."
            time.sleep(2)

        else:
            time.sleep(2)
            print "You've found the bag. There is a knife and some instructions in there."
            time.sleep(2)

    print "The instructions say:\n" \
          "Find the guard with the green key.\n" \
          "Use that key on the blue door.\n" \
          "Kill if you must, but you don't have to.\n" \
          "There is a peaceful way out.\n" \
          "\n" \
          "Good luck.\n"
    player['weapon'] = WEAPONS['knife']
    time.sleep(2)

    print "You return to the corner and peek again..."
    time.sleep(2)
    print  "You seem to be lucky, the guard is still with his back towards you."
    if ask("Do you want to sneak towards the guard?"):
        print "You sneak towards him..."
        time.sleep(1)
        print "You are now right behind him..."
        time.sleep(1)
        if ask("Do you want to grab and stab him?"):
            time.sleep(1)
            print "You grab the guard from behind and stab him twice in his heart..."
            time.sleep(0.5)
            print "He is dead"
        else:
            #if ask("Do you want to 2")
            print "test"
game()
