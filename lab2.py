def merge(left: list[int], right: list[int]) -> list[int]:
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def calc_minimum_cost(prices: list[int], discount: int) -> str:
    if not prices:
        return "0.00"
    
    sorted_prices = merge_sort(prices)
    
    num_discounts = len(sorted_prices) // 3
    
    discount_multiplier = (100 - discount) / 100.0
    
    discounted_sum = sum(sorted_prices[:num_discounts]) * discount_multiplier
    full_price_sum = sum(sorted_prices[num_discounts:])
    
    total = discounted_sum + full_price_sum
    return f"{total:.2f}"