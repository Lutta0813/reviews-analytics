#讀取reviews.txt
#放入data清單

data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())

dataCount = 0

for dataNumber in data:
	dataCount += 1
  
print('檔案讀取完了，總共有：', dataCount, '筆資料')

wc = {} # word_count
for d in data:
	words = d.split()
	for w in words:
		if w in wc:
			wc[w] += 1
		else:
			wc[w] = 1
	# break

for word in wc:
	if wc[word] > 100:
		print(word, wc[word])	

print ('總共有' ,len(wc), '個不同的字')

while True:
	word = input('請輸入想查詢的字： ')
	if word == 'q':
		break
	elif word in wc:
		print(word, '總共出現' , wc[word], '次')
	else:
		print('這個字沒有出現過哦。')

print('感謝使用本查詢功能')







































 





# # 篩選留言長度
# new = []
# for d in data:
# 	if len(d) <= 100:
# 		new.append(d)
# print('總共有', len(new), '筆留言長度小於100')


# # 篩選特定用詞
# # good = []
# # for d in data:
# # 	if 'good' in d:
# # 		good.append(d)
# # print('總共有', len(good), '筆留言中提到good')
# # print(good[0])

# # list comprehension

# good = [d for d in data if 'good' in d] # 此行與上面篩選特定用詞（40～43）的程式碼相同。
# print('總共有', len(good), '筆留言中提到good')

# bad = [d for d in data if 'bad' in d]
# print('總共有', len(bad), '筆留言中提到bad')


