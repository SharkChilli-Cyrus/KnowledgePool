from queue import Queue

def the_last_one(name_list, num):
    simple_queue = Queue(maxsize=0) # maxsize <= 0 ==> infinity
    for name in name_list:
        simple_queue.put(name)

    while simple_queue.qsize() > 1:
        for i in range(num-1):
            out = simple_queue.get()
            simple_queue.put(out) # become a circle
        
        simple_queue.get()
    
    return simple_queue.get()

if __name__ == "__main__":
    name_list = ["Andy", "Ben", "David", "Cindy", "Eric", "Tom", "Jerry", "Linda", "Garry", "Belly", "Robot"]
    num = 3

    winner = the_last_one(name_list, num)
    winner_index = name_list.index(winner)
    print(winner, winner_index + 1)