driving = input('請問你有沒有開過車?:')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('請問你的年齡:')
if driving == '有':
	if int(age) >= 18:
		print('你通過測驗了')
	else:
		print('奇怪你怎麼有開過車')
elif driving == '沒有':
	if int(age) >=18:
		print('你可以考駕照了，怎麼還不去考')
	else:
		print('再過幾年你就可以考駕照了')