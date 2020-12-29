from logic import TruthTable


TruthTable (["p", "q"], ["p or q"]).display ()
print ()

#Warmup
TruthTable (["a", "b"], ["a and -b"]).display ()
print ()

TruthTable (["a", "b", "c"], ["a and b", "-c", "(a and b) or -c"]).display ()
print ()

#Rules of inference
TruthTable (["p", "q"], ["p -> q", "(p -> q) and p", "((p -> q) and p) -> q"]).display () #Modus Ponens
print ()

TruthTable (["p", "q"], ["p -> q", "-q and (p -> q)", "(-q and (p -> q)) -> -p"]).display () #Modus Tollens
print ()

TruthTable (["p", "q", "r"], ["p -> q", "q -> r", "(p -> q) and (q -> r)", "p -> r", "((p -> q) and (q -> r)) -> (p -> r)"]).display () #Hypotheical Syllogism
print ()

TruthTable (["p", "q"], ["p or q", "(p or q) and -p", "((p or q) and -p) -> q"]).display () #Disjuctive Syllogism
print ()

TruthTable (["p", "q"], ["p or q", "p -> (p or q)"]).display () #Addition
print ()

TruthTable (["p", "q"], ["p and q", "(p and q) -> p"]).display () #Simplification
print ()

TruthTable (["p", "q"], ["p and q", "((p) and (q)) -> (p and q)"]).display () #Conjunction
print ()

TruthTable (["p", "q", "r"], ["p or q", "-p or r", "((p or q) and (-p or r))", "q or r", "((p or q) and (-p or r)) -> (q or r)"]).display () #Resolution
print ()
