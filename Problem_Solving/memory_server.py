'''
A cloud computing company CloudO operates two servers to manage memory resource requests. These requests can be either:

- Positive integers representing memory allocation

- Negative integers representing memory deallocation

For efficient load balancing, the system distributes incoming requests alternatively between the two servers:

The first request goes to Server 1, the second to Server 2, the third to Server 1, and so on.

Write a Python program that:

- Accepts the number of requests N

- Accepts a list of N integers representing memory allocation/deallocation requests

- Calculates and prints the total memory units (allocated/deallocated) handled by Server 1 after all the requests are processed

'''

def memory_server(numOfReq, requests):
    total_memory_server1 = 0

    for i in range(numOfReq):
        if i % 2 == 0:
            total_memory_server1 += requests[i]

    return  total_memory_server1

numOfReq = int(input("Enter the number of requests: "))
requests = list(map(int,input("Enter the requests: ").split()))

result = memory_server(numOfReq, requests)

print("Total memory handled by server1: ",result)