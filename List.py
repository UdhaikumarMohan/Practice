nums = [12, 30, 45, 17, 17]
nums.remove(17)
nums
if 12 not in nums:
    print("Yes")

else:
    print("No")
nums.insert(0,77)
nums.pop()
nums
del nums[2:]
nums
nums.extend([29, 12, 14, 36])

min(nums)
max(nums)
sum(nums)
nums.sort()
nums

List = [["Udhai", 25], ["Pavithra", 30], ["Iniyan", 20], ["Rini", 90], ["Akshaya", 70]]
List.sort()
List

List[1][1]

Mark_Sheet = []
for N in range(int(input())):
    name = input()
    score = float(input())
        
    Mark_Sheet.append([name, score])
        
print(name)
