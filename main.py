list2 = [[1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]]
for b in range(5):
    for a in range(5):
        if list2[b][a] == 1:
            led.plot(a, b)
        else:
            led.unplot(a, b)

def on_forever():
    pass
basic.forever(on_forever)
