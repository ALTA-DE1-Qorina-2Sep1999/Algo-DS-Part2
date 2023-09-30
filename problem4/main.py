def count_item_and_sort(items):
    sorted_item = sorted(items)
    element_count = {}
    for element in sorted_item:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    sorted_elements = sorted(element_count.items(), key=lambda x: x[1])
    formatted_list = ' '.join([f"{item[0]}->{item[1]}" for item in sorted_elements])
    return formatted_list

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"