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
    def __init__(self):
        self.hands = []
        for i in range(2):
          self.draw()

    def draw(self):
        card = Card()
        randomNumber = random.randrange(13)
        self.hands.append(card.getNumber(randomNumber))
        print(card.getCardKinds(random.randrange(4)) + card.getCards(randomNumber) + "をドローしました。")

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
        print("カードをドローします。")
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
if player.getSum() > dealer.getSum() and (player.getSum() <= 21 and dealer.getSum() > 21):
    print("あなたの勝ちです！！")
elif player.getSum() < dealer.getSum() and (player.getSum() > 21 and dealer.getSum() <= 21):
    print("ディーラーの勝ちです・・・")
else:
    print("引き分けです。")    