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
        return len(line) in self._get_idxs_after_match(line, [0])


    def _get_idxs_after_match(self, line, start_idxs):
        if self._char:
            return [idx + 1 for idx in start_idxs if idx < len(line) and line[idx] == self._charmatch]
        else:
            return self._try_match(line, start_idxs)


    def _try_match(self, line, start_idxs):
        matched_idxs = []
        for alt in self._alternatives:
            next_idxs = [i for i in start_idxs]
            for rule in alt:
                next_idxs = Rule.__rules[rule]._get_idxs_after_match(line, next_idxs)
                if not next_idxs:
                    break
            
            for next_idx in next_idxs:
                matched_idxs.append(next_idx)

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