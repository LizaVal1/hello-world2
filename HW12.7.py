per_cent={'ТКБ':5.6,'СКБ':5.9,'ВТБ':4.28,'СБЕР':4.0}
money=int(input("Введите сумму депозита:"))
a=per_cent.values()
new_a = list(map(float, a))
deposit= [new_a[0]*money*0.01,new_a[1]*money*0.01,new_a[2]*money*0.01,new_a[3]*money*0.01]
deposit_max=max(deposit)
print(deposit,'Максимальная сумма, которую вы можете заработать - ',deposit_max)
