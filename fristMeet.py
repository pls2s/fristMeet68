import random
import time

def main():
    print("🔥 ว่าไงไวรุ่น ITI 🔥")
    print("=" *25)

    name = input("ชื่ออะไรจ๊ะ : ")
    sub = input("สาขาอะไรจ๊ะ : ")

    print(f"\n{name} โหลดอยู่รอแปป" ,end="")
    for i in range(3):
        print("." , end="" ,flush=True)
        time.sleep(0.5)
    print(" ไปกันต่ออออ\n")

def hobbits():
    hobbys = ["คุยกับ ai ยันเช้า","F5 รัวๆ เพื่อแก้ BUG", "กรีดร้องวาลาเจอ ERROR" , "หลับ1ตื่นเพื่อเเก้ BUG"]
    hobby = random.choice(hobbys)
    print("งานอกิเรก 💼 : " + hobby)


def power():
    powers = []
