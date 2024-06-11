def filter_short_strings(input_array):
    result_array = []
    for string in input_array:
        if len(string) <= 3:
            result_array.append(string)
    return result_array

input1 = ["Hello", "2", "world", ":-)"]
input2 = ["1234", "1567", "-2", "computer science"]
input3 = ["Russia", "Denmark", "Kazan"]

output1 = filter_short_strings(input1)
output2 = filter_short_strings(input2)
output3 = filter_short_strings(input3)

print(output1)  # ["2", ":-)"]
print(output2)  # ["-2"]
print(output3)  # []