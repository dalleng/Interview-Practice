from collections import deque


def predictPartyVictory(senate: str) -> str:
    vote_r = 0
    vote_d = 0
    current_queue = deque(senate)
    next_round = deque()

    while current_queue:
        current = current_queue.popleft()
        if current == 'R':
            if vote_d == 0:
                next_round.append(current)
                vote_r += 1
            elif vote_d > 0:
                vote_d -= 1
        elif current == 'D':
            if vote_r == 0:
                next_round.append(current)
                vote_d += 1
            elif vote_r > 0:
                vote_r -= 1
        
        if not current_queue:
            if len(set(next_round)) == 1:
                break
            else:
                current_queue = next_round
                next_round = deque()

    winner = next_round[0]
    return 'Radiant' if winner == 'R' else 'Dire'

if __name__ == "__main__":
    assert predictPartyVictory('RD') == 'Radiant'
    assert predictPartyVictory('RDD') == 'Dire'

