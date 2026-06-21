#モジュールについて
#pythonのプログラムが書かれているファイルで,別のpythonスクリプトから利用されることを想定したファイル.
#一つのファイルで管理しきれないコードの場合に主に用いる。

#モジュールの使い方
from my_module import print_module
print("script開始")
print_module()
print("script終了")

#複数モジュールの使用
from my_module import print_module,add_numbers   #[,]で区切ることによって複数モジュールを1処理で利用できるようになる。
print("script開始")
print_module()
x=add_numbers(1,2)
print("script 終了")

#名称省略
from my_module import print_module as pm  #as~でモジュール名の省略を行える
print("script 開始")
pm()
print("script 終了")

#補足：フォルダをまたがってモジュールを呼び出したい場合、
# from サブディレクトリ名.モジュール名 import ~でOK！