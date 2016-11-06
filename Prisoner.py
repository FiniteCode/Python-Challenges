import random
from time import sleep
prisonerA = 0
prisonerB = ['stayed silent','confessed']
choice = 0
repeat = "yes"
invalid = "true"
while repeat == "yes":
    print ("=================================================")
    print ("There are 2 prisoners and you are one of them.")
    print ("Do you choose to confess or stay silent?")
    print ("=================================================")
    invalid = "true"
    while invalid == "true":
        prisonerA = input("[confess / stay silent] ")
        print ("=================================================")
        if prisonerA == "confess":
            invalid = "false"
            print ("You had confessed")
        elif prisonerA == "stay silent":
            invalid = "false"
            print ("You had stayed silent")
        else:
            print ("Invalid Option")
    sleep(1)
    choice = (random.choice(prisonerB))
    print ("The other prisoner had "+choice)
    print ("=================================================")
    sleep(1)
    if prisonerA == "confess":
        if choice == 'stayed silent':
            print ("You had confessed and left the prison")
            print ("however the other prisoner is setenced to jail for 20 years")
        if choice == 'confessed':
            print ("You had confessed along with the other prisoner")
            print ("You both are sentenced to prison for only 5 years")
    if prisonerA == "stay silent":
        if choice == 'stayed silent':
            print ("You and the other prisoner stayed silent")
            print ("You both are sentenced for only 1 year before leaving")
        if choice == 'confessed':
            print ("You had stayed silent but the other prisoner had confessed")
            print ("The other prisoner had left however you are sentenced to prison for 20 years")
    print ("=================================================")
    print ("Would you want to repeat simulation?")
    repeat = input("[yes / no] ")
