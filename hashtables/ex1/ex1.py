#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i, w in enumerate(weights):
        if hash_table_retrieve(ht, w) is not None:
            existing = hash_table_retrieve(ht, w)
            existing.append(i)
            hash_table_insert(ht, w, existing)
        else:
            hash_table_insert(ht, w, [i])

    for i, w in enumerate(weights):
        pair_indices = hash_table_retrieve(ht, limit - w)
        pair_index = pair_indices[0] if pair_indices is not None else None

        if pair_index == i and len(pair_indices) > 1:
            pair_index = pair_indices[1]

        if pair_index is not None:
            w_index = hash_table_retrieve(ht, w)[0]
            return (w_index, pair_index) if w_index >= pair_index else (pair_index, w_index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
