from tkinter import filedialog
import requests
import base64


def upload_img():
    global filename
    filename=filedialog.askopenfilename()   #通过上传文件的方式获取本地图片的地址
    
    '''任务1：将图片地址赋值给file变量'''
    global photo
    photo=tk.PhotoImage(file=filename)
    txt1.image_create('end',image=photo)    #将图片显示在第一个文本框中
    

def words_rec():
    
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=SfAqtEcet9HFZfLAuFp4siVL&client_secret=Ih8gr9i9Q36ZFGrOF6YqG7DHOLDAI2r1'
    response = requests.get(host)
    if response:
        access_token=response.json()['access_token']

    '''任务2:下划线部分写入导入的图片地址'''   
    f=open(filename,'rb') 
    img_b64 = base64.b64encode(f.read())
    params = {"image":img_b64,"language_type":"CHN_ENG","detect_direction":"true"}
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    print(response.json())

    word=''

    for i in response.json()['words_result']:
         word=word+i['words']
    txt2.insert('insert',word)

import tkinter as tk

root=tk.Tk()

root.title("analysis")
root.geometry('600x700')

bt=tk.Button(root,text='update',command=upload_img)
bt.pack()
txt1=tk.Text(root)
txt1.pack()

bt2=tk.Button(root,text='now!',command=words_rec)
bt2.pack()
txt2=tk.Text(root)
txt2.pack()

root.mainloop()

