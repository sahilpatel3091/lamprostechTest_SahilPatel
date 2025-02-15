'''
array = [5, 2, 5, 3, 5, 3, 1]
k = 2

dict = {
    frequency : value
    3 : 5,
    1 : 2,
    2 : 3,
    1 : 1
}

Sort this dictionary 

Return top k element
'''



from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    This function will find top k frequent element

    Parameter:
        nums: List[int] -> so num is basically list of integer
        k: int -> k is also integer
    Return:
        List of k most frequent elements
    """

    
    # Initalize empty dictionery
    freq_list = {}

    # Counting frequency of each number present in list
    for num in nums:
        # Check if num is already a key in dictionary
        freq_list[num] = freq_list.get(num, 0) + 1 

    # Converting the dictionary items into a list of (num, frequency) tuples
    frequency_list = list(freq_list.items())

    # Sort the list by frequency in descending order
    sort_freq_list = sorted(frequency_list, key=lambda item: item[1], reverse=True)

    # Extract the top k most frequent element
    #top_k_elements = [num for num, freq in sort_freq_list[:k]]
    top_k_elements = []
    for num, freq in sort_freq_list[:k]:
        top_k_elements.append(num)

    return top_k_elements

# Example usage:
nums = [5, 2, 5, 3, 5, 3, 1]
k = 2
print(topKFrequent(nums, k))

