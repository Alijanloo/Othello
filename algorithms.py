import Game

def minMaxSearch(state, depth, maximizingPlayer):
    """
    returns maximum of its children values if it is white turn, or minimum if its black, 
    and goes to parameterized depth for calculating values
    """
    if depth == 0 or Game.is_terminal(state):
        return Game.heuristic(state)

    if maximizingPlayer:
        maxEval = float('-inf')

        for child in Game.successor(state, 1):
            eval = minMaxSearch(child, depth - 1, False)
            
            if eval > maxEval:
                maxEval = eval

        return maxEval

    else:
        minEval = float('inf')

        for child in Game.successor(state, -1):
            eval = minMaxSearch(child, depth - 1, True)

            if eval < minEval:
                minEval = eval

        return minEval