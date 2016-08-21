#1〜30までのFizzBuzzの結果をファイルに書き込むプログラム

if __name__ == "__main__":

    f = open("shiren1-2.txt", "w", encoding="utf-8")

    for counter in range(1,31):
        if counter % 15 == 0:
            f.write("FizzBuzz\n")
            continue
        elif counter % 5 == 0:
            f.write("Buzz\n")
            continue
        elif counter % 3 == 0:
            f.write("Fizz\n")
            continue
        hoge = str(counter) + "\n"
        f.write(hoge)

    f.close()
