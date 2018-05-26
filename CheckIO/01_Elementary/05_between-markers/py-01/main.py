
def between_markers(text: str, begin: str, end: str) -> str:
    bi = text.find(begin)
    ei = text.find(end)

    if bi == -1:
        bi = 0
    else:
        bi += len(begin)
    if ei == -1:
        ei = len(text)

    return text[bi:ei] 


if __name__ == '__main__':
    ex1 =  between_markers('What is >apple<', '>', '<') # "apple", "One sym"
    print(ex1)
    ex2 =  between_markers("<head><title>My new site</title></head>", "<title>", "</title>") # "My new site", "HTML"
    print(ex2)
    ex3 =  between_markers('No[/b] hi', '[b]', '[/b]') # 'No', 'No opened'
    print(ex3)
    ex4 =  between_markers('No [b]hi', '[b]', '[/b]') # 'hi', 'No close'
    print(ex4)
    ex5 =  between_markers('No hi', '[b]', '[/b]') # 'No hi', 'No markers at all'
    print(ex5)
    ex6 =  between_markers('No <hi>', '>', '<') # '', 'Wrong direction'
    print(ex6)

