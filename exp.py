# Whoever takes the last stone loses

def main():
    stones = 20
    print("There are 20 stones left.")
    player_one = int(input("Player 1 would you like to remove 1 or 2 stones? "))
    print()
    while player_one != 1 and player_one != 2:
        player_one = int(input("Please enter 1 or 2: "))
    player_one = int(player_one)
    stones = stones - player_one
    print(f"There are {stones} stones left.")
    player_two = int(input("Player 2 would you like to remove 1 or 2 stones? "))
    while player_two != 1  and player_two != 2:
        player_two = int(input("Please enter 1 or 2: "))
    print()
    player_two = int(player_two)
    stones = stones - player_two
    print(f"There are {stones} stones left.")
    while stones > 0:
        player_one = int(input("Player 1 would you like to remove 1 or 2 stones? "))
        while player_one != 1 and player_one != 2:
            player_one = int(input("Please enter 1 or 2: "))
        player_one = int(player_one)
        stones = stones - player_one
        print()
        if stones <= 0:
            print("Player 2 wins!")
        else:
            print(f"There are {stones} stones left.")
            player_two = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while player_two != 1  and player_two != 2:
                player_two = int(input("Please enter 1 or 2: "))
            player_two = int(player_two)
            stones = stones - player_two
            print()
            if stones <= 0:
                print()
                print("Player 1 wins!")
            else:
                print(f"There are {stones} stones left.")

if __name__ == '__main__':
    main()
