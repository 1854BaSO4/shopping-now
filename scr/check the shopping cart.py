products = [
    {"名称": "冰箱", "价格": 2999, "购买人数": 100},
    {"名称": "洗衣机", "价格": 1999, "购买人数": 50},
    {"名称": "电视机", "价格": 3999, "购买人数": 200},
    {"名称": "空调", "价格": 3499, "购买人数": 75},
    {"名称": "微波炉", "价格": 499, "购买人数": 150},
    {"名称": "电饭煲", "价格": 299, "购买人数": 120},
    {"名称": "电磁炉", "价格": 199, "购买人数": 30},
    {"名称": "吸尘器", "价格": 599, "购买人数": 90},
    {"名称": "烤箱", "价格": 999, "购买人数": 60},
    {"名称": "榨汁机", "价格": 199, "购买人数": 80}
]

cart = []

def show_cart():
    if len(cart) == 0:
        print("购物车中暂无商品")
    else:
        print("您的购物车中的商品有：")
        for index, item in enumerate(cart):
            print(f"{index+1}. 商品名称: {item['名称']}, 价格: ￥{item['价格']}, 购买人数: {item['购买人数']}人")

def add_to_cart(product_name):
    for product in products:
        if product["名称"] == product_name:
            cart.append(product)
            print(f"{product_name} 已成功添加到购物车！")
            return
    print("未找到该商品信息，请重新输入。")

def remove_from_cart(index):
    if index < 1 or index > len(cart):
        print("无效的索引")
    else:
        removed_product = cart.pop(index - 1)
        print(f"{removed_product['名称']} 已从购物车中移除")

while True:
    print("\\n1. 查看购物车")
    print("2. 添加商品到购物车")
    print("3. 从购物车中移除商品")
    print("4. 确认购买")
    print("5. 退出")

    choice = input("请选择操作：")

    if choice == "1":
        show_cart()
    elif choice == "2":
        product_name = input("请输入要添加到购物车的商品名称：")
        add_to_cart(product_name)
    elif choice == "3":
        show_cart()
        index = int(input("请输入要移除的商品索引："))
        remove_from_cart(index)
    elif choice == "4":
        show_cart()
        confirm = input("是否确认购买？(确认请输入‘是’): ")
        if confirm == "是":
            print("购买成功！")
            break
    elif choice == "5":
        break
    else:
        print("无效的操作，请重新选择")
