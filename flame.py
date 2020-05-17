name1 = input("ENTER YOUR NAME:")
name2 = input("ENTER YOUR BOY FRIEND/GIRL FRIEND NAME:")
count = None
name1 = list(name1)
name2 = list(name2)

for i in name1:
    if i in name2:
        name1.remove(i)
        name2.remove(i)

total_letters = len(name1) + len(name2)

Flame = ["F", "L", "A", "M", "E", "S"]
i = 1


def reorder(count):
    global Flame
    if count == 2:
        Flame = Flames[2:]
        Flame.append(Flames[0])
        Flame.append(Flames[1])
        print(Flame)
        return Flame
    elif count == 3:
        Flame = Flames[3:]
        Flame.append(Flames[0])
        Flame.append(Flames[1])
        Flame.append(Flames[2])
        print(Flame)
        return Flame
    elif count == 4:
        Flame = Flames[4:]
        Flame.append(Flames[0])
        Flame.append(Flames[1])
        Flame.append(Flames[2])
        Flame.append(Flames[3])
        print(Flame)
        return Flame
    elif count == 1:
        Flame = Flames[1:]
        Flame.append(Flames[0])
        print(Flame)
        return Flame
    else:
        Flame = Flames[0:]
        print(Flame)
        return Flame


while i < 5:

    if total_letters <= len(Flame):
        count = len(Flame) - 1
        print(Flame)
        del Flame[total_letters - 1]
        Flames = Flame.copy()
        print(count)
        print(Flames)
        reorder(count)
        print(Flame)
    elif total_letters % len(Flame) == 0:
        count = len(Flame) - 1
        print(Flame)
        del Flame[len(Flame) - 1]
        Flames = Flame.copy()
        print(count)
        print(Flames)
        reorder(count)
        print(Flame)
    else:
        b = total_letters % len(Flame)
        count = b - 1
        print(Flame)
        del Flame[b - 1]
        Flames = Flame.copy()
        print(count)
        print(Flames)
        reorder(count)
        print(Flame)

    if len(Flame) == 1:
        break

i += 1

if Flame[0] == "F":
    print("YOU BOTH ARE FRIENDS")
elif Flame[0] == "L":
    print("YOU BOTH WILL FALL IN LOVE SOON")
elif Flame[0] == "A":
    print("YOU BOTH HAVE AFFECTION OVER EACH OTHER")
elif Flame[0] == "M":
    print("YOU BOTH WILL GET MARRIED EACH OTHER")
elif Flame[0] == "E":
    print("YOU BOTH WILL BECOME ENEMIES SOON")
else:
    print("YOU BOTH ARE BROTHERS AND SISTERS")
