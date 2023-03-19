import heapq

def parallel_processing(n, m, data):
    output = []
    start_time= [0] * n
    thread_heap=[(0,i) for i in range (n)] 

    for i in range(m):
        processing_time=data[i]

        free_time, thread_idx=heapq.heappop(thread_heap)

        output.append((thread_idx, free_time))

        start_time[thread_idx]=free_time+processing_time

        heapq.heappush(thread_heap,(start_time[thread_idx],thread_idx))


   

    return output


def main():
   # n = 0
   # m = 0

    n,m=map(int, input().split())

    
    data = [int(x) for x in input().split()]

    result = parallel_processing(n,m,data)
    
    

    for a,start_time in result:
        print(a,start_time)



if __name__ == "__main__":
    main()
