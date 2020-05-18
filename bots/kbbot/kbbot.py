#!/usr/bin/env python
"""
This is a bot that applies propositional logic reasoning to determine its strategy.
The strategy it uses is determined by what is defined in load.py. Here it is to always
pick a Jack to play whenever this is a legal move.

It loads general information about the game, as well as the definition of a strategy,
from load.py.
"""

from api import State, util
import random
# from . import load
# from .kb import KB, Boolean, Integer

class Bot:

    def __init__(self):
        pass

    def get_move(self, state):

        moves = state.moves()

        random.shuffle(moves)

        # num_moves = len(moves)
        # count = 0
        # print("Trump Suit: " + state.get_trump_suit())

        if(state.get_phase() == 1):
            # print("count is: " + str(count))
            for move in moves:
                if move[0] == None:
                    return move
                elif int(move[0] / 5) == 3 and state.get_trump_suit() != "S":
                    if move[0] == 19 or move[0] == 18 or move[0] == 17:
                        return move
                elif int(move[0] / 5) == 2 and state.get_trump_suit() != "H":
                    if move[0] == 14 or move[0] == 13 or move[0] == 12:
                        return move
                elif int(move[0] / 5) == 1 and state.get_trump_suit() != "D":
                    if move[0] == 9 or move[0] == 8 or move[0] == 7:
                        return move
                elif int(move[0] / 5) == 0 and state.get_trump_suit() != "C":
                    if move[0] == 4 or move[0] == 3 or move[0] == 2:
                        return move
            # return random.choice(moves)
        else:
            for move in moves:
                # count += 1
                if int(move[0] / 5) == 3 and state.get_trump_suit() == "S" or int(move[0] / 5) == 2 and state.get_trump_suit() == "H" or int(move[0] / 5) == 1 and state.get_trump_suit() == "D" or int(move[0] / 5) == 0 and state.get_trump_suit() == "C":
                    return move
                # elif count == num_moves:

                # print("count: " + str(count))
        return random.choice(moves)

    #         if not self.kb_consistent(state, move):
    #             # Plays the first move that makes the kb inconsistent. We do not take
    #             # into account that there might be other valid moves according to the strategy.
    #             # Uncomment the next line if you want to see that something happens.
    #             print("Strategy Applied")
    #             return move
    #
    #     # If no move that is entailed by the kb is found, play random move
    #     return random.choice(moves)
    #
    # # Note: In this example, the state object is not used,
    # # but you might want to do it for your own strategy.
    # def kb_consistent(self, state, move):
    # # type: (State, move) -> bool
    #
    #     # each time we check for consistency we initialise a new knowledge-base
    #     kb = KB()
    #
    #     # Add general information about the game
    #     load.general_information(kb)
    #
    #     # Add the necessary knowledge about the strategy
    #     load.strategy_knowledge(kb)
    #
    #     # This line stores the index of the card in the deck.
    #     # If this doesn't make sense, refer to _deck.py for the card index mapping
    #     index = move[0]
    #
    #     # This creates the string which is used to make the strategy_variable.
    #     # Note that as far as kb.py is concerned, two objects created with the same
    #     # string in the constructor are equivalent, and are seen as the same symbol.
    #     # Here we use "pj" to indicate that the card with index "index" should be played with the
    #     # PlayJack heuristics that was defined in class. Initialise a different variable if
    #     # you want to apply a different strategy (that you will have to define in load.py)
    #     # variable_string = "pc" + str(index)
    #     # strategy_variable = Boolean(variable_string)
    #     strategy_variable = state.get_phase()
    #     if(move[0] / 5 == 3):
    #         card_suit = Boolean('C')
    #     elif(move[0] / 5 == 2):
    #         card_suit = Boolean('D')
    #     elif(move[0] / 5 == 1):
    #         card_suit = Boolean('H')
    #     else:
    #         card_suit = Boolean('S')
    #
    #
    #     # Add the relevant clause to the loaded knowledge base
    #     kb.add_clause(~strategy_variable)
    #
    #     t_suit = str(state.get_trump_suit())
    #     # print(str(t_suit))
    #
    #     strategy_variable = Boolean(t_suit)
    #     kb.add_clause(~strategy_variable)
    #     # If the knowledge base is not satisfiable, the strategy variable is
    #     # entailed (proof by refutation)
    #     return kb.satisfiable()
