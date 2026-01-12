import random

def calculate_mean_median_mode(numbers):
    sorted_numbers = sorted(numbers)
    total = len(sorted_numbers)
    #find mean
    mean = sum(sorted_numbers) / total
    #find median
    middle_index = total // 2
    if total % 2 == 0:
       median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
       median = sorted_numbers[middle_index]
    #find mode
    freq = {}
    for num in sorted_numbers:
        freq[num] = freq.get(num, 0) + 1
    mode = max(freq, key=freq.get)

    return mean, median, mode

#main
random_numbers = []
# Generate 100 random numbers between 100 and 150
for _ in range(100):
    num = random.randint(100, 150)
    random_numbers.append(num)
        
mean_result, median_result, mode_result = calculate_mean_median_mode(random_numbers)

print("Mean:", mean_result)
print("Median:", median_result)
print("Mode:", mode_result)
