# encoding=utf-8

# 现有 i 张十元纸币，k 张五元纸币，j 张两元纸币, 购物后要支付 n 元（i,j,k,n为整数）。
# 要求编写一个复杂度为 O(1) 的函数 FindSolution( i,j,k, n)，
# 功能是计算出能否用现在手上拥有的纸币是否足够并能刚好拼凑齐 n 元，而不需要找零。
# 1、如果可以，在屏幕输出一个方案并结束；（例子：“需要 2 张十元纸币，1 张五元纸币， 1 张两元纸币，刚好可凑齐 27 元”）
# 2、如果不可以，在屏幕输出 “不能刚好凑齐 n 元”。

# reference
# https://codeleading.com/article/96691964424/


def find_solution(i, j, k, n):
    a, b = divmod(n, 10)
    if b in [1, 3]:
        # 1
        print(f'不能刚好凑齐{n}元')
    else:
        # 2
        c = 5 * j // 10
        d = b // 2 if n % 2 == 0 else (b - 5) // 2
        e = 2 * (k - d) // 10
        if a > i + c + e or e < 0:
            # 2.1
            print(f'不能刚好凑齐{n}元')
        else:
            # 2.2
            if i >= a:
                # 2.2.1
                num_10 = a
                num_5 = 0 if n % 2 == 0 else 1
                num_2 = d
            else:
                # 2.2.2
                num_10 = i
                if (n - 10 * i) // 5 >= j:
                    # 2.2.2.1
                    num_5 = j
                    num_2 = d + (n - 10 * i - 5 * j) // 2
                else:
                    # 2.2.2.2
                    num_5 = (n - 10 * i) // 5
                    num_2 = d
            if 10 * num_10 + 5 * num_5 + 2 * num_2 == n:
                print(f'需要 {num_10} 张十元纸币，{num_5} 张五元纸币， {num_2} 张两元纸币，刚好可凑齐 {n} 元')
            else:
                print(f'不能刚好凑齐{n}元')


if __name__ == '__main__':
    # 1
    find_solution(100, 10, 10, 1)
    find_solution(100, 10, 10, 3)
    # 2.1
    find_solution(100, 10, 10, 180)
    find_solution(100, 10, 2, 88)
    # 2.2.1
    find_solution(100, 10, 2, 82)
    find_solution(100, 10, 10, 87)
    # 2.2.2.1
    find_solution(10, 1, 100, 122)
    # 2.2.2.2
    find_solution(10, 30, 100, 122)
