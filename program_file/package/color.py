from colorama import Fore, Back, Style, init
class Color:
    FORE_BLACK   = Fore.BLACK   # 黒 
    FORE_RED     = Fore.RED     # 赤 
    FORE_GREEN   = Fore.GREEN   # 緑 
    FORE_YELLOW  = Fore.YELLOW  # 黄 
    FORE_BLUE    = Fore.BLUE    # 青い 
    FORE_MAGENTA = Fore.MAGENTA # 赤紫色 
    FORE_CYAN    = Fore.CYAN    # シアン 
    FORE_WHITE   = Fore.WHITE   # 白い 
    FORE_RESET   = Fore.RESET   # リセット 

    ##### ライン #####
    BACK_BLACK   = Back.BLACK   # 黒
    BACK_RED     = Back.RED     # 赤
    BACK_GREEN   = Back.GREEN   # 緑
    BACK_YELLOW  = Back.YELLOW  # 黄
    BACK_BLUE    = Back.BLUE    # 青い
    BACK_MAGENTA = Back.MAGENTA # 赤紫色
    BACK_CYAN    = Back.CYAN    # シアン
    BACK_WHITE   = Back.WHITE   # 白い
    BACK_RESET   = Back.RESET   # リセット

    STYLE_DIM       = Style.DIM       # 暗い
    STYLE_NORMAL    = Style.NORMAL    # 正常
    STYLE_BRIGHT    = Style.BRIGHT    # 明るく
    STYLE_RESET_ALL = Style.RESET_ALL # スタイルリセット

class Escape:
    SCREEN_CLEAR    = "\033[2J" # 画面クリア
    RIGHTMOST_CLEAR = "\033[0K" # カーソル位置からその行の右端までをクリア
    LEFTMOST_CLEAR  = "\033[1K" # カーソル位置からその行の左端までをクリア
    CLEAR_ROW       = "\033[2K" # カーソル位置の行をクリア

    MOVING_RIGHT_ONE   = "\033[1C" # カーソルを1行だけ右に移動
    MOVING_RIGHT_TWO   = "\033[2C" # カーソルを2行だけ右に移動
    MOVING_RIGHT_THREE = "\033[3C" # カーソルを3行だけ右に移動
    
    MOVING_LEFT_ONE   = "\033[1D" # カーソルを1行だけ左に移動
    MOVING_LEFT_TWO   = "\033[2D" # カーソルを2行だけ左に移動
    MOVING_LEFT_THREE = "\033[3D" # カーソルを3行だけ左に移動
    
    UNDER_MOVE_ONE   = "\033[1B" # カーソルを1行だけ下に移動
    UNDER_MOVE_TWO   = "\033[2B" # カーソルを2行だけ下に移動
    UNDER_MOVE_THREE = "\033[3B" # カーソルを3行だけ下に移動

    ABOVE_MOVE_ONE   = "\033[1A" # カーソルを1行だけ上に移動
    ABOVE_MOVE_TWO   = "\033[2A" # カーソルを2行だけ上に移動
    ABOVE_MOVE_THREE = "\033[3A" # カーソルを3行だけ上に移動