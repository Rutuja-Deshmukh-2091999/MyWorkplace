Item_Number = [101,102,103,104]
Item_Name = ['Milk','Cheese','Ghee','Bread']
Price = [42,50,500,40]
Stock = [10,20,15,16]

try:
    item_num = int(input())
    quantity = int(input())
    if item_num not in Item_Number:
        raise ValueError('A very specified bad thing happened')
    if quantity < Stock[Item_Number.index(item_num)]:
        print("{0:.1f} INR".format(Price[Item_Number.index(item_num)]*quantity))
        print(Stock[Item_Number.index(item_num)]-quantity,"LEFT")
    else:
        print("NO STOCK")
        print(Stock[Item_Number.index(item_num)],"LEFT")
except ValueError:
    print("INVALID INPUT")
