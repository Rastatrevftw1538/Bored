'''list all the natural numbers below 20 that are multiples of 3(Foo) or 5(Bar), we get
3: Foo
5: Bar
6: Foo
9: Foo
10: Bar
12: Foo
15: Foobar
18: Foo

Find all Foobars under 1000'''


def main():
    for x in range(15, 1000, 15):
        print(f"{x}:Foobar")


main()
