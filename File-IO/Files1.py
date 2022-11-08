
def read_series(filename: str):
    f = open(filename, mode='rt', encoding='utf-8')
    series = []
    for line in f:
        a = int(line.strip())
        series.append(a)
    f.close()
    return series

def main(filename: str):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main(filename='text.txt')

