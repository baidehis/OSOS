def combine_lists(list1, list2):
    combined = []

    while list1 and list2:
        if list1[0] < list2[0]:
            combined.append(list1.pop(0))
        else:
            combined.append(list2.pop(0))
    
    # Add remaining elements from whichever list still has items
    combined += list1
    combined += list2

    return combined