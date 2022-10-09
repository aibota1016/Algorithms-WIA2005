
def main():
    s = "algorisfunalgoisgreat"
    pattern = "algo"
    KPM(s, pattern)
    

def KPM(T, P):
    n = len(T)
    m = len(P)
    p = compute_prefix_function(P)
    q = 0
    for i in range(n):
        while q>0 and P[q] != T[i]:
            q = p[q-1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            print("Pattern occurs with shift ", i-m+1)
            q = p[q-1]
    

def compute_prefix_function(P):
    m = len(P)
    p = [0] * m
    k = 0
    for q in range(1, m):
        while k and P[q] != P[k]:
            k = p[k-1]
        if P[k] == P[q]:
            k += 1
            p[q] = k
    return p



if __name__ == "__main__":
    main()