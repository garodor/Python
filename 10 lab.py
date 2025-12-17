def main():
    A = []
    while True:
        comm = input("Что нужно сделать? ")
        if comm == "add":
            data_matrix(A)
        elif comm == "show":
            print_matrix()
        elif comm == "exit":
            return
        else:
            print("Неправильная комманда")

def data_matrix(A):
    with open('test.txt', 'a') as file:
        B = []
        B.append(input("Введите ФИО "))
        B.append(input("Введите Группу "))
        A.append(B)
        file.write(' '.join(B) + '\n')

def print_matrix():
    with open('test.txt', 'r') as file:
        found = False
        num = int(input("Информацию о каком ученике нужно дать информацию? "))
        for line_num, line in enumerate(file, 1):  
                if line_num == num:  
                    print(line.strip())
                    found = True
                    break  
        if found == False:
            print("Такого студента нет")


if __name__ == "__main__":
    main()
