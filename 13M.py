tickets_number=int(input('Введите количество билетов:'))
i=0
cost=0
try:
    for i in range(tickets_number):
        i+=1
        age=int(input('Введите возраст поситителя:'))
        if age<18:
         cost+=0
         print('Билет бесплатный',',','Общая сумма:',cost )
        elif 18<=age<=25:
         cost += 990
         print('Билет стоит 990',',','Общая сумма:', cost)
        elif 25<age:
         cost += 1390
         print('Билет стоит 1390',',','Общая сумма:', cost )
except ValueError :
                print('Введите целое число возраста')
if tickets_number>3:
 cost=0.9*cost
 print('Общая сумма заказа, с учетом скидки 10% - ',cost,',','Количество билетов в заказе:', tickets_number )
else:
        tickets_number <=3
print('Общая сумма заказа:',cost,',','Количество билетов в заказе:', tickets_number)








