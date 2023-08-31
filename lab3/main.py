import timeit as tt
import GreedyGP as ggp
import BruteforceGP as bgp

def tolistofinput(s):
    arr = []
    for i in s: arr.append(i)
    return arr

arr1 = ['G', 'P', 'P', 'G', 'P']
k = 1
t1 = tt.default_timer()
r = bgp.grabNgub(arr1, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 1 (Brute force algorithm):",r)
print("Time used:",t2)
print("\n")
t1 = tt.default_timer()
r = ggp.grabNgub(arr1, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 1 (Greedy algorithm):",r)
print("Time used:",t2)
print("\n")
arr2 = ['P', 'P', 'G', 'G', 'P', 'G']
k = 2
t1 = tt.default_timer()
r = bgp.grabNgub(arr2, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 2 (Brute force algorithm):",r)
print("Time used:",t2)
print("\n")
t1 = tt.default_timer()
r = ggp.grabNgub(arr2, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 2 (Greedy algorithm):",r)
print("Time used:",t2)
print("\n")
arr3 = ['G', 'P', 'G', 'P', 'P', 'G']
k = 3
t1 = tt.default_timer()
r = bgp.grabNgub(arr3, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 3 (Brute force algorithm):",r)
print("Time used:",t2)
print("\n")
t1 = tt.default_timer()
r = ggp.grabNgub(arr3, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 3 (Greedy algorithm):",r)
print("Time used:",t2)
print("\n")
arr4 = tolistofinput('GPGPGPGPGPGPGPGPGPGP')
k = 3
'''t1 = tt.default_timer()
r = bgp.grabNgub(arr4, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 4 (Brute force algorithm):",r)
print("Time used:",t2)
print("\n")'''
t1 = tt.default_timer()
r = ggp.grabNgub(arr4, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 4 (Greedy algorithm):",r)
print("Time used:",t2)
print("\n")
arr5 = tolistofinput('GGPPGGGGPPPG')
k = 3
t1 = tt.default_timer()
r = bgp.grabNgub(arr5, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 5 (Brute force algorithm):",r)
print("Time used:",t2)
print("\n")
t1 = tt.default_timer()
r = ggp.grabNgub(arr5, k)
t2 = tt.default_timer()-t1
print("Maximum of Passenger(s) can ride Grab(s) of input 5 (Greedy algorithm):",r)
print("Time used:",t2)
print("\n")