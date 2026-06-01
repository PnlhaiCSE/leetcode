Cot = ['A','B','C']

def thapHN(n, i, j, k):
    if n==1:
        print(f"Chuyển đĩa {n} từ cột {Cot[i]} sang cột {Cot[j]}")
    else:
        thapHN(n-1, i, k, j)
        print(f"Chuyển đĩa {n} từ cột {Cot[i]} sang cột {Cot[j]}")
        thapHN(n-1, k, j, i)

n = int(input("Nhập số lượng đĩa: ").strip())
thapHN(n, 0, 2, 1) 