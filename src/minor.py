#minor 0.0.1

vardict = {} #创建一个存放变量的字典

def error(name): #用于报错的函数
	if name == "NameError":
		print("NameError")
	elif name == "Error":
		print("Error")

def isvar(var): #检测是否有一个变量
	return vardict.get(var,False) #没有则返回False
	
def run(a):
	count = 0 #设置计数变量为0
	word = a.split() #分割输入的命令
	while word != []: #在列表为空前一直循环
		i = word[count] #提取出当前命令
		count += 1
		n = word[count] #提取下一个命令
		if i == "print": #输出命令：print 内容
			if isvar(n):
				print(vardict[n])
			else:
				print(n)
		elif i == "var": #定义变量命令：var 变量名 = 值
		    if word[count + 1] != "=":
		    	error("Error")
		    count += 2 #变量值位于第二个下两个
		    v = word[count]
		    vardict[n] = v
			
def main(): #主函数
	try: #排除可能的错误
		while True:
			a = input(">>>")
			run(a)
	except IndexError:
		main() #迭代循环

main() #开始运行
