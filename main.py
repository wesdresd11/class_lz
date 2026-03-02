from figure import Octagon #импортировали класс


def main():
    l = int(input("Введите длину стороны:")) #задали сторону октагона
    octagon = Octagon(l)
    outer = octagon.outer() #присвоили переменным соответствующие значения, далее вывели их через print
    inner = octagon.inner()
    octag = octagon.oct()
    print(f"Внешний радиус  и площадь описанной окружности соотв.: {outer}. \nВнутренний радиус и площадь вписанной окружности соотв.:{inner} \nПлощадь октагона и периметр соотв.: {octag}")
    octagon.picture() #график

if __name__ == "__main__":
    main()