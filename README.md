
# สามารถใช้ api [ได้จากที่นี่](http://165.22.3.172:8000/docs)



api นี้ จะแนะนำตาม Content-based Filtering แล้ว Content-based Filtering คืออะไร ตัวอย่างเช่น 
ถ้าเราชอบหนังแนว fantasy มันก็จะแนะนำหนัง ที่มีแนว fantasy แบบในรูป
![You](https://user-images.githubusercontent.com/98101484/201525513-2af1e7cf-d9b7-47b8-b991-d8e8cb4f4cd6.png =100x20)

สามารถดู source code ได้จาก เรื่องของ การแนะนำอย่างไรได้จาก ไฟล์ rec.py

ใช้ข้อมูลจากไหน
ส่วนข้อมูลที่ใช้ จะเอามาจาก การดึงข้อมูลจาก api tmdb ทั้งหมด 7,278 เรื่อง 
โดยมี การ clean ข้อมูลที่ ออกไปแล้ว ในไฟล์ movie.csv
 
ส่วนการ เอาไปใช้ เป็น api นั้นผมใช้ fast-api ในการทำ เพราะ มี feature พิเศษ ที่สามารถ สร้าง หน้า docs ให้ อัตโนมัติ
แบบนี้ 
![Screenshot (85)](https://user-images.githubusercontent.com/98101484/201657351-ccd1ca55-ed9d-464b-982d-6c01c11177fd.png)
### แต่สามารถรันใน localhost ได้โดยใช้คำสั่งนี่ลงใน terminal

#### ซึ่งคนที่อ่าน git hub นี้ ก็สามารถ เอาไปใช้ได้อย่างง่ายๆโดยการ clone gtihub โดยใช้ python version 3.9.12 version 

## จากนั้นก็ทำตามนี้
สร้าง env
```bash
python3 -m venv 'env_name'
```

activate env
```bash
'env_name'\Scripts\activate
```
install library ต่างๆ
```bash
pip install -r /path/to/requirements.txt
```
รัน server ใน localhost
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
