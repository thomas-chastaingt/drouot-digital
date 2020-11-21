coins_values = [1 ,2 ,5 ,10, 20, 50 ,100]
itemValue = 275
paidValue = 300

#define the method to change coins
def change(itemValue, paidValue, coins_values):
    map = {}
    render = paidValue - itemValue

    for c in coins_values:
        map.update({c : 0})

    i = len(coins_values) - 1
    while render > 0:
        val = coins_values[i]
        if render < val:
            i -= 1
        else:
            map[val] += 1
            render -= val
    print(map)
    return map

change(itemValue, paidValue, coins_values)