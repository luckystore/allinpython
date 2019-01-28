from collections import Counter

text = "We hope to one day become the world's leader in free, educational resource. We are constantly "\
       "discovering and adding more free content to the website everyday. There is already an anormous "\
       "amount of resources online that can be accessed for free by anyone in the world, the main issue "\
       "right now is that very little of it id organized or structured in any way. We want to be the "\
       "solution to that problem. "

words = text.split()
Counter = Counter(words)

top_three = Counter.most_common(3)
print(top_three)