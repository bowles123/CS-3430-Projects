#Brian Bowles Assignment 4, February 2, 2015.

# Makes leaf of huffman tree.
def make_leaf(symbol, weight):
    return (symbol, weight)

# Returns true if it is a leaf.
def is_leaf(x):
    return isinstance(x, tuple) and len(x) == 2 and \
            isinstance(x[0], str) and isinstance(x[1], int)

# Get the symbol of a given leaf.
def get_leaf_symbol(leaf):
    return leaf[0]

# Get the frequency of a given leaf.
def get_leaf_freq(leaf):
    return leaf[1]

# Get left branch of a given huff tree.
def get_left_branch(huff_tree):
    return huff_tree[0]

# Get right branch of a given huff tree.
def get_right_branch(huff_tree):
    return huff_tree[1]

# Get symbols of a given huff tree.
def get_symbols(huff_tree):
    if is_leaf(huff_tree):
        return [get_leaf_symbol(huff_tree)]
    else:
        return huff_tree[2]

# Get frequency of a given huff tree.
def get_freq(huff_tree):
    if is_leaf(huff_tree):
        return get_leaf_freq(huff_tree)
    else:
        return huff_tree[3]
# Make a huffman tree.
def make_huffman_tree(left_branch, right_branch):
    return [left_branch,
            right_branch,
            get_symbols(left_branch) + get_symbols(right_branch),
            get_freq(left_branch) + get_freq(right_branch)]

# Make leaves.
E_1 = make_leaf('E', 1)
F_1 = make_leaf('F', 1)

G_1 = make_leaf('G', 1)
H_1 = make_leaf('H', 1)

C_1 = make_leaf('C', 1)
D_1 = make_leaf('D', 1)

B_3 = make_leaf('B', 3)
A_8 = make_leaf('A', 8)

# Make subtrees.
EF_2 = make_huffman_tree(E_1, F_1)
GH_2 = make_huffman_tree(G_1, make_leaf('H', 1))
EFGH_4 = make_huffman_tree(EF_2, GH_2)

CD_2 = make_huffman_tree(C_1, D_1)
BCD_5 = make_huffman_tree(B_3, CD_2)

BCDEFGH_9 = make_huffman_tree(BCD_5, EFGH_4)

#Make final huffman tree.
ABCDEFGH_17 = make_huffman_tree(A_8, BCDEFGH_9)

# Encode symbol given a huffman tree
def huffman_encode_symbol(symbol, huff_tree):
    # Variables.
    current_node = huff_tree
    encoding = []

    # While current node isn't the leaf loop.
    while is_leaf(current_node) == False:
        left_symbols = get_symbols(get_left_branch(huff_tree))
        right_symbols = get_symbols(get_right_branch(huff_tree))

        # If symbol is in left branch traverse that branch.
        if symbol in left_symbols:
            encoding.append(0)
            huff_tree = get_left_branch(huff_tree)

        # If symbol is in the right branch traverse that branch.
        if symbol in right_symbols:
            encoding.append(1)
            huff_tree = get_right_branch(huff_tree)

        current_node = huff_tree

    return encoding

# Encode a given message using the huffman tree.
def huffman_encode(message, huff_tree):
    encoding = []

    # While message still has bits encode symbol.
    for i in range(len(message)):
        encoding.extend(huffman_encode_symbol(message[i], huff_tree))

    return encoding

# Decode given a list of bits and a huffman tree.                             
def huffman_decode (bits, huff_tree):
    # Variables.
    current_node = huff_tree
    decoding = []
    new_bits = list(bits)

    # While it doesn't return loop.
    while True:
        # If the current node is a leaf add it to decoding.
        if is_leaf(current_node):
            decoding.append(get_leaf_symbol(current_node))
            current_node = huff_tree

        if current_node == huff_tree and new_bits == []:
            return decoding

        # If you're not done decoding, but huff tree doesn't equal root throw error.
        if new_bits == [] and current_node != huff_tree:
            print "Error"
            return decoding

        # If in left branch traverse that branch and read bits.
        if new_bits[0] == 0:
            current_node = get_left_branch(current_node)
            new_bits.pop(0)

        # Otherwise should be in right branch, read bits.
        elif new_bits[0] == 1:
            current_node = get_right_branch(current_node)
            new_bits.pop(0)
        else:
            return decoding
        
# Examples of functions.
message = ['B', 'A', 'C']
code = [1,0,0,0,1,0,1,0]

print huffman_decode([0,1,0,0,1,0,0,0], ABCDEFGH_17)
print huffman_decode(code, ABCDEFGH_17)
print huffman_encode(message, ABCDEFGH_17)
print huffman_encode(['A', 'B', 'B', 'A'], ABCDEFGH_17)

print huffman_decode(huffman_encode(message, ABCDEFGH_17), ABCDEFGH_17)
print huffman_encode(huffman_decode(code, ABCDEFGH_17), ABCDEFGH_17) == code
