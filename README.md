api นี้ จะแนะนำตาม Content-based Filtering แล้ว Content-based Filtering คืออะไร ตัวอย่างเช่น 
ถ้าเราชอบหนังแนว fantasy มันก็จะแนะนำหนัง ที่มีแนว fantasy อยู่ด้วย ดังรูป
![IMG_4314](https://user-images.githubusercontent.com/98101484/201359971-6f942d75-f813-47ab-80c2-e0e6ced3f1de.JPG)

สามารถดู source code ได้จาก ไฟล์ rec.py


ใช้ข้อมูลจากไหน
ส่วนข้อมูลที่ใช้ จะเอามาจาก การดึงข้อมูลจาก api tmdb ทั้งหมด 7,278 เรื่อง 
โดยมี การ clean ข้อมูลที่ ออกไปแล้ว
ทำมไถึงใช้ข้อมูลนี้ 
เพราะว่า api tmdb มีข้อมูล พวก รูป โปสเตอร์หนัง คำอธิบาย และ feature อื่นๆ ที่
ที่มีความเหมาะสมให้นำไปดึงข้อมูลใช้ต่อ ในการ ทำเว็บ

 
 deploy เป็น api ยังไง มี หน้าไหนบ้าง
 ใช้ยังไง

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
