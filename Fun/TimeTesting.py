import time

start = time.time()

print('hello world')
    
end = time.time()
print(str((end-start) * 1000) + "ms")