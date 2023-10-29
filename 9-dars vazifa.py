# a = "2+3*5-2+9/(2+7/5-123)"
# dc = {}
# for i in a:
#     if not i.digit():
#         try:
#             d[i]+=1
#         except:
#             dc[i]=1
#
# for k,v dc.items:
#     if i






# startTime = list(map(int, input().split()))
# endTime = list(map(int, input().split()))
# q = int(input())
# n=0
# for i in range(len(startTime)):
#     if startTime[i] <=q and endTime[i]>=q:
#         n+=1
# # return n
#
# print(n)





# nums = list(map(int, input().split()))
# ls = []
# n = len(nums)
# for i in range(1, n+1):
#     s=0
#     for j in range(i):
#         s = s+nums[j]
#     ls.append(s)
# # print(ls)
# return ls







# accounts = list(map(int, input().split()))
# ls = []
# n = len(accounts)
# for i in range(n):
#     s=0
#     s = sum(accounts[i])
#     ls.append(s)
# a = max(ls)
# return a







# command = input()
# c = ""
# n = len(command)
# for i in range(n):
#     if command[i]=='(' and command[i+1]==')':
#         c[i]='o'
#         c[i+1]=''
#         i+=1
#         print(1)
#     elif command[i]=='(' or command[i]==')':
#         c[i]=''
#         print(2)
#     else:
#         c[i] = f"{command[i]}"
# print(c)

# command = input()
# n = len(command)
# for i in range(n):
#     if command[i] == '(' and (i + 1) == ')':
#         command.replace(i, 'o')
#         command.replace(i + 1, '')
#     elif i == '(':
#         command.replace(i, '')
# print(command)





# unli = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# s = input()
# n = len(s)
# cnt1=0
# cnt2=0
# for i in range(n):
#     if i<n/2:
#         for j in unli:
#             if s[i]==j:
#                 cnt1+=1
#     elif i>=n/2:
#         for j in unli:
#             if s[i]==j:
#                 cnt2+=1
# if cnt1==cnt2:
#     print("True")
# else:
#     print("False")






nums = list(map(int, input().split()))
ls = []
for i in nums:
    if nums.count(i)==1:
#         ls.append(i)
# return sum(ls)
print(sum(ls))