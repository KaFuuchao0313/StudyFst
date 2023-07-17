from tkinter import filedialog
import requests
import base64


def upload_img():
    global filename
    filename=filedialog.askopenfilename()   #通过上传文件的方式获取本地图片的地址
    
    '''任务1：将图片地址赋值给file变量'''
    global photo
    photo=tk.PhotoImage(file=as_the_light_shine.png)
    txt1.image_create('end',image=photo)    #将图片显示在第一个文本框中
    

def words_rec():
    
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=SfAqtEcet9HFZfLAuFp4siVL&client_secret=Ih8gr9i9Q36ZFGrOF6YqG7DHOLDAI2r1'
    response = requests.get(host)
    if response:
        access_token=response.json()['access_token']

    '''任务2:下划线部分写入导入的图片地址'''   
    f=open(as_the_light_shine.png,'rb') 
    img_b64 = base64.b64encode(f.read())
    params = {"image":img_b64,"language_type":"CHN_ENG","detect_direction":"true"}
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    print(response.json())

    '''任务3，提取返回结果中的文本，插入在名为txt2的文本框中'''

        



