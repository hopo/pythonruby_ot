
def count_words(text, words):
    cnt = 0
    for e in words:
        if text.lower().find(e) != -1:
            cnt += 1
    return cnt


if __name__ == '__main__':
    ex1 = count_words("How aresjfhdskfhskd you?", {
                      "how", "are", "you", "hello"})  # 3, "Example"
    print(ex1)
    ex2 = count_words("Bananas, give me bananas!!!", {
                      "banana", "bananas"})  # 2, "BANANAS!"
    print(ex2)
    ex3 = count_words(
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
        {"sum", "hamlet", "infinity", "anything"}
    )  # 1, "Weird text"
    print(ex3)
