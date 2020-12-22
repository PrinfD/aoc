import re
import numpy as np


class Rule:
    __rules = {}

    def __init__(self, rule, key):
        self._init_rule(rule)
        Rule.__rules[key] = self


    def _init_rule(self, rule):
        self._alternatives = []
        if rule == '"a"' or rule == '"b"':
            self._charmatch = rule[1]
            self._char = True
        else:
            self._charmatch = []
            self._char = False
            alts = rule.strip().split("|")
            for alt in alts:
                rules = alt.split()
                self._alternatives.append(rules)
    

    def set_rule(self, newrule):
        self._init_rule(newrule)


    def full_match(self, line):
        return len(line) in self.get_idxs_after_match(line, 0)


    def get_idxs_after_match(self, line, start_idx):
        if self._char:
            if start_idx >= len(line) or line[start_idx] != self._charmatch:
                return []
            else:
                return [start_idx + 1]
        else:
            return self._try_match(line, start_idx)


    def _try_match(self, line, start_idx):
        matched_idxs = []
        next_idxs = [start_idx]
        for alt in self._alternatives:
            for rule in alt:
                new_next_idxs = []
                for next_idx in next_idxs:
                    res = Rule.__rules[rule].get_idxs_after_match(line, next_idx)
                    for next_res in res:
                        new_next_idxs.append(next_res)
                        
                next_idxs = new_next_idxs
                if not new_next_idxs:
                    break
            
            for next_idx in next_idxs:
                matched_idxs.append(next_idx)
            
            next_idxs = [start_idx]

        return matched_idxs

def read():
    content = "".join(line for line in open("day19.txt"))
    rules, text_string = content.strip().split("\n\n")
    text_arr = text_string.split()
    return (rules, text_arr)

def parse_rules(rules):
    rulemap = {rule.split(": ")[0] : Rule(rule.split(": ")[1], rule.split(": ")[0]) for rule in rules.split("\n")}
    return rulemap

def day19_1():
    rule_str, text = read()
    rules = parse_rules(rule_str)
    result = [rules["0"].full_match(line) for line in text]
    print(sum(result))

def day19_2():
    rule_str, text = read()
    rules = parse_rules(rule_str)
    rules["8"].set_rule("42 | 42 8")
    rules["11"].set_rule("42 31 | 42 11 31")
    result = [rules["0"].full_match(line) for line in text]
    print(sum(result))


if __name__ == "__main__":
    day19_1() #184
    day19_2() #389