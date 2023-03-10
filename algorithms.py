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

def BeamSearch(state, depth, maximizingPlayer,width):
    """
    returns maximum of its children values if it is white turn, or minimum if its black, 
    and goes to parameterized depth for calculating values
    """
    if depth == 0 or Game.is_terminal(state):
        return Game.heuristic(state)

    if maximizingPlayer: # aka white 
        maxEval = float('-inf')
        
        candidates = []
        for child in Game.successor(state, 1):
            candidates.append((Game.heuristic(child),child))
      
        candidates.sort(key=lambda tup: tup[0],reverse=True)
        for tu in candidates[:width]:
            child = tu[1]
            eval = BeamSearch(child, depth - 1, False, width)
            
            if eval > maxEval:
                maxEval = eval

        return maxEval

    else: #black 
        minEval = float('inf')
        
        candidates = []
        for child in Game.successor(state, -1):
            candidates.append((Game.heuristic(child),child))
      
        candidates.sort(key=lambda tup: tup[0])
        
        for tu in candidates[:width]:
            child = tu[1]
            eval = BeamSearch(child, depth - 1, True, width)

            if eval < minEval:
                minEval = eval

        return minEval

 
def AlphaBetaPruning(state,maximizingplayer,depth,alpha,beta):
    """
    Minimax Algorithm with alpha beta pruning
    """
    if depth == 0 or Game.is_terminal(state):
        return Game.heuristic(state)

    if maximizingplayer:
        maxEval = float('-inf')

        for child in Game.successor(state, 1):
            eval = AlphaBetaPruning(child, False, depth - 1, alpha, beta)
            #Alpha Beta Pruning
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
            
        return maxEval

    else:
        minEval = float('inf')

        for child in Game.successor(state, -1):
            eval = AlphaBetaPruning(child, True, depth - 1, alpha, beta)
            #Alpha Beta Pruning
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break

        return minEval
