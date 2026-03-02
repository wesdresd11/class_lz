import math
import matplotlib.pyplot as plt


class Octagon: #Импортировали необход. бибилиотеки, создали класс октагон


    def __init__(self, side_length): #конструктор, задали длину, и константы по условию лабы
        self.side_length = side_length
        self.angle = (math.pi * 3) / 4
        self.k = 1 + 2 ** 0.5
    
    def outer(self): #считаем радиус и площадь опис. окруж., школьный формулы, возвращаем их в конце
        outer_circle_radius = ((self.side_length ** 2) / (2 - (2 ** 0.5))) ** 0.5
        outer_circle_sq = math.pi * (outer_circle_radius ** 2)
        return outer_circle_radius, outer_circle_sq
    
    def inner(self): #считаем радиус и площадь впис. окруж., школьный формулы, возвращаем их в конце
        inner_circle_radius = (((self.side_length ** 2) / (2 - (2 ** 0.5))) ** 0.5) * math.cos(math.pi / 8)
        inner_circle_sq = math.pi * (inner_circle_radius ** 2)
        return inner_circle_radius, inner_circle_sq
    
    def oct(self): #считаем площадь, периметр октагона, возвращаем их в конце
        octagon_sq = 2 * self.k * (self.side_length ** 2)
        octagon_perim = 8 * self.side_length
        return octagon_sq, octagon_perim
    
    def picture(self): #отрисовываем графики наших фигур, вводим радиус впис. и опис. окруж-стей 
        R = ((self.side_length ** 2) / (2 - (2 ** 0.5))) ** 0.5
        r = (((self.side_length ** 2) / (2 - (2 ** 0.5))) ** 0.5) * math.cos(math.pi / 8)
        x = []
        y = []

        for i in range(8):                      #для октагона создаем список его точек х и у, а также все углы через цикл for и добавляем их в список точек
            a = i * (math.pi - self.angle)
            x.append(R * math.cos(a))
            y.append(R * math.sin(a))

        x.append(x[0])
        y.append(y[0]) #последняя точки октагона, замыкаем его

        plt.plot(x, y, "black")   #отрисовали октагон, цвет черный, координаты точек из наших массивов х и у

        plt.gca().add_patch(plt.Circle((0, 0), R, fill=False, color="red")) #отрисовали опис. окруж, где R - ее радиус, заливка цвтом выключена, а цвет окруж. - красный

        plt.gca().add_patch(plt.Circle((0, 0), r, fill=False, color="green")) #то же самео, только впис. окруж, где r - радиус впис. окруж, цвет зеленый

        plt.axis("equal") #убираем растягивание круга, а то получился бы овал
        plt.show() #окно рисунка





