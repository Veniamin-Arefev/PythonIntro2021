import random
import sys

L = int(input())
words = sys.stdin.read().replace("\n    ", " @ ").split()

triplet = {}
for i in range(len(words) - 2):
    triplet.setdefault((words[i], words[i + 1]), []).append(words[i + 2])

start_index = random.randint(0, len(words) - 2)
answer = [words[start_index - 1], words[start_index]]
for i in range(L - 2):
    answer.append(random.choice((triplet[(answer[-2], answer[-1])])))

answer = (" ".join(answer)).replace(' @ ', "\n    ")
print(answer)
