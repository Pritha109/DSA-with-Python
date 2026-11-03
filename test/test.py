# def first_occurence(nums,target):
#     first_occurence = -1
#     low = 0
#     high = len(nums) - 1
#     while low <= high:
#         mid = (low + high) // 2      
#         if nums[mid] >= target:
#             first_occurence = mid
            
#             high = mid - 1
#         else: 
#             low = mid + 1
    

    
#     if first_occurence == -1 or nums[first_occurence] != target:
#         return 0
#     return first_occurence       
            
# def  last_occurence(nums,target): 
#     last_occurence = -1
#     low = 0
#     high = len(nums) - 1
#     while low <= high:
#         mid = (low + high) // 2    
#         if nums[mid] > target:
#             last_occurence = mid 
#             high = mid - 1 
            
#         else:
#             low = mid + 1  
#     if last_occurence == -1 or nums[last_occurence-1] != target:
#         return -1        
#     return last_occurence-1  
          

# nums = [1,2,3,3,3,3,5,6,8,9,9,10]
# target = 13
# result =last_occurence(nums,target)-first_occurence(nums,target)+1    #No of occurence of a number in a list
# print(result)  

      