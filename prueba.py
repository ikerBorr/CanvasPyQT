WIDTH = 1000
HEIGHT = 500

def area(w, h) -> int:
    return int(WIDTH / w) * int(HEIGHT / h)

def cal1(w, h) -> int:
    a = WIDTH % w
    b = HEIGHT % h
    m = WIDTH % h
    n = HEIGHT % w

    t1 = (1 + a) * (1 + b)
    t2 = (1 + m) * (1 + n)

    if  t1 < t2:
        return area(w, h)
    else:
        return area(h, w)

def cal2(w, h) -> int:
    a = int(WIDTH / w)
    b = int(HEIGHT / h)
    m = int(WIDTH / h)
    n = int(HEIGHT / w)

    t1 = a * b
    t2 = m * n

    if t1 > t2:
        return area(w, h)
    else:
        return area(h, w)


def main() -> None:
    w = 1

    while w <= WIDTH:
        h = 1
        while h <= HEIGHT:
            a1 = cal1(w, h)
            a2 = cal2(w, h)

            if a1 != a2:
                print("w: ", w, " h: ", h)
                print("A1: ", a1, " A2: ", a2)
                assert False

            h = h + 1
        w = w + 1


if __name__ == "__main__":
    for i in range(100):
        main()
    print("NO error")

