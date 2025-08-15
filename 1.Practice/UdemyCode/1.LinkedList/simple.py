import time 


# nemo = ['nemo']


# def findNemo(array):
#     t = time.time()
#     for i in range(len(array)):
#         if array[i] =="nemo":
#             print("Found Nemo")
#     t1 = time.time()
#     print(f"Call to find Nemo took: {(t1-t) * 1000:.2f} milliseconds.")

# findNemo(nemo)
    

# nemo =["nemo"]
# everyone = ["dory","bruce","marlin","nemo","gill","bloat","nigel","squirt","darla","hank"];

# def findNemo(array):
#     t0 =time.time()
#     for i in range(len(array)):
#         if array[i] =="nemo":
#             print("Nemo is found.")
#     t1 = time.time()
#     print(f"Call to find Nemo took: {(t1-t0)*1000:.2f} milliseconds.")

# findNemo(everyone)

### Time ### 
# nemo = ['nemo']
# everyone = ['dory','bruce','marlin','nemo','gill','bloat','nigel','squirt','darla','hank']

# large = ['nemo'] * 10000

# def findNemo(array):
#     t0 =time.time()
#     for i in range(len(array)):
#         if array[i] =="nemo":
#             print("Nemo is found.")
#         t1 = time.time()
#         print(f"Call to find Nemo took: {(t1-t0)*10000:.2f} milliseconds.")

# findNemo(everyone)


## Scale ### 
nemo = ['nemo']
everyone = ['dory','bruce','marlin','nemo','gill','bloat','nigel','squirt','darla','hank']

large = ['nemo'] * 10000

def findNemo(array):
    t0 =time.perf_counter()
    for i in range(len(array)):
        if array[i] =="nemo":
            print("Nemo is found.")
        t1 = time.perf_counter()
        print(f"Call to find Nemo took: {(t1-t0)*10000:.2f} milliseconds.")

findNemo(everyone)

