def calculate_paint_needed(length, width, height, paint, window_door):
    wall_area = 2 * height * (length + width)

    effective_wall_area = wall_area * (1 - window_door / 100)

    paint_needed = effective_wall_area * paint

    return paint_needed, effective_wall_area

def calculate_cost(paint_needed, paint_price_per_liter):
    return paint_needed * paint_price_per_liter

length = float(input('Введите длину комнаты (в метрах): '))
width = float(input('Введите ширину комнаты (в метрах): '))
height = float(input('Введите высоту комнаты (в метрах): '))
paint = float(input('Сколько литров краски требуется на 1 м²: '))
window_door = float(input('Процент площади стен, занимаемой окнами и дверями: '))
paint_price_per_liter = float(input('Цена за литр краски (в рублях): '))

paint_needed, effective_wall_area = calculate_paint_needed(length, width, height, paint, window_door)
total_cost = calculate_cost(paint_needed, paint_price_per_liter)

print('')
print('Общая площадь стен:', effective_wall_area, 'м²')
print('Необходимое количество краски:', paint_needed, 'литров')
print('Общая стоимость краски:', total_cost, 'рублей')