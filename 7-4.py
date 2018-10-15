adds =[]
while True:
    add = input('Write new add to pizza, you can write "quit" to stop: ').split()
    if add == ['quit']:
        break
    adds += add
print(*adds)
