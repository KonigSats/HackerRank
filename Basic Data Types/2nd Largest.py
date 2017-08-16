if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    largest = max(arr)
    arr = [x for x in arr if x != largest]
    print(max(arr))