# Q1 — Basic for Loop

print("Basic for Loop")
for i in range(1, 6):
    print(i)


# Q2 — for + continue

print("Continue example:")
for i in range(6):
    if i == 3:
        continue
    print(i)


# Q3 — for + break

print("Break example:")
for i in range(10):
    if i == 4:
        break
    print(i)