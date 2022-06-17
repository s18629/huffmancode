import string
codee = ''
fullCode = ''
save = open('codedmessage.txt', 'a')


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''


def printNodes(node, val=''):
    newVal = val + str(node.huff)

    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

    if not node.left and not node.right:
        toPrint = f"{node.symbol} -> {newVal}\n"
        print(f"{node.symbol} -> {newVal}")
        save.write(toPrint)
        global fullCode
        if (fullCode == ''):
            fullCode = {node.symbol: newVal}
        else:
            fullCode[node.symbol] = [newVal]


text = open('toencode.txt').read()
letters = string.ascii_lowercase + ' '

freq = []
chars = ""

for a in letters:
    if a in text:
        freq.append(text.count(a))
        chars += a

nodes = []

for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.freq)

    left = nodes[0]
    right = nodes[1]

    left.huff = 0
    right.huff = 1

    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)


def printCode():
    code = ''
    for q in text:
        if q in fullCode.keys():
            code += str(fullCode[q])
    print(("%s" % code).replace("'", "").replace("[", "").replace("]", ""))
    save.write((("%s" % code).replace("'", "").replace("[", "").replace("]", "")))


printNodes(nodes[0])
printCode()
save.close()
