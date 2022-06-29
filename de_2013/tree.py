class Tree:
    def __init__(root, team, score): 
        root.left = None
        root.right = None
        root.team = team
        root.score = int(score)

def add_node(root, new):
    if root is None:
        root = new
    elif root.team < new.team:
        root.right = add_node(root.right, new)
    elif root.team > new.team:
        root.left = add_node(root.left, new)
    return root

def traversal(root):
    if root is not None:
        traversal(root.left)
        print(root.team, root.score)
        traversal(root.right)

def search(root, team):
    if root is None:
        return None
    elif root.team < team:
        return search(root.right, team)
    elif root.team > team:
        return search(root.left, team)
    else:
        return root

def LeftMost(root):
    while root.left is not None:
        root = root.left
    return root

def delete(root, team_out):
    if root is None:
        return root
    if root.team > team_out:
        root.left = delete(root.left, team_out)
    elif root.team < team_out:
        root.right = delete(root.right, team_out)
    else:
        if root.left is None:
            new = root.right
            root = None
            return new
        elif root.right is None:
            new = root.left
            root = None
            return new

        new = LeftMost(root.right)
        root.team = new.team
        root.score = new.score
        root.right = delete(root.right, new.team)
    return root

def read_file(f):
    root = None

    for x in f:
        x = x.split(" ")
        x[-1] = x[-1].strip()

        team1 = search(root, x[0])
        team2 = search(root, x[1])
        if team1 is None:
            team1 = Tree(x[0], 0)
            root = add_node(root, team1)
        if team2 is None:
            team2 = Tree(x[1], 0)
            root = add_node(root, team2)

        if x[2] < x[3]: team2.score += 3
        elif x[2] > x[3]: team1.score += 3
        else: 
            team1.score += 1
            team2.score += 1

    return root

def output(f, root):
    if root is not None:
        output(f, root.left)
        f.write("%s %d\n" %(root.team, root.score))
        output(f, root.right)

