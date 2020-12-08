import re

def conv_inner(inner):
    bags = []
    for i in inner.split(", "):
        test = re.match(r"(\d+) ([\w ]+) bags?\.?", i)
        if test:
            color = test.group(2)
            count = int(test.group(1))
            bags.append((count, color))

    return bags

def get_parent_and_children(line):
    outer, inner = line.split(" bags contain ")
    return (outer, conv_inner(inner))

def get_parents(color, current_parents, bags):
    for c in bags.get(color, set()):
        current_parents.add(c)
        get_parents(c, current_parents, bags)
    
    return current_parents

def day7_1(): #248
    bags = dict()
    for line in open("day7.txt"):
        parent, children = get_parent_and_children(line.strip())
        for count, child in children:
            cur_parents = bags.get(child, set())
            cur_parents.add(parent)
            bags.update({child: cur_parents})
    
    print(len(get_parents("shiny gold", set(), bags)))


def get_child_count(bag_count, color, bags): 
    children_per_bag = 0
    for count, color in bags.get(color):
        children_per_bag += count + get_child_count(count, color, bags)
    
    return children_per_bag * bag_count

def day7_2(): #57281
    bags = dict(get_parent_and_children(line) for line in open("day7.txt"))
    print(get_child_count(1, "shiny gold", bags))


if __name__ == "__main__":
    day7_1()
    day7_2()