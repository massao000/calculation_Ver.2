import os
import random
import time
import csv
import datetime
from colorama import init
from package.color import Color, Escape
init()

class Writing:
    EASY_MODE        = "イージーモード"
    NORMAL_MODE      = "ノーマルモード"
    HARD_MODE        = "ハードモード"
    CORRECT_ANSWER   = "正解"
    INCORRECT_ANSWER = "不正解"
    NOW_DAY          = datetime.date.today()
    NEW_FILE_NAME    = "record_file"
    TOKYO_TZ         = datetime.timezone(datetime.timedelta(hours=9))
    NOW              = datetime.datetime.now(TOKYO_TZ)
    CURRENT_TIME     = (f'{str(NOW.hour).zfill(2)}:{str(NOW.minute).zfill(2)}:{str(NOW.second).zfill(2)}')

    def __init__(self, level_display, issue, answer, problem, time_attack, correct_answer_rate, fraction):
        self.level_display = level_display # 難易度
        self.issue_list = issue # 解答の問題
        self.correct_incorrect_list = answer # 成か不か
        self.problem_number = problem # 問題数
        self.time_attack = time_attack # タイム
        self.correct_answer_rate = correct_answer_rate # 正答率
        self.fraction_number = fraction

    def show(self):
        max = 0
        for padding_number in self.issue_list:
            if max < len(padding_number):
                max = len(padding_number)
        print("──────────────┤結果表示├──")
        print(f'{Writing.NOW_DAY} {self.level_display}')
        for number, (issue, solution) in enumerate(zip(self.issue_list, self.correct_incorrect_list), 1):
            if solution == Writing.CORRECT_ANSWER: # 正解
                print(f'{"{0:02d}".format(number)}: {issue.ljust(max, " ")} {Color.FORE_BLUE}{Color.STYLE_BRIGHT}{solution}{Color.STYLE_RESET_ALL}{Color.FORE_RESET}')
            elif solution == Writing.INCORRECT_ANSWER: # 不正解
                print(f'{"{0:02d}".format(number)}: {issue.ljust(max, " ")} {Color.FORE_RED}{Color.STYLE_BRIGHT}{solution}{Color.STYLE_RESET_ALL}{Color.FORE_RESET}')
        print(f'問題数: {self.problem_number}\nタイム: {self.time_attack}\n正答率: {self.fraction_number} {self.correct_answer_rate}%')
        print("─────────────────────────")

class Operator:
    def __init__(self):
        self.problem_list = [] # 出題問題
        self.answer_list = [] # 不か成か
        self.csv_data = [] # csv用list

    def random_problem(self, easy, level):
        self.level = level
        self.rondom_list1 = []
        self.rondom_list2 = []
        self.rondom_list3 = []
        self.csv_data.append(self.level)
        if self.level == Writing.EASY_MODE:
            self.random_problem_number = easy
            for k in range(self.random_problem_number):
                first = random.randint(1,10)
                second = random.randint(1,10)
                self.rondom_list1.append(first)
                self.rondom_list2.append(second)
            self.operation()
        elif self.level == Writing.NORMAL_MODE:
            self.random_problem_number = easy
            for k in range(self.random_problem_number):
                first = random.randint(1,100)
                second = random.randint(1,100)
                self.rondom_list1.append(first)
                self.rondom_list2.append(second)
            self.operation()
        elif self.level == Writing.HARD_MODE:
            self.random_problem_number = easy
            for k in range(self.random_problem_number):
                first = random.randint(1,10000)
                second = random.randint(1,10000)
                third = random.randint(1,10000)
                self.rondom_list1.append(first)
                self.rondom_list2.append(second)
                self.rondom_list3.append(third)
            self.operation_hard()

    def operation(self):
        self.start_time = time.time()
        self.correct_answer_rate_count_list = [] # 正答率

        for number, (left_number, right_number) in enumerate(zip(self.rondom_list1, self.rondom_list2), 1):
            self.number = number
            self.left_number = left_number
            self.right_number = right_number
            # print(f'デバック（問題）{i} {n}', end=" ")
            ran = random.randrange(4)
            if ran == 1:
                self.division_operator()
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')
            elif ran == 2:
                self.multiplication_operator()
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')
            elif ran == 3:
                self.subtraction_operator()
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')
            else:
                self.addition_operator()
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')
        self.end_time = time.time()
        self.end_time_show()

    def operation_hard(self):
        self.start_time = time.time()
        self.correct_answer_rate_count_list = [] # 正答率

        for number, (left_number, center_number, right_number) in enumerate(zip(self.rondom_list1, self.rondom_list2, self.rondom_list3), 1):
            self.number = number
            self.left_number = left_number
            self.center_number = center_number
            self.right_number = right_number
            ran = random.randrange(4)
            if ran == 1:
                self.division_operator_hard()
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')
            elif ran == 2:
                self.multiplication_operator_hard()
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')
            elif ran == 3:
                self.subtraction_operator_hard()
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')
            else:
                self.addition_operator_hard()
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')
        self.end_time = time.time()
        self.end_time_show()

    def end_time_show(self):
        self.aggregate_time = self.end_time - self.start_time - self.random_problem_number
        # end_ti = self.end_time - self.start_time
        elapsed_minute = round(self.aggregate_time % 3600) // 60
        elapsed_second = round(self.aggregate_time % 3600 % 60, 2)
        self.time_attack = (f'{str(elapsed_minute).zfill(2)}:{str(elapsed_second).zfill(5)}') # ディレイ分は引かれている
        self.correct_answer_total = sum(self.correct_answer_rate_count_list)
        self.correct_answer_count = round(self.correct_answer_total / len(self.correct_answer_rate_count_list) * 100, 1)
        self.fraction = (f'{self.correct_answer_total}/{self.random_problem_number}')
        # print(f'デバック{self.correct_answer_total}/{self.random_problem_number}') # 解答/答え
        for i in range(4):
            print("結果を表示します", "." * i)
            time.sleep(0.5)
            print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
            print(f'{Escape.ABOVE_MOVE_TWO}')
        print(Escape.SCREEN_CLEAR)
        Writing(self.level, self.problem_list, self.answer_list, self.random_problem_number, self.time_attack, self.correct_answer_count, self.fraction).show()
        self.text_file()
        self.csv_data.append(self.time_attack)
        self.csv_data.append(self.correct_answer_count)
        # self.csv_data.append()
        self.csv_file()

    def text_file(self):
        txt = "text.txt"
        app_exists_path = os.getcwd()
        max = 0
        for padding_number in self.problem_list:
            if max < len(padding_number):
                max = len(padding_number)
        if os.path.exists(f'{app_exists_path}\\{Writing.NEW_FILE_NAME}\\{txt}'):
            with open(f'{app_exists_path}\\{Writing.NEW_FILE_NAME}\\{txt}', 'a', encoding='UTF-8')as f:
                f.write(f'\n日付：{Writing.NOW_DAY} {Writing.CURRENT_TIME}\nモード：{self.level}')
                for i, (problem_writing, correct_incorrect) in enumerate(zip(self.problem_list, self.answer_list), 1):
                    f.write(f'\n{"{0:02d}".format(i)}：{problem_writing.ljust(max, " ")} {correct_incorrect}')
                f.write(f'\n問題数：{self.random_problem_number}\nタイム：{self.time_attack}\n正答率：{self.fraction} {self.correct_answer_count}%\n──────────────────────')
        else:
            os.mkdir(f'{app_exists_path}\\{Writing.NEW_FILE_NAME}')
            with open(f'{app_exists_path}\\{Writing.NEW_FILE_NAME}\\{txt}', 'w', encoding='UTF-8')as f:
                f.write(f'日付：{Writing.NOW_DAY} {Writing.CURRENT_TIME}\nモード：{self.level}')
                for i, (problem_writing, correct_incorrect) in enumerate(zip(self.problem_list, self.answer_list), 1):
                    f.write(f'\n{"{0:02d}".format(i)}：{problem_writing.ljust(max, " ")} {correct_incorrect}')
                f.write(f'\n問題数：{self.random_problem_number}\nタイム：{self.time_attack}\n正答率：{self.fraction} {self.correct_answer_count}%\n──────────────────────')

    def csv_file(self):
        csv_file_name = "data.csv"
        app_exists_path = os.getcwd()
        if os.path.exists(f'{app_exists_path}\\{Writing.NEW_FILE_NAME}\\{csv_file_name}'):
            with open(f'{app_exists_path}\\{Writing.NEW_FILE_NAME}\\{csv_file_name}', 'a', encoding='UTF-8')as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(self.csv_data)
        else:
            with open(f'{app_exists_path}\\{Writing.NEW_FILE_NAME}\\{csv_file_name}', 'w', encoding='UTF-8')as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(self.csv_data)

        

    def division_operator(self):
        self.operation_answer = self.left_number / self.right_number
        self.operation_answer = round(self.operation_answer, 2) 
        if isinstance(self.operation_answer, float) == True:
            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} ÷ {self.right_number} = ')
            self.answer = IntError().operation_float_Error(self.issue, self.now_number_prodlem)
        self.answer_data()

    def multiplication_operator(self):
        self.operation_answer = self.left_number * self.right_number
        self.now_number_prodlem = (f'{self.number}問目')
        self.issue = (f'{self.left_number} x {self.right_number} = ')
        self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        self.answer_data()

    def subtraction_operator(self):
        self.operation_answer = self.left_number - self.right_number
        self.now_number_prodlem = (f'{self.number}問目')
        self.issue = (f'{self.left_number} - {self.right_number} = ')
        self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        self.answer_data()

    def addition_operator(self):
        self.operation_answer = self.left_number + self.right_number
        self.now_number_prodlem = (f'{self.number}問目')
        self.issue = (f'{self.left_number} + {self.right_number} = ')
        self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        self.answer_data()

    def division_operator_hard(self):
        rand = random.randrange(4)
        if rand == 1:
            self.operation_answer = self.left_number / self.center_number + self.right_number
            self.operation_answer = round(self.operation_answer, 2)
            if isinstance(self.operation_answer, float) == True:
                self.now_number_prodlem = (f'{self.number}問目')
                self.issue = (f'{self.left_number} ÷ {self.center_number} + {self.right_number} = ')
                self.answer = IntError().operation_float_Error(self.issue, self.now_number_prodlem)
        elif rand == 2:
            self.operation_answer = self.left_number / self.center_number - self.right_number
            self.operation_answer = round(self.operation_answer, 2)
            if isinstance(self.operation_answer, float) == True:
                self.now_number_prodlem = (f'{self.number}問目')
                self.issue = (f'{self.left_number} ÷ {self.center_number} - {self.right_number} = ')
                self.answer = IntError().operation_float_Error(self.issue, self.now_number_prodlem)
        elif rand == 3:
            self.operation_answer = self.left_number / self.center_number * self.right_number
            self.operation_answer = round(self.operation_answer, 2)
            if isinstance(self.operation_answer, float) == True:
                self.now_number_prodlem = (f'{self.number}問目')
                self.issue = (f'{self.left_number} ÷ {self.center_number} x {self.right_number} = ')
                self.answer = IntError().operation_float_Error(self.issue, self.now_number_prodlem)
        else:
            self.operation_answer = self.left_number / self.center_number / self.right_number
            self.operation_answer = round(self.operation_answer, 2)
            if isinstance(self.operation_answer, float) == True:
                self.now_number_prodlem = (f'{self.number}問目')
                self.issue = (f'{self.left_number} ÷ {self.center_number} ÷ {self.right_number} = ')
                self.answer = IntError().operation_float_Error(self.issue, self.now_number_prodlem)
        self.answer_data()

    def multiplication_operator_hard(self):
        rand = random.randrange(4)
        if rand == 1:
            self.operation_answer = self.left_number * self.center_number + self.right_number

            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} x {self.center_number} + {self.right_number} = ')
            self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        elif rand == 2:
            self.operation_answer = self.left_number * self.center_number - self.right_number
            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} x {self.center_number} - {self.right_number} = ')
            self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        elif rand == 3:
            self.operation_answer = self.left_number * self.center_number / self.right_number
            self.operation_answer = round(self.operation_answer, 2)
            if isinstance(self.operation_answer, float) == True:
                self.now_number_prodlem = (f'{self.number}問目')
                self.issue = (f'{self.left_number} x {self.center_number} ÷ {self.right_number} = ')
                self.answer = IntError().operation_float_Error(self.issue, self.now_number_prodlem)
        else:
            self.operation_answer = self.left_number * self.center_number * self.right_number
            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} x {self.center_number} ÷ {self.right_number} = ')
            self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        self.answer_data()

    def subtraction_operator_hard(self):
        rand = random.randrange(4)
        if rand == 1:
            self.operation_answer = self.left_number - self.center_number + self.right_number
            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} - {self.center_number} + {self.right_number} = ')
            self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        elif rand == 2:
            self.operation_answer = self.left_number - self.center_number * self.right_number
            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} - {self.center_number} x {self.right_number} = ')
            self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        elif rand == 3:
            self.operation_answer = self.left_number - self.center_number / self.right_number
            self.operation_answer = round(self.operation_answer, 2)
            if isinstance(self.operation_answer, float) == True:
                self.now_number_prodlem = (f'{self.number}問目')
                self.issue = (f'{self.left_number} - {self.center_number} ÷ {self.right_number} = ')
                self.answer = IntError().operation_float_Error(self.issue, self.now_number_prodlem)
        else:
            self.operation_answer = self.left_number - self.center_number - self.right_number
            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} - {self.center_number} - {self.right_number} = ')
            self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        self.answer_data()

    def addition_operator_hard(self):
        rand = random.randrange(4)
        if rand == 1:
            self.operation_answer = self.left_number + self.center_number - self.right_number
            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} + {self.center_number} - {self.right_number} = ')
            self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        elif rand == 2:
            self.operation_answer = self.left_number + self.center_number * self.right_number
            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} + {self.center_number} x {self.right_number} = ')
            self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        elif rand == 3:
            self.operation_answer = self.left_number + self.center_number / self.right_number
            self.operation_answer = round(self.operation_answer, 2)
            if isinstance(self.operation_answer, float) == True:
                self.now_number_prodlem = (f'{self.number}問目')
                self.issue = (f'{self.left_number} + {self.center_number} ÷ {self.right_number} = ')
                self.answer = IntError().operation_float_Error(self.issue, self.now_number_prodlem)
        else:
            self.operation_answer = self.left_number + self.center_number + self.right_number
            self.now_number_prodlem = (f'{self.number}問目')
            self.issue = (f'{self.left_number} + {self.center_number} + {self.right_number} = ')
            self.answer = IntError().operation_int_Error(self.issue, self.now_number_prodlem)
        self.answer_data()

    def answer_data(self):
        if self.answer == self.operation_answer:
            print(f'{Color.FORE_BLUE}{Color.STYLE_BRIGHT}{Writing.CORRECT_ANSWER}{Color.FORE_RESET}{Color.STYLE_RESET_ALL}')
            you_answer = (f'{self.issue}{str(self.answer)}')
            correct_ncorrect = (f'{Writing.CORRECT_ANSWER}')
            self.problem_list.append(you_answer)
            self.answer_list.append(correct_ncorrect)
            self.csv_data.append(you_answer)
            self.csv_data.append(correct_ncorrect)
            self.correct_answer_rate_count_list.append(1)
            time.sleep(1)
        else:
            print(f'{Color.FORE_RED}{Color.STYLE_BRIGHT}{Writing.INCORRECT_ANSWER}{Color.FORE_RESET}{Color.STYLE_RESET_ALL} 答え {self.operation_answer}')
            you_answer = (f'{self.issue}{str(self.answer)}')
            correct_ncorrect = (f'{Writing.INCORRECT_ANSWER}')
            self.problem_list.append(you_answer)
            self.answer_list.append(correct_ncorrect)
            self.csv_data.append(you_answer)
            self.csv_data.append(correct_ncorrect)
            self.correct_answer_rate_count_list.append(0)
            time.sleep(1)


##### 数値か判断 #####
class IntError(Exception):
    pass

    def mode_int_Error(self):
        while True:
            try:
                inp = input("モードの選択：")
                if inp == "":
                    raise IntError()
                if int(inp) >= 5:
                    raise IntError()
                if int(inp) == 0:
                    raise IntError()
                return_inp = int(inp)
                return return_inp
            except:
                print(f"{Color.FORE_RED}{Color.STYLE_BRIGHT}メニューにない数字もしくは文字が入っています{Color.FORE_RESET}{Color.STYLE_RESET_ALL}")
                time.sleep(1)
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')
    
    def operation_int_Error(self, input_waiting, display_problem):
        while True:
            try:
                inp = int(input(f'{display_problem} {input_waiting}'))
                if inp == "":
                    raise IntError()
                if isinstance(inp, str) == True:
                    raise IntError()
                you_entry = int(inp)
                return you_entry
            except:
                print(f"{Color.FORE_RED}{Color.STYLE_BRIGHT}数字以外が入ってます{Color.FORE_RESET}{Color.STYLE_RESET_ALL}")
                time.sleep(1)
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')

    def operation_float_Error(self, input_waiting, display_problem):
        while True:
            try:
                inp = float(input(f'{display_problem} {input_waiting}'))
                if inp == "":
                    raise IntError()
                if isinstance(inp, str) == True:
                    raise IntError()
                you_entry = float(inp)
                return you_entry
            except:
                print(f"{Color.FORE_RED}{Color.STYLE_BRIGHT}数字以外が入ってます{Color.FORE_RESET}{Color.STYLE_RESET_ALL}")
                time.sleep(1)
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')

    def end(self):
        while True:
            inp = input("終了しますか？(y/n)：")
            if inp == "y":
                return inp
            elif inp == "n":
                return inp
            else:
                print(f"{Color.FORE_RED}{Color.STYLE_BRIGHT}半角英数字で入力してください{Color.FORE_RESET}{Color.STYLE_RESET_ALL}")
                time.sleep(1)
                print(f'{Escape.ABOVE_MOVE_ONE}{Escape.CLEAR_ROW}')
                print(f'{Escape.ABOVE_MOVE_TWO}{Escape.CLEAR_ROW}{Escape.ABOVE_MOVE_ONE}')

class Animation: # ここを改行できるようにする
    def anim(self, list_data):
        for list_string in list_data:
            one_character = []
            stairs_list = [] 
            for moji in list_string:
                one_character += moji
                comma_character = ",".join(one_character)
                string = comma_character.replace(",", '')
                stairs_list.append(string)
            for stairs in stairs_list:
                print(f"{stairs}", end="")
                time.sleep(0.03)
                print("\r", end="")
            print()
    
    def start_loading(self):
            # print(f"実行されました")
        for i in range(3, -1, -1):
            print(f'\r開始まで {i}', end='')
            time.sleep(0.85)
        print()

    def end_loading(self):
            # print(f"実行されました")
        for i in range(5, -1, -1):
            print(f'\r終了まで {i}', end='')
            time.sleep(0.85)
        print()
