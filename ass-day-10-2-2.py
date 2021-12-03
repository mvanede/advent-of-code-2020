def get_next_posibilities(joltage, adapters):
    return [adapter for adapter in adapters if adapter>joltage and  adapter<=joltage+3]


cache = {}
def count_max_leaves(start_joltage, adapter_list):
    # print(f"generate_list({start_joltage}, {len(adapter_list)})")
    sequences = []

    if start_joltage in cache:
        # print(f"Returning from cache for {start_joltage}")
        return cache[start_joltage]

    next_posibilities = get_next_posibilities(start_joltage, adapter_list)
    # print(f"posibilities: {len(next_posibilities)}")

    max_leaves = 0
    for possibility in next_posibilities:
        left_over_adapters = [adapter for adapter in adapter_list if adapter > possibility]
        if not left_over_adapters:
            sequences.append([possibility])
            max_leaves += 1
        else:
            max_leaves += count_max_leaves(possibility, left_over_adapters)

    # Let's cache it
    cache[start_joltage] = max_leaves
    # print(f"Cache {start_joltage}, {sequences}")
    return max_leaves


# Read input
f = open("ass-day-10-input.txt", "r")
lines = f.read().split("\n")
all_adapter_list = [int(line) for line in lines]

adapter_order_possibilities = count_max_leaves(0, all_adapter_list)
print(adapter_order_possibilities)
