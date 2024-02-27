hammingMP = {1:1}
hamming = [1]

def init():
    i2, i3, i5 = 0, 0, 0
    num = 1
    while num<=20:
        hamming_number = min(hamming[i2] * 2, hamming[i3] * 3, hamming[i5] * 5)
        if hamming_number > 10 ** 18:
            return
        if hamming_number == hamming[i2] * 2:
            i2 += 1
        if hamming_number == hamming[i3] * 3:
            i3 += 1
        if hamming_number == hamming[i5] * 5:
            i5 += 1
        num+=1
        hamming.append(hamming_number)
        hammingMP[hamming_number] = num

if __name__ == "__main__":
    init()
    t = int(input())
    for _ in range(t):
        n = int(input())
        # idx = binary_search(hamming, n)
        if n not in hammingMP:
            print('Not in sequence')
        else:
            print(hammingMP[n])