def get_next_posibilities(joltage, adapters):
    return [adapter for adapter in adapters if adapter>joltage and  adapter<=joltage+3]


cache = {}
def generate_list(start_joltage, adapter_list):
    print(f"generate_list({start_joltage}, {len(adapter_list)})")
    # Get next posibilities
    sequences = []

    if start_joltage in cache:
        print(f"Returning from cache for {start_joltage}")
        return cache[start_joltage]

    next_posibilities = get_next_posibilities(start_joltage, adapter_list)
    print(f"posibilities: {len(next_posibilities)})")
    for possibility in next_posibilities:
        left_over_adapters = [adapter for adapter in adapter_list if adapter > possibility]
        if not left_over_adapters:
            sequences.append([possibility])
        else:
            gl = generate_list(possibility, left_over_adapters)
            for l in gl:
                sequences.append([possibility]+l)

    # Let's cache it
    cache[start_joltage] = sequences
    # print(f"Cache {start_joltage}, {sequences}")
    return sequences


# Read input
f = open("ass-day-10-input.txt", "r")
lines = f.read().split("\n")
all_adapter_list = [int(line) for line in lines]

adapter_order = generate_list(0, all_adapter_list)
print(len(adapter_order))
