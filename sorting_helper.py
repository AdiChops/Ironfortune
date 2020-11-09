# if the list needs to be sorted by default, which is coins, otherwise its sorted by DamagePoints
def merge_sort_moves(moves, default=True):
    if len(moves) <= 1:
        return moves
    else:
        left = merge_sort_moves(moves[0:len(moves) // 2])
        right = merge_sort_moves(moves[len(moves) // 2:len(moves)])
        return merge(left, right, default)


def merge(l, r, default=True):
    return_list = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if default:
            condition = l[i] < r[j]
        else:
            condition = l[i].DamagePoints < r[j].DamagePoints
        if condition:
            return_list.append(l[i])
            i += 1
        else:
            return_list.append(r[j])
            j += 1
    while i < len(l):
        return_list.append(l[i])
        i += 1
    while j < len(r):
        return_list.append(r[j])
        j += 1
    return return_list
