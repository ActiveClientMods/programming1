import random

tree_height = 15

RED = '\033[91m'
GREEN = '\033[92m'
BROWN = '\033[33m'
RESET = '\033[0m'

for i in range(tree_height):
    spaces = " " * (tree_height - i - 1)
    tree = ''.join([
        f'{GREEN}#{RESET}'
        if random.random() > 0.2 else f'{RED}O{RESET}'
        for _ in range(2 * i + 1)
        ])
    print(spaces + tree)

log_width = (tree_height // (2 * 2)) + 1

if log_width % 2 == 0 and log_width >= 3:
    log_width += 1
elif log_width <= 2:
    log_width -= 1

log_height = (2 * tree_height) // 5
log_spaces = " " * ((tree_height * 2 - 1 - log_width) // 2)

for _ in range(log_height):
    print(log_spaces + (BROWN+'|' * log_width+RESET))
