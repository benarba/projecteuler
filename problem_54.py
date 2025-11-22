m = {}
for i in range(2, 10):
    m[str(i)] = i
m["T"] = 10
m["J"] = 11
m["Q"] = 12
m["K"] = 13
m["A"] = 14


def eval_hand(cards):

    n_dict = {}
    for card in cards:
        n = m[card[0]]
        if n in n_dict:
            n_dict[n] += 1
        else:
            n_dict[n] = 1

    rev_n_dict = {}
    for k, v in n_dict.items():
        if v in rev_n_dict:
            rev_n_dict[v].append(k)
        else:
            rev_n_dict[v] = [k]

    s_dict = {}
    for card in cards:
        s = card[1]
        if s in s_dict:
            s_dict[s] += 1
        else:
            s_dict[s] = 1

    # NOTE: straight check
    straight = len(n_dict) == 5 and max(n_dict) - min(n_dict) == 4

    # NOTE: flush check
    flush = len(s_dict) == 1

    # NOTE: straight flush
    straight_flush = straight and flush

    # NOTE: royal flush
    royal_flush = straight and flush and 14 in n_dict

    # NOTE: 4 of a kind
    kind4 = 4 in rev_n_dict

    # NOTE: full house
    full_house = 3 in rev_n_dict and 2 in rev_n_dict

    # NOTE: 3 of a kind
    kind3 = 3 in rev_n_dict

    # NOTE: a pair
    pair = 2 in rev_n_dict

    # NOTE: 2 pairs
    pairs2 = False
    if 2 in rev_n_dict:
        if len(rev_n_dict[2]) == 2:
            pairs2 = True

    order = ""
    for key in sorted(rev_n_dict, reverse=True):
        for n in sorted(rev_n_dict[key], reverse=True):
            order += format(n, "02d") * key

    eval_str = (
        str(int(royal_flush))
        + str(int(straight_flush))
        + str(int(kind4))
        + str(int(full_house))
        + str(int(flush))
        + str(int(straight))
        + str(int(kind3))
        + str(int(pairs2))
        + str(int(pair))
        + order
    )

    return eval_str


with open("0054_poker.txt", "r") as f:
    text = f.read()

lines = text.split("\n")
player_1 = []
player_2 = []

for line in lines:
    moves = line.split()
    if len(moves) < 10:
        continue
    player_1.append(moves[:5])
    player_2.append(moves[5:])


counter = 0
for i in range(len(player_1)):
    if eval_hand(player_1[i]) > eval_hand(player_2[i]):
        counter += 1
print(counter)
