import os

def file_filter(filter_name):
    l = []
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        if len(files) > 0:
            print("文件列表：")
            for f in files:
                # print(f)
                if filter_name in f:
                    l.append(f)
    return l

def download_file_rename(directory,src_name_list,dst_name_list):
    for file_index in range(len(src_name_list)):
        os.rename(src_name_list[file_index], dst_name_list[file_index])
        # print(src_name_list[file_index]," ",dst_name_list[file_index])

def file_name_compare(arr):
    for i in range(len(arr)-1):
        if(arr[i]<arr[i+1]):
            print("true len=",len(arr)," ",arr[i]," ",arr[i+1])
        else:
            print("false len=",len(arr)," ",arr[i]," ",arr[i+1])

#数组长度判断
def arr_len(arr):
    arr_len = len(arr)
    if (arr_len <= 0):
        return 0
    else:
        return arr_len - 1

#文件内容读取
def file_read(file_name):
    f = open(file_name,'r+',encoding="UTF-8")
    f_s = f.read()
    f.close()
    return f_s
#解析idm导出文件提取下载文件名称
def idm_ef2_src_file_name_parse(file_name):
    file_name_list = []
    idm_url = file_read(file_name)
    for u in idm_url.split("<"):
        arr = u.split("?e=")[0].split('/')
        if(arr_len(arr)):
            file_name_list.append(arr[arr_len(arr)])
    return file_name_list

def idm_ef2_dst_file_name_parse(file_name):
    file_name_list = []
    idm_url = file_read(file_name)
    for u in idm_url.split("<"):
        arr = u.split("\n>")[0].split('filename: ')
        if(arr_len(arr)):
            file_name_list.append(arr[arr_len(arr)])
    return file_name_list

#获取下载列表中的文件名字
def idm_ef2_file_parse(url_file_dir,file_list,type):
    #os.chdir(url_file_dir)
    lst = []
    for file in file_list:
        if type == "src_name":
            lst.extend(idm_ef2_src_file_name_parse(file))
        elif type == "dst_name":
            lst.extend(idm_ef2_dst_file_name_parse(file))
        else:
            print("error")
    print("len=",len(lst))
    return lst

url_file_dir = os.getcwd()
url_file_list = file_filter(".ef2")

dst_file_dir = os.getcwd()

src_name_list = idm_ef2_file_parse(url_file_dir,url_file_list,"src_name")
dst_name_list = idm_ef2_file_parse(url_file_dir,url_file_list,"dst_name")

# print(src_name_list)
# print(dst_name_list)

download_file_rename(dst_file_dir,src_name_list,dst_name_list)
