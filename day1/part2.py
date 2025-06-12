from collections import Counter


def parse_lists(list_a: list[int], list_b: list[int]) -> int:
    answer: int = 0
    counter: Counter = Counter(list_b)
    for item in list_a:
        answer += item * counter.get(item, 0)
    return answer


def parse_input(input: list[str]) -> int:
    list_a: list[int] = []
    list_b: list[int] = []
    for line in input:
        parts: list[str] = line.split("   ")
        list_a.append(int(parts[0]))
        list_b.append(int(parts[1]))
    return parse_lists(list_a, list_b)


def main() -> None:
    with open("input.txt", "r") as file:
        input: list[str] = file.readlines()
    answer: int = parse_input(input)
    print(f"The answer is {answer}")


if __name__ == "__main__":
    main()
