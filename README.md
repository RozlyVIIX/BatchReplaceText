### 文本替换

1. ReplaceText.sh

   **bash ReplaceText.sh 待处理的文件路径 被替换值 替换值**

   ~~功能鸡肋，只能对文件的单一替换值批量替换。等同于文本编辑器替换功能，请忽略。~~

2. BatchScript.py

   python3 ./BatchScript.py ./fileList.txt ./text.txt

   注：

   * 环境无Python3，请优先安装。
   * 建议将上述三个文件放在同一目录下。

   说明：

   * fileList.txt：每行存放被处理的文件路径。批量处理文件时，请多行写入。
   * text.txt：单数行存放被替换值，双数行存放替换值。批量替换值时，同理适用。
