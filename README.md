#Requiments
open3d >= 0.9.0<br> 
argparse 

#Command
python ver0.py --init_pos 450 50 0 300 --amount 4 --data_path "YOUR_PATH"

#目录说明
读取点云的目录下有FuXiao_1--4，4个文件夹

#操作说明
输入Command后弹出open3d窗口，可用鼠标等默认操作进行缩放、旋转、平移，按h命令行弹出键盘说明（默认）<br>
利用下述按键的进行帧数切换时，命令行均会弹出对应的说明，和正在显示的文件路径信息

#颜色说明
红： FuXiao1<br>
黄： FuXiao2<br>
绿： FuXiao3<br>
蓝： FuXiao4<br>

#按键说明
.   4个目录下均前进100帧<br>
,  	4个目录下均后退100帧<br>
p  	命令行输入任意目录+帧数，空格隔开，例：2 200，即FuXiao2的第200帧<br>
    注意：命令行输入时，窗口会卡死，建议不要进行别的操作，否则容易崩溃<br>
o  	退出程序<br>
a  	激活要操作的路径，输入1，2，3，4中的一个数字x，代表后续的w e s d操作针对FuXiao_x进行<br>
w	  选定目录后退10帧<br>
e	  选定目录前进10帧<br>
s	  选定目录后退1帧<br>
d	  选定目录前进1帧<br>
i   融合本帧和后帧内容显示
