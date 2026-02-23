def find_intrusion(signal, pattern):
    n = len(signal)
    m = len(pattern)
    found_indices = []


    if m > n or m == 0:
        return None

  
    for i in range(n - m + 1):

        if signal[i : i + m] == pattern:
            found_indices.append(i)

    if not found_indices:
        return None
    
    return found_indices


sensor_stream = [0, 1, 0, 9, 9, 5, 0, 1, 0, 9, 9, 5, 2, 3]
hack_pattern = [0, 9, 9, 5]

result = find_intrusion(sensor_stream, hack_pattern)

print(f"Сигнал: {sensor_stream}")
print(f"Патерн: {hack_pattern}")
if result:
    print(f"Hacking attempts on indexes found: {result}")
else:
    print("None")

print("-" * 30)

safe_stream = [1, 2, 3, 4, 5, 6]
result_safe = find_intrusion(safe_stream, hack_pattern)
print(f"safe signal: {result_safe}")