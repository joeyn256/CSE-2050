import time
from tkinter import N
from Functions import t_const, t_lin, t_quad

def foo(f, args):
    return f(*args)

def time_f(func, args, n_trials = 10):
    t = float('inf')
    for i in range(n_trials):
        start = time.time()
        func(args)
        end = time.time()
        trial = end - start
        if trial < t:
            t = trial
    return t

def values():
    n_values = [100,200,400,600,800]
    s2 = ''
    p1 = 2
    p2 = [5,6,5,-1,4,4,12]
    for i in n_values:
        n1 = p1 * i
        n2 = p2 * i
        t1 = time_f(t_const, n1, 10)
        t2 = time_f(t_lin, n2, 10)
        t3 = time_f(t_quad, n2, 10)
        s2 = s2 + str(i) + '\t' + ("{:.6f}".format(t1*1000)) + '\t' + ("{:.6f}".format(t2*1000)) + '\t' + ("{:.2f}".format(t3*1000)) + '\n'
    s2 = s2.strip('\n')
    return s2

def built_in_1(n_trials = 10):
    n_values = [100, 1000, 10000,100000,1000000]
    L = [1,2,3,4,5]
    s4 = []
    max = -1
    for i in n_values:
        for k in range(n_trials):
            L1 = L * i
            start = time.time()
            if 6 in L1:
                return True
            end = time.time()
            s3 = (end-start)
            if s3 > max:
                max = s3
        s4.append("{:.4f}".format(max*1000))
    return s4

def built_in_2(n_trials = 10):
    n_values = [100, 1000, 10000,100000,1000000]
    L = (1,2,3,4,5)
    s4 = []
    max = -1
    for i in n_values:
        for k in range(n_trials):
            L1 = L * i
            start = time.time()
            if 6 in L1:
                return True
            end = time.time()
            s3 = (end-start)
            if s3 > max:
                max = s3
        s4.append("{:.4f}".format(max*1000))
    return s4

def built_in_3(n_trials = 10):
    n_values = [100,1000,10000,100000,1000000]
    L = 'money'
    s4 = []
    max = -1
    for i in n_values:
        for k in range(n_trials):    
            L1 = L * i
            start = time.time()
            if 'z' in L1:
                return True
            end = time.time()
            s3 = (end-start)
            if s3 > max:
                max = s3
        s4.append("{:.4f}".format(max*1000))
    return s4

"""def built_in_4():
    n_values = [100,1000,10000,100000,1000000,10000000]
    L1 = set()
    s4 = []
    for i in n_values:
        for j in range(i):
            L1.add(j)
        start = time.time()
        if -1 in L1:
            return True
        end = time.time()
        s3 = (end-start)
        s4.append("{:.6f}".format(s3*1000))
    return s4"""

def built_in_4(n_trials = 10):
    n_values = [100,1000,10000,100000,1000000]
    L1 = set()
    s4 = []
    max = -1
    for i in n_values:
        for k in range(n_trials):
            for j in range(i):
                L1.add(j)
            start = time.time()
            if -1 in L1:
                return True
            end = time.time()
            s3 = (end-start)
            if s3 > max:
                max = s3
        s4.append("{:.4f}".format(max*1000))
    return s4


"""
if __name__ == "__main__":
    L1 = [2,5,6,5,3,2,-1,4,14,4,12,14]
    a = 2
    L3 = L1 * 100
    L4 = L1 * 800

    t1 = time_f(t_const, a, 10)
    t2 = time_f(t_lin, L1, 10)
    t3 = time_f(t_quad, L1, 10)
    t4 = time_f(t_quad, L3, 10)
    t5 = time_f(t_quad, L4, 10)

    print(t1)
    t1_f = ("t(a) = {:.3g} ms".format(t1*1000))
    print(t1_f)


    print(t2)
    t2_f = ("t(L1) = {:.3g} ms".format(t2*1000))
    print(t2_f)

    print(t3)
    t3_f = ("t(L1) = {:.3g} ms".format(t3*1000))
    print(t3_f)
    t4_f1 = ("t(L3) = {:.3g} ms".format(t4*1000))
    print(t4_f1)
    t5_f1 = ("t(L4) = {:.3g} ms".format(t5*1000))
    print(t5_f1)
"""

# intiation of the beginning of the table
F = '=' * 50
L = '-' * 50

s1 = F + '\n' + 'n' + '\t' + 't_const (ms)' + '\t' + 't_lin (ms)' + '\t' + 't_quad (ms)' + '\n' + L + '\n'
s3 = F + '\n' + '\t' 'Contains (times in ms)' + '\n' + L + '\n' + 'n' + '\t' + 't_list' + '\t' + 't_tup' + '\t' + 't_str' + '\t' + 't_set' + '\n' + L + '\n'

#print(s1 + values())
#print(s3)

def table_2():
    s4 = ''
    n_vals = [100,1000,10000,100000,1000000]
    for i in range(len(n_vals)):
        s4 = s4 + str(n_vals[i]) + '\t' + str(built_in_1(1)[i]) + '\t' + str(built_in_2(1)[i]) + '\t' + str(built_in_3(1)[i]) + '\t' + str(built_in_4(1)[i]) + '\n'
    s4 = s4.strip('\n')
    return s4
    
print(s3 + table_2())



#print(built_in_1())
#print(built_in_2())
#print(built_in_3())
#print(built_in_4())







