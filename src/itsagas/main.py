import random
import time

gases = ['air', 'nitrogen', 'oxygen', 'hydrogen', 'neon',
         'carbondioxide', 'carbonmonoxide', 'krypton', 'xenon', 'radon']

guesses = set([])

while True:
    gas = random.choice(gases)

    print("""
I'm thinking of a gas
          """)
    time.sleep(1)

    print("Guess which one?")

    while True:
        guess = input(": ").lower()
        print()

        match guess:
            case "help":
                print(f"""
Whaddya know, it just so happens that we have a list:
{", ".join(gases)}
                      """)
                continue

            case "exit" | "stop" | "quit" | "q" | "":
                print("Fine. What do you think this is? A game? Out of my face!")
                exit()

            case g if g == gas:
                print("You gassed it!")
                exit()

            case g if g in guesses:
                print("No pressure.")

            case _:
                guesses.add(guess.lower())
                if guess in gases:
                    print("It's a gas.")
                else:
                    print("Gas again!")

        print()


if __name__ == "__main__":
    main()
