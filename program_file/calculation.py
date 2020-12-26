from package import *


menu_list = ["イージーモード (3~6 問)", "ノーマルモード (5~15 問)", "ハードモード (10~30 問)", "終了"]
mode_one_description = ["3~6問の問題が出題されます", "1~10桁のランダムな問題", "小数第二位以上になる場合", "小数点第二まで書いてください"]
mode_two_description = ["5~15問の問題が出題されます", "1~100桁のランダムな問題", "小数第二位以上になる場合", "小数点第二まで書いてください"]
mode_three_description = ["10~30問の問題が出題されます", "1~10000桁のランダムな問題", "演算子が複数出ます", "小数第二位以上になる場合", "小数点第二まで書いてください"]
count = 0
while True:
    print("──────────────┤メニュー├───")
    for number, name in enumerate(menu_list, 1):
        print(f'{number}：{name}')
    print("───────────────────────────")
    mode = IntError().mode_int_Error()
    # print(mode)
    if mode == 1:
        print(menu_list[0])
        Animation().anim(mode_one_description) # print("モードの説明")
        input("Enterを押すとカウントスタート")
        Animation().start_loading()
        print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
        print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}')
        Operator().random_problem(random.randint(3, 6), Writing.EASY_MODE)
        count += 1
    elif mode == 2:
        print(menu_list[1])
        Animation().anim(mode_two_description)
        input("Enterを押すとカウントスタート")
        Animation().start_loading()
        print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
        print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}')
        Operator().random_problem(random.randint(5, 15), Writing.NORMAL_MODE)
        count += 1
    elif mode == 3:
        print(menu_list[2])
        Animation().anim(mode_three_description)
        input("Enterを押すとスタート")
        Animation().start_loading()
        print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
        print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}')
        Operator().random_problem(random.randint(10, 30), Writing.HARD_MODE)
        count += 1
    elif mode == 4:
        if count < 1:
            Animation().end_loading()
            break
        else:
            print(f"txtファイルとcsvファイルが\n{os.getcwd()}\\{Writing.NEW_FILE_NAME}\nに作成されました")
            Animation().end_loading()
            break

    y_n = IntError().end()
    if y_n == "y":
        print(f"txtファイルとcsvファイルが\n{os.getcwd()}\\{Writing.NEW_FILE_NAME}\nに作成されました")
        Animation().end_loading()
        break
    elif y_n == "n":
        for i in range(4):
            print("画面をクリア中", "." * i)
            time.sleep(1)
            print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
            print(f'{Escape.ABOVE_MOVE_TWO}')
        print(f'{Escape.SCREEN_CLEAR}')
        continue