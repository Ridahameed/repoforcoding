#--------------------------------
# ----------For reversing--------------
# str = ["a", "b", "c", ]
# print(str[::-1])

#------------------------------------
# ---------For checking if the list is sorted or not---------------
# arr = [1,2,3,4,6,7]
# is_sorted = True
# for i in  range(len(arr) -1):
#    if arr[i] > arr[i+1]:
#        is_sorted = False
#        break
# print(is_sorted)
#--------------------------------------
# ----------For counting the even and odd numbers in list-------------
# arr = [1,2,3,4,6,7]
# even = 0
# odd = 0
# for i in arr:
#   if i % 2 == 0:
#     even += 1 
#   else:
#     odd += 1

# print("Count of even is:" , even)
# print("Count of odd numbers is:" ,odd)
#-------------------------------------------------
# --------------For avoiding any duplicates-----------------
# arr = [1,2,2,6,3,4,6,7]
# duplicate = []
# for a in arr:
#   for b in arr:
#     if b not in duplicate:
#       duplicate.append(b)
# print(duplicate)
#-------------------------------------------------
# -------------For counting duplicates-----------------
# arr = [1,2,2,6,3,4,6,7]
# nonduplicates = []
# duplicate =  []
# for a in  arr:
#     if a not in nonduplicates:
#        nonduplicates.append(a)
#     else:
#        duplicate.append(a)
# print(len(duplicate))
#-------------------------------------------------------
# -------------For Avoiding any duplicates-------------------
# arr = {1,2,2,6,3,4,6,7}
# print(arr)
# ------------------------------------------------------
# ------------For printing Duplicates------------------------
# arr = [1,2,2,6,3,4,6,7]
# newlist = []
# for i in arr:
#     if i not in newlist:
#         newlist.append(i)
#     elif i in newlist:
#         print(i)
# ------------------------------------------------------------

