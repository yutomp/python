import random

class Card:
    cardNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardKinds = ["スペード", "クラブ", "ダイヤ", "ハート"]
    
    def getNumber(self, num):
        return self.cardNumbers[num]

    def getCards(self, num):
        return self.cards[num]

    def getCardKinds(self, num):
        return self.cardKinds[num]

class Player:
    drawedCards = [[False] * 13 for i in range(4)]
    def __init__(self):
        self.hands = []
        for i in range(2):
          self.draw()
    
    def draw(self):
        card = Card()
        #重複時のやり直し
        while True:
            self.randomCardNumber = random.randrange(13)
            self.randomCard = self.randomCardNumber
            self.randomCardKinds = random.randrange(4)
            if self.drawedCards[self.randomCardKinds][self.randomCard] == False:
                self.drawedCards[self.randomCardKinds][self.randomCard] = True
                self.hands.append(card.getNumber(self.randomCardNumber))
                print(card.getCardKinds(self.randomCardKinds) + card.getCards(self.randomCard) + "をドローしました。")
                break

    def getSum(self):
        self.sum = 0
        for i in self.hands:
            self.sum += i
        return self.sum


print("-----Game Start-----")

#プレイヤー
player = Player()
while True:
    print("カードをドローしますか？（はい:y、　いいえ：それ以外）")
    if input() == "y":
        player.draw()
    else:
        break
print("あなたの合計は" + str(player.getSum()) + "です。")

#ディーラー
dealer = Player()
while True:
    if dealer.getSum() >= 17:
        break
    dealer.draw()
print("ディーラーの合計は" + str(dealer.getSum()) + "です。")

#判定
if (player.getSum() > 21 and dealer.getSum() > 21) or player.getSum() == dealer.getSum():
    print("引き分けです。")   
elif player.getSum() <= 21 and (dealer.getSum() > 21 or player.getSum() > dealer.getSum()):
    print("あなたの勝ちです！！")
elif (player.getSum() > 21 or player.getSum() < dealer.getSum()) and dealer.getSum() <= 21:
    print("あなたの負けです・・・")

     