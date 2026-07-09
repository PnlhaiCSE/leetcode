# chuỗi đối xứng max bằng quy hoạch động

def substr(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    count = 1
    for i in range(n):
        dp[i][i] = True

    for cd in range(2, n+1):
        if cd == 2:
            for i in range(n-1):
                j = i + 1
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    dp[i][j] = True
                    count = max(count,cd)
        else:
            for i in range(n-cd+1):
                j = i + cd - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count = max(count,cd)
                else:
                    dp[i][j] = False
    return count
# test
s = str(input("Nhập chuỗi: ").strip())
print(substr(s))
'''
s = 'abcecaced'
sub = ecace    kq = 5
s = 'rcaeacr' kq = 7
'''