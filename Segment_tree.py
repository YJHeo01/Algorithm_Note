import sys, math

input = sys.stdin.readline

def main():

def init(i):
    i += tree_size
    tree[i] += 1
    i //= 2
    while i:
        tree[i] = tree[2*i] + tree[2*i+1]
        i //= 2

def update(i):
    i += tree_size
    tree[i] -= 1
    i //= 2
    while i:
        tree[i] = tree[2*i] + tree[2*i+1]
        i //= 2

def query(l, r):
    l += tree_size
    r += tree_size
    ret_value = 0
    while l <= r:
        if l % 2 == 1:
            ret_value += tree[l]
            l += 1
        if r % 2 == 0:
            ret_value += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return ret_value

if __name__ == "__main__":
    n,k = map(int,input().split())
    tree_size = 2 ** math.ceil(math.log2(n))
    tree = [0] * (2 * tree_size)
    main()
