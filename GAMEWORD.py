import random

def choisir_mot():
    mots = ["python", "programmation", "ordinateur", "intelligence", "algorithmique", "informatique"]
    return random.choice(mots)

def melanger_mot(mot):
    lettres = list(mot)
    random.shuffle(lettres)
    return ''.join(lettres)

def main():
    mot_secret = choisir_mot()
    mot_melange = melanger_mot(mot_secret)
    print("***************************************************************Weeeeeeelcomeeee to the gaaaaame*****************************************************************************************************")
    print("Guess the word: ", mot_melange )
    print("tap help to see two first letters ")


    tentative = 0
    help = False

    while True:
        proposition = input("Proposition : ").lower()

        if proposition == "help" and not help:
            help = True
            print("First Two letters :", mot_secret[:2])
            continue

        if proposition == mot_secret:
            print("Congratulationsss")
            break
        else:
            print("Not correct ")
        
        tentative += 1
        print("you still have ", 5-tentative)
        if tentative >= 5:
            print("Max guesses the word is  {}.".format(mot_secret))
            break

if __name__ == "__main__":
    main()

