# -*- coding: utf-8 -*-

# Finger exercise: You are wandering through a forest and see a field of
# delicious-looking mushrooms. You fill your basket with them, and head home prepared
# to cook them up and serve them to your husband. Before you cook them, however,
# he demands that you consult a book about local mushroom species to check whether
# they are poisonous. The book says that 80% of the mushrooms in the local forest
# are poisonous. However, you compare your mushrooms to the ones pictured in the book,
# and decide that you are 95% certain that your mushrooms are safe.

# How comfortable should you be about serving them to your husband (assuming
# that you would rather not become a widow)?

poison = 0.8
no_poison = 1 - poison
certain = 0.95
false_certain = 1 - certain

# Bayes' Theorem:
# P(A|B) = (P(A) * P(B|A)) / P(B)

comfort = (no_poison*certain) / \
    (no_poison*certain + poison*false_certain)

print(
    f"You should have {100*comfort:.2f}% confidence that it's safe to eat the mushrooms.")
