from iteration_utilities import unique_everseen, duplicates

print("********************* Program  : 2 Methods to Find Duplicate number in List *****************************************\n\n")

def Find_Duplicate_1stmethod(Templist):
    "Method 1 : iteration_utilities module offers the duplicates function, which yields duplicate elements."
    print("\n**************************************************************\n")
    print('\t\t\t\tMethod 1 : ')
    duplicateElements=list(unique_everseen(duplicates(Templist)))
    print("Duplicate Elements in List are ",duplicateElements)
    print("\n**************************************************************\n")
def Find_Duplicate_2ndmethod(Templist):
    "Method 2 : "
    print("\n**************************************************************\n")
    print('\t\t\t\tMethod 2 : ')
    duplicateElements=[]
    for a in Templist:
        if Templist.count(a)>1:
            if a not in duplicateElements:
                duplicateElements.append(a)
    print("Duplicate Elements in List are ",duplicateElements)
    print("\n**************************************************************\n")

list_ = [1,2,3,4,5,6,7,8,9,9,0]
print('List elements are : ', list_ ,end="\n\n")
Find_Duplicate_1stmethod(list_)
Find_Duplicate_2ndmethod(list_)
