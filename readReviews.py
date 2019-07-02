#讀取reviews.txt
#放入data清單

data = []

count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 == 0: # %符號用來求餘數，這邊的意思是每當count除以10000時餘數等於0就進入if，數學上的說法就是「如果count是10000的倍數」我就印一遍
			print(len(data))

# print(len(data)) #顯示reviews內有一百萬筆資料
print(data[0])