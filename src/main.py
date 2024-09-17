
def main():
    print("Write name of detail:")
    detail = input()
    print("Write color:")
    color =  input()
    total_cost = CountPriceOfPainting(detail, color)
    print ("Total cost is " , total_cost)



def CalculateColor(color): 
    colors = {'Белый': 1, 'Синий': 1, 'Желтый': 1.1, 'Красный': 1, 'Перламутровый': 1.2, 'Серый металлик': 1.3}
    return colors[color]

def CalculateDetail(detail):
    details = {'Капот': 1, 'Передняя дверь': 1.2, 'Задняя дверь': 1.1, 'Передний бампер': 1, 'Задний бампер': 1, 'Крыша': 1.1}
    return details[detail]

def CountPriceOfPainting(detail, color): 
    cost_color = CalculateColor(color)
    cost_detail = CalculateDetail(detail)
    return (cost_color+cost_detail)*12000



main()