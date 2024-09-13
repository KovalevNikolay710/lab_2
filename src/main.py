
def main():

    print("Write name:")
    name = input()
    print("Write color:")
    color =  input()



def CountPriceOfPainting(name, color): 
    """return price"""

def CalculateColor(color): 
    colors = {'Белый': 1, 'Синий': 1, 'Желтый': 1.1, 'Красный': 1, 'Перламутровый': 1.2, 'Серый металлик': 1.3}
    return colors[color]

def CalculateDetail(detail):
    """return ratio""" 
    details = {'Капот': 1, 'Передняя дверь': 1.2, 'Задняя дверь': 1.1, 'Передний бампер': 1, 'Задний бампер': 1, 'Крыша': 1.1}
    return details[detail]
