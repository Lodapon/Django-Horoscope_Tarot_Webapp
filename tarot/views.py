from django.shortcuts import render
import random
from .card_data import tarot_cards


# Create your views here.


# def generate_horoscope(request):
#     # Randomly select 3 Tarot cards
#     selected_cards = random.sample(tarot_cards, 3)

#     cards_with_meanings = []

#     for card in selected_cards:
#         # Randomly select whether the card is upright or reversed
#         is_upright = random.choice([True, False])

#         # Get the appropriate meaning based on the card's orientation
#         if is_upright:
#             meaning = card["upright_meaning"]
#         else:
#             meaning = card["reversed_meaning"]

#         # Add the card, its meaning, and orientation to the list
#         cards_with_meanings.append({
#             "card": card,
#             "meaning": meaning,
#             "is_upright": is_upright
#         })

#     # Pass the list of cards and their meanings to the template
#     return render(request, 'tarot/horoscope.html', {'cards': cards_with_meanings})


def generate_horoscope(request):
    # Randomly select 3 Tarot cards
    selected_cards = random.sample(tarot_cards, 3)

    cards_with_meanings = []
    combined_meaning = ""  # To hold the combined interpretation

    for card in selected_cards:
        # Randomly select whether the card is upright or reversed
        is_upright = random.choice([True, False])

        # Get the appropriate meaning based on the card's orientation
        if is_upright:
            meaning = card["upright_meaning"]
        else:
            meaning = card["reversed_meaning"]

        # Add the card, its meaning, and orientation to the list
        cards_with_meanings.append({
            "card": card,
            "meaning": meaning,
            "is_upright": is_upright
        })

        # Combine the meanings of all 3 cards
        combined_meaning += f"{card['name']} ({'Upright' if is_upright else 'Reversed'}): {meaning}<br>"

    # Pass the list of cards, their meanings, and combined interpretation to the template
    return render(request, 'tarot/horoscope.html', {
        'cards': cards_with_meanings,
        'combined_meaning': combined_meaning
    })
