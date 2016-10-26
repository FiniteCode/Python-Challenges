score_player = 0
score_cpu = 0
hand = 0
cpu_hand = 0
from random import randint
while 2 > 0:
    print ("===================================")
    print ("Rock, Paper or Scissors?")
    print ("===================================")
    hand = input("[You] ")
    cpu_hand = randint(1,3)
    if cpu_hand == 1:
        print ("[Cpu] Rock")
        if hand == "Rock":
            print ("--------Draw--------")
        elif hand == "Paper":
            print ("-------You Win-------")
            score_player = score_player+1
        elif hand == "Scissors":
            print ("-------Cpu Win-------")
            score_cpu = score_cpu+1
        else:
            print ("-------Invalid-------")
    elif cpu_hand == 2:
        print ("[Cpu] Paper")
        if hand == "Paper":
            print ("--------Draw--------")
        elif hand == "Scissors":
            print ("-------You Win-------")
            score_player = score_player+1
        elif hand == "Rock":
            print ("-------Cpu Win-------")
            score_cpu = score_cpu+1
        else:
            print ("-------Invalid-------")
    elif cpu_hand == 3:
        print ("[Cpu] Scissors")
        if hand == "Scissors":
            print ("--------Draw--------")
        elif hand == "Rock":
            print ("-------You Win-------")
            score_player = score_player+1
        elif hand == "Paper":
            print ("-------Cpu Win-------")
            score_cpu = score_cpu+1
        else:
            print ("-------Invalid-------")
    print ("Player: "+str(score_player))
    print ("Computer: "+str(score_cpu))
