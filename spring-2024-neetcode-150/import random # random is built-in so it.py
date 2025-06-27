import random

def distribute_cards(num_cards, num_players):
    # Base case: check if there is atleast one player
    if num_players <= 0:
        raise ValueError("There must be at least one player.")

    # Base case: only carry on if there are cards
    if num_cards < 0:
        raise ValueError("The number of cards cannot be negative.")
    
    # Create a deck of cards represented as numbers from 1 to num_cards
    deck = list(range(1, num_cards + 1))
    
    # Shuffle the deck
    random.shuffle(deck)
    
    # Create a dictionary to store each player's cards
    # This will be of format {1: [cards], 2:[cards], etc...}
    players = {i: [] for i in range(1, num_players + 1)}
    
    # Deal cards and store in the dict we made earlier, modulo is easy to use here
    for i, card in enumerate(deck):
        # (i % num_players) cycles through 0 to (num_players-1), then add 1 to shift the range to 1 ... num_players.
        player_id = (i % num_players) + 1
        # Add the current card to the current players list of cards
        players[player_id].append(card)
    
    return players

# Example: 5 and Number of players: 3.
# Here, two players should get 2 cards and one player should get 1 card.
players_cards = distribute_cards(5, 3)

for player, cards in players_cards.items():
    print(f"Player {player}: {len(cards)} card(s) -> {cards}")
