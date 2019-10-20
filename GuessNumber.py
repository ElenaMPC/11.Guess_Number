import random
import json
import datetime
from operator import itemgetter


secret = random.randint(1, 5)
attempts = 0


with open("score_list.txt","r") as score_file:
    score_list = json.loads(score_file.read())
    newlist = sorted(score_list, key=itemgetter("attempts"))[:3]

    for x in newlist:
        print(str(x["attempts"]) + " attempts, date: " + x.get("date") + " " + x["nombre"])

        # print(score_list[:3])
        # esto imprime sólo los 3 primeros elementos de la lista

wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 5): "))
    attempts += 1      # A lo que tuvieras ya, súmale 1 attemps = attemps + 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        current_time = str(datetime.datetime.now())
        user = input("¿Usuario?")
        score_data = {"attempts": attempts, "date": current_time, "nombre": user, "Wrong_guesses": wrong_guesses}
        print(current_time, "Muy bien", user, "!")


        score_list.append(score_data)
        # Esto añade datos a la lista.

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")

    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)