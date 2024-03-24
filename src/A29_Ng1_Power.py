
import io
import sys

_INPUT = """\
5 6
"""
sys.stdin = io.StringIO(_INPUT)

# 解答までの流れ
# 1.素数のリストを作成する
# 2.素数✕N < A のリストを作成
# 3.B = (素数✕N) / M の余りを Bに乗算
# 4.3でできた整数をMで割った余りを求める
# ※18 / 5 の余りは （6 / 5の余り）✕ (3 / 5の余り) / 5 で求められる
a, b = map(int, input().split())
# 割る数
CONST_DIVISION = 10 ** 9 + 7
CONST_NUM = a ** b
# 100までの素数リスト
# PrimeNumberList = [2 ,3 ,5, 7, 11, 13 ,17, 19, 23 , 29, 31, 37, 41, 43, 47, 53, 59, 61 ,67, 71 ,73, 79, 83, 89, 97]

# 素数リストの算出
# 素数列挙は数学の永遠のテーマのため高速算出アルゴリズムはライブラリを使うのがよい。
# これは貼り付け（https://ebisuke33.hatenablog.com/entry/eratosthenes）
def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes

# 素数✕MがN以下のペアを算出
def createFactdict(num, primeNumberList):
    ret  = dict()
    for i in primeNumberList:
        if i > num: break
        ret[i] , ii = 0, i
        # print(ret)
        # print(ii)
        while ii <= num:
            ret[i] += num // ii
            ii *= i
    
    return ret

def factMod(fctDict, M):
  ret = 1
  for p in fctDict.keys():
    ret *= pow(p,fctDict[p], M)
    ret %= M
  return ret

# step1 素数リスト作成
primeNumberList = sieve_of_eratosthenes(a**b)
#print(primeNumberList)
# step2 素数リストの因数dict作成
factDict = createFactdict(a**b, primeNumberList)
#print(factDict)
# step 3 4 割り算した答えを作成
ret = factMod(factDict, CONST_DIVISION)
print(ret)


