#密碼重試程式
correct_password = 'a123456'
i=1 #嘗試次數
while i <= 3:
	password = input('請輸入密碼: ')
	if password != correct_password:
		print('密碼錯誤! 你還有', 3-i, '次機會')
		i = i + 1
	else:
		print('登入成功!')
		break
