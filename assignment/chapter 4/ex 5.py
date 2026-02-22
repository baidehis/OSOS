def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    pairs = []
    
    for number in number:
        if number % 2 == 0: # even number
            if odd_queue.size > 0:
                odd = odd_queue.dequeue()
                pairs.append((number, odd))
            else:
                even_queue.enqueue(number)
        else: # odd number
            if even_queue.size > 0:
                even = even_queue.dequeue()
                pairs.append((even, number))
            else:
                odd_queue.enqueue(number)

    return pairs



nums = [1, 2, 3, 4, 5, 6]
print(get_pairs(nums))

