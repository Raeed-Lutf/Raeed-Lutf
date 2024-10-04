import random

# كلاس يمثل الكروت
class Card:
    def init(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def repr(self):
        return f'{self.rank}{self.suit}'

# كلاس يمثل اللاعب
class Player:
    def init(self, name):
        self.name = name
        self.hand = []
        self.collected_cards = []

    def draw_card(self, card):
        self.hand.append(card)

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return card
        return None

    def collect_cards(self, cards):
        self.collected_cards.extend(cards)

# كلاس يمثل اللعبة
class BasraGame:
    def init(self):
        self.deck = [Card(str(num), suit) for num in list(range(1, 11)) + ['جاك', 'ملكة', 'ملك'] for suit in ['♠', '♥', '♦', '♣']]
        self.player = Player("اللاعب")
        self.opponent = Player("الخصم")
        self.table_cards = []
        self.remaining_deck = []

    def shuffle_and_deal(self):
        random.shuffle(self.deck)
        self.player.hand = self.deck[:4]
        self.opponent.hand = self.deck[4:8]
        self.table_cards = self.deck[8:12]
        self.remaining_deck = self.deck[12:]

    def show_cards(self, cards):
        return ' '.join([str(card) for card in cards])

    def player_turn(self):
        print(f"\nأوراقك: {self.show_cards(self.player.hand)}")
        print(f"أوراق على الطاولة: {self.show_cards(self.table_cards)}")
        chosen_card = self.player.hand[0]  # بشكل بسيط، اللاعب يلعب الورقة الأولى (يمكن تحسينه لاحقاً)
        print(f"لقد لعبت: {chosen_card}")
        self.player.play_card(chosen_card)

        collected_cards = self.collect_from_table(chosen_card)
        if collected_cards:
            print(f"جمعت الأوراق: {self.show_cards(collected_cards)}")
            self.player.collect_cards(collected_cards)
        else:
            print("لم تجمع أي أوراق.")
        self.table_cards.append(chosen_card)

    def collect_from_table(self, card):
        collected_cards = []
        for table_card in self.table_cards:
            if card.rank == table_card.rank:
                collected_cards.append(table_card)
        for collected in collected_cards:
            self.table_cards.remove(collected)
        return collected_cards

    def play_game(self):
        self.shuffle_and_deal()
        print("=== بدء اللعبة ===")
        print(f"أوراق على الطاولة: {self.show_cards(self.table_cards)}")
        self.player_turn()
        # يمكن تطوير اللعبة لإضافة دور الخصم وتوزيع الأوراق المتبقية

# بدء اللعبة
game = BasraGame()
game.play_game()