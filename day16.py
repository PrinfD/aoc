import re

def check_rule(rule, value):
    return any(l <= value <= r for l, r in rule)

def matches_any_rule(rules, value):
    return any(check_rule(rule, value) for rule_key, rule in rules.items())


def day16_1():
    result = "".join(open("day16.txt").readlines()).strip() #last linebreak has to be removed 

    rulies = {}
    total_invalid = 0

    for idx, chapter in enumerate(result.split("\n\n")):
        if idx == 0:
            rules = chapter.splitlines()
            for rule in rules:
                field, val = rule.split(": ")
                lv, rv = val.split(" or ")
                llv, rlv = lv.split("-")
                lrv, rrv = rv.split("-")

                rulies[field] = ((int(llv), int(rlv)), (int(lrv), int(rrv)))
        elif idx == 1:
            ticket = chapter.splitlines()[1]
        elif idx == 2:
            tickets = chapter.splitlines()[1:]

            for ticket in tickets:
                vals = [int(val) for val in ticket.split(",")]
                not_valid = [value for value in vals if not matches_any_rule(rulies, value)]
                total_invalid += sum(not_valid)
    
    print(total_invalid)


def remove_singles(possible):
    removed = True

    while removed:
        removed = False
        for p in possible.values():
            if len(p) == 1:
                for op in possible.values():
                    if len(op) != 1:
                        pre_len = len(op)
                        op.difference_update(p)
                        af_len = len(op)
                        if af_len < pre_len:
                            removed = True
                if removed:
                    break

def day16_2():
    result = "".join(open("day16.txt").readlines()).strip() #last linebreak has to be removed 

    rulies = {}
    valid_tickets = []
    m_ticket = []

    for idx, chapter in enumerate(result.split("\n\n")):
        if idx == 0:
            rules = chapter.splitlines()
            for rule in rules:
                field, val = rule.split(": ")
                lv, rv = val.split(" or ")
                llv, rlv = lv.split("-")
                lrv, rrv = rv.split("-")

                rulies[field] = ((int(llv), int(rlv)), (int(lrv), int(rrv)))
        elif idx == 1:
            ticket = chapter.splitlines()[1]
            m_ticket = [int(val) for val in ticket.split(",")]
        elif idx == 2:
            tickets = chapter.splitlines()[1:]

            for ticket in tickets:
                vals = [int(val) for val in ticket.split(",")]
                if all(matches_any_rule(rulies, value) for value in vals):
                    valid_tickets.append(vals)
    
    possible = {}
    for idx in range(0, len(valid_tickets[0])):
        p = set() | rulies.keys()
        possible[idx] = p

    for ticket in valid_tickets:
        for i in range(0, len(ticket)):
            value = ticket[i]
            p = possible[i]

            new_p = set(field for field in p if check_rule(rulies[field], value))
            possible[i] = new_p

            if len(new_p) == 1:
                remove_singles(possible)

    print(possible)
    print([len(vals) for vals in possible.values()])

    total = 1
    for pos, field in possible.items():
        f = field.pop()
        if "departure" in f:
            total *= m_ticket[pos]

    print(total)

if __name__ == "__main__":
    day16_1()
    day16_2()