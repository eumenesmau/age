driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('請輸入  有/沒有 ')
	raise SystemExit
age = input('請問你現在幾歲呢?')
age = int(age)
if driving == '有':
	if age >= 18:
		print ('你通過測驗了!')
	else:
		print('奇怪，那你怎麼會開過車呢?')
elif driving == '沒有':
	if age >= 18:
		print('可以去考駕照了喔!')
	else:
		print('再等個幾年吧!')

