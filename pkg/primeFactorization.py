import random
import math

def primeFactorization(max:int):
    # ↑引数は必ず型を定義
    # 変数名をa, b, cってするのは自分だけが使うならいいけどほんとはよくない
    # 英単語略語はOK 代表例: response -> res, request -> req, object -> obj とかね
    # ↑オリジナル略はやめよう(大体相場が決まってる)
    x = random.randint(2,max)
    l = x
    sqrt = int(math.sqrt(x)) # 分かりやすい変数名
    k = 2
    print(x , sqrt)
    array = []
    if sqrt == x:
        print(l,"= 1 x",x)
    else:
        array.append(2)
        while 1 < k <= sqrt:
            i = 2
            while 1 < i <= k:
                if k % i == 0:
                    i = 2
                    break
                else:
                    if i == k-1:
                        array.append(k)
                    i += 1
            k += 1
        result = []
        # 変数名は英語で書こう
        for factor in array:

            while x % factor == 0:
                x /= factor
                result.append(factor)
        o = "1"
        for resultFactor in result: # 変数名のナンバリングはやめよう
            o += "x " + str(resultFactor)
        if not result:
            print(l,"= 1x",l)
        elif x != 1:
            print(l,"= ",o,"x",str(int(x)))
        else:
            print(l,"= ",o)