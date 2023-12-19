tree_height = 15

for i in range(1, tree_height + 1):
    spaces = " " * (tree_height - i)
    hashtags = "#" * (2 * i - 1)
    print(spaces + hashtags)

log_width = (tree_height // (2 * 2)) + 1

if log_width % 2 == 0 and log_width >= 3:
    log_width += 1
elif log_width <= 2:
    log_width -= 1

log_height = (2 * tree_height) // 5
log_spaces = " " * ((tree_height * 2 - 1 - log_width) // 2)

for _ in range(log_height):
    print(log_spaces + '|' * log_width)