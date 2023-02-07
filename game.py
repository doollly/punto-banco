import random

class PuntoBanco:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(self.deck)
        self.punto = []
        self.banco = []

    def deal(self):
        self.punto.append(self.deck.pop())
        self.banco.append(self.deck.pop())
        self.punto.append(self.deck.pop())
        self.banco.append(self.deck.pop())

    def total(self, hand):
        t = sum(hand)
        for i in hand:
            if i == 11 and t > 21:
                t -= 10
        return t

    def play(self):
        self.deal()
        print(f"Punto hand: {self.punto} ({self.total(self.punto)})")
        print(f"Banco hand: [{self.banco[0]}, X]")

        while self.total(self.punto) < 21:
            action = input("Do you want to hit or stand? ")
            if action == "hit":
                self.punto.append(self.deck.pop())
                print(f"Punto hand: {self.punto} ({self.total(self.punto)})")
            elif action == "stand":
                break

        while self.total(self.banco) < 17:
            self.banco.append(self.deck.pop())

        print(f"Banco hand: {self.banco} ({self.total(self.banco)})")

        if self.total(self.punto) > 21:
            print("Punto busts, Banco wins!")
        elif self.total(self.banco) > 21:
            print("Banco busts, Punto wins!")
        elif self.total(self.punto) > self.total(self.banco):
            print("Punto wins!")
        elif self.total(self.punto) < self.total(self.banco):
            print("Banco wins!")
        else:
            print("Tie!")

game = PuntoBanco()
game.play()
