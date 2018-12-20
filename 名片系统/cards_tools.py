card_list = []


def print_menu():
    """
    显示功能菜单
    :return:
    """
    print("*" * 100)
    print("欢迎来到名片管理系统\n输入以下对应数字选择对应功能：\n"
          + "1.添加名片\n"
          + "2.显示名片\n"
          + "3.查询名片\n"
          + "0.退出系统")
    print("*" * 100)


def new_card():
    """
    新增名片
    :return:
    """
    print("-" * 100)
    print("新增名片")

    # 1.输入信息
    name_str = input("输入姓名")
    phone_str = input("输入电话")
    qq_str = input("输入QQ")

    # 2.定义名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str}

    # 3.添加到名片列表
    card_list.append(card_dict)

    # 4.输出添加信息
    print(card_list)
    print("%s添加成功" % name_str)


def show_all():
    """
    显示所有名片
    :return:
    """
    print("-" * 100)
    print("显示所有名片")

    # 判断是否有记录
    if len(card_list) == 0:
        print("没有记录")
    else:
        for name in ["姓名", "电话", "QQ"]:
            print(name, end='\t\t')
        print("\n")

        for card_info in card_list:
            print("%s\t\t%s\t\t%s\t\t" % (card_info["name"], card_info["phone"], card_info["qq"]))


def search_card():
    """
    搜索名片
    :return:
    """
    print("-" * 100)
    print("搜索名片")

    # 输入信息
    name = input("输入要查找的姓名")
    for info in ["姓名", "电话", "QQ"]:
        print(info, end='\t\t')

    print("\n")
    for card_info in card_list:
        if card_info["name"] == name:
            print("%s\t\t%s\t\t%s\t\t" % (card_info["name"], card_info["phone"], card_info["qq"]))

            # TODO 修改和删除
            deal_card(card_info)
            break
    else:
        print("没有找到")


def deal_card(card_info):
    """
    查询以后对名片进行处理
    :param card_info: 查询到的名片
    :return:
    """
    print("请选择对名片进行的操作"
          "[1]修改名片 [2]删除名片 [0]返回")
    choose = input()

    if choose == '1':
        card_info["name"] = deal_card_input(card_info["name"], "输入名字")
        card_info["phone"] = deal_card_input(card_info["phone"], "输入电话")
        card_info["qq"] = deal_card_input(card_info["qq"], "输入QQ")
        print("修改成功")
    elif choose == '2':
        card_list.remove(card_info)
        print("删除成功")
    else:
        return


def deal_card_input(card_value, message):
    """
    处理修改的数据，如果为空则不修改
    :param card_value: 要修改的量
    :param message: 提示信息
    :return: 修改的值
    """
    print(message)
    change = input()
    if len(change) == 0:
        return card_value
    else:
        return change
