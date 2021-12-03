


def get_next_posibilities(joltage, adapters):
    return [adapter for adapter in adapters if adapter>joltage and  adapter<=joltage+3]

def generate_list(start_joltage, adapter_list):
    adapter_sequences = []

    # while len(all_adapter_list):
    possible_adapters = get_next_posibilities(start_joltage, adapter_list)
    print("---------------------------------------")
    print(f"generate_list for {start_joltage} with {adapter_list} = {possible_adapters}")


    for pa in possible_adapters:
        print(f"Adapter: {pa}")
        left_over_adapters = [adapter for adapter in adapter_list if adapter>pa]

        # Also remove all adapters
        print(f"Left over adapters: {left_over_adapters}")
        # print(f"Current joltage: {start_joltage + pa}")

        y = []
        y.append(pa)
        #
        if not left_over_adapters:
            adapter_sequences.append(y)
        else:
            print("Go to next generate_list")
            for possibility in generate_list(start_joltage + pa, left_over_adapters):
                print(f"Possibility in generated_list: {possibility}")
                if isinstance(possibility, list):
                    y += possibility
                else:
                    y.append(possibility)
                adapter_sequences.append(y)

                print(f"Current adapter_sequences: {adapter_sequences}")

    print(f"Return sequence {adapter_sequences}")
    return adapter_sequences


# Read input
f = open("ass-day-10-input.txt", "r")
lines = f.read().split("\n")
all_adapter_list = [int(line) for line in lines]

adapter_order = generate_list(0, all_adapter_list)
# adapter_order.append(adapter_order[-1] + 3)
print(adapter_order)
