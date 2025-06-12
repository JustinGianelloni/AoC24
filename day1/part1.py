def parse_lists(list_a: list[int], list_b: list[int]) -> int:
    answer: int = 0
    for i, item in enumerate(list_a):
        answer += abs(list_a[i] - list_b[i])
    return answer


def parse_input(input: list[str]) -> int:
    list_a: list[int] = []
    list_b: list[int] = []
    for line in input:
        parts: list[str] = line.split("   ")
        list_a.append(int(parts[0]))
        list_b.append(int(parts[1]))
    list_a.sort()
    list_b.sort()
    return parse_lists(list_a, list_b)


def main() -> None:
    with open("input.txt", "r") as file:
        input: list[str] = file.readlines()
    answer: int = parse_input(input)
    print(f"The answer is {answer}")


if __name__ == "__main__":
    main()
