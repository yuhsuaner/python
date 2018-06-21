# # 數字
# 3.5 
# print(3.5)
# # print(資料)
# print("Hello Python")
# #字串
# print("任意的文字")

# #布林值
# True
# False
# print(True)

# #變數
# input=3
# print(input) #建立新的變數，把資料3放進去
# input="Irene"
# print(input) #變數可以被覆蓋

# #運算符號
# data=5//2 #//兩個斜線叫 整數除法
# print(data)
# data=6**3 #6的3次方
# print(data)
# print("Hello"+"World")
# input(提示文字)以【字串的型態】取得使用者輸入
# n1=input("Enter a Number:")
# n2=input("Enter a Number:")
# n1=int(n1) #int(資料) 將資料轉換成整數型態
# n2=int(n2)
# result=n1+n2
# print(result)
#讓使用者輸入 5 個數字 ， 1. 算總和 2. 哪個數字最大
#使用 List 列表處理 by線上影片用1.5倍快轉

l = []
for i in range(5):
    n = (int(input("Enter a Number:")))
    l.append(n)
print(sum(l))
print(max(l))

