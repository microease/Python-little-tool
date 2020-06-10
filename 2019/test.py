domains = ['''m.szffmr.com''', '''mm.szffmr.com''', '''m.88833222.com''', '''m.ffyy.cc''', '''wap.mr91.com''',
           '''baidu.mr91.com''']

desktop = "C:\\Users\micro\Desktop\\"
# 在这里输入你想要的文件夹名称
new_dir_name = "202005tmj"
dirs = ["/网站文件/szffmr/wap/zhuanti/", "/网站文件/szffmr/mm/zhuanti/", "/网站文件/www.88833222.com/wap/zhuanti/",
        "/网站文件/www.ffyy.cc/wap/zhuanti/", "/网站文件/wap.mr91.com/zhuanti/", "/网站文件/baidu.mr91.com/zhuanti/"]
new_dirs = [desktop + i + new_dir_name for i in dirs]
print(new_dirs)
