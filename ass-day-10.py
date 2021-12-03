


def get_next_posibilities(joltage, adapters):
    return [adapter for adapter in adapters if adapter<=joltage+3]

def generate_list(start_joltage, all_adapter_list):
    adapter_order = []

    while len(all_adapter_list):
        possible_adapters = get_next_posibilities(start_joltage, all_adapter_list)
        possible_adapters.sort()
        adapter_order += possible_adapters
        print(f"Possible adapters: {possible_adapters}")

        all_adapter_list= list(set(all_adapter_list) - set(possible_adapters))
        print(f"Left over adapters: {all_adapter_list}")

        start_joltage=max(possible_adapters)
        print(f"Current joltage: {start_joltage}")

    return adapter_order

# Read input
f = open("ass-day-10-input.txt", "r")
lines = f.read().split("\n")
all_adapter_list = [int(line) for line in lines]

adapter_order = generate_list(0, all_adapter_list)
adapter_order.append(adapter_order[-1] + 3)
print(adapter_order)

ones = 0
threes = 0
start=0
for a in adapter_order:
    if a==start+1:
        ones+=1
    if a==start+3:
        threes+=1
    start=a

print(f"Ones: {ones} threes: {threes}, multiplied: {ones*threes}")

# possible_adapters = get_next_posibilities(current_joltage, adapter_list)
# # possible_adapters.sort()
# print(f"Possible adapters: {possible_adapters}")
