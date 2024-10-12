import random
start = input("want to play blackjack game yes or no")
if start == "yes":





    your_cards = []
    computer_card = []

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # random.choice(cards)
    your_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))

    first_card = your_cards

    print(f"your card  = {first_card} -- current score = {sum(first_card)}")

    computer_card.append(random.choice(cards))
    computer_first_card = computer_card
    print(f"computer's first card = {computer_first_card}")


    def step1():
        if sum(your_cards) <= 21 and sum(computer_card) <= 21:
            your_cards.append(random.choice(cards))
            # computer_card.append(random.choice(cards))
            print(f"your card = {your_cards} -- current score = {sum(your_cards)} \ncomputer card = {computer_card} -- current score = {sum(computer_card)}")
            if your_cards[len(your_cards)-1] == 11 and sum(your_cards)>21:
                your_cards.remove(11)
                your_cards.append(1)
            else:
                pass
    
    def step2():
        for i in range(1,len(your_cards)):
            computer_card.append(random.choice(cards))
            print(f"your card = {your_cards} -- current score = {sum(your_cards)} \ncomputer card = {computer_card} -- current score = {sum(computer_card)}")
    
    def step3():
        your_cards.remove(11)
        your_cards.append(1)
        
    final_scoreY = 0
    final_scoreC = 0
    should_continue = True
    while should_continue:
        direction = input("Type 'y' to get another card, type 'n' to pass:")
        if direction == 'y':
            step1()
            final_scoreY = sum(your_cards)
            final_scoreC = sum(computer_card)
            
            if final_scoreY >21  and final_scoreY>final_scoreC:
                should_continue = False
                print(f"you lose")
                
            
            elif final_scoreC >= 21  and final_scoreC>final_scoreY:
                should_continue = False
                print(f"you win ")    
        elif direction == 'n':
            step2()
            final_scoreY = sum(your_cards)
            final_scoreC = sum(computer_card)
            if final_scoreY == final_scoreC:
                print("draw")
            
            else:
                if final_scoreY>21  and final_scoreY<final_scoreC:
                    print("you lose")
                    should_continue = False
                elif final_scoreY == 21:
                    print("you win")
                    should_continue = False
                elif final_scoreC == 21:
                    print("you loss")
                # elif sum(your_cards)<= 21  and final_scoreC<final_scoreY:
                #     print("you win")
                #     should_continue = False
                else:
                    should_continue = False
                    print("you win")
            
        
        
else:
    print("why.....")       
    
    
    
    
    
    
    
    
    
