import cards_tools

while(True):

    cards_tools.print_menu()
    choose = int(input())
    print("你选择的功能是 %d " % choose)

    # TODO 系统功能
    if choose == 0:
        print("欢迎再次使用")
        break
    elif choose in [1,2,3]:
        if choose == 1:
            cards_tools.new_card()
        elif choose == 2:
            cards_tools.show_all()
        else:
            cards_tools.search_card()
    else:
        print("输入有误，请重新输入")
