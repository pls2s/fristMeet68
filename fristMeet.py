import random
import time

def main():
    print("   🔥 ว่าไงไวรุ่น ITI 🔥")
    print("=" *25)
    
    print("📱 พี่ชื่อ พอร์ช CS ปี3")
    print("📲 IG: p.p_04 | GitHub: pls2s")
    print("😴 ความสามารถพิเศษ: นอนได้ 24/7")
    print("=" * 25 +"\n")

    print("ตาน้องบ้างละ")
    name = input("ชื่ออะไรจ๊ะ : ")
    sub = input("สาขาอะไรจ๊ะ : ")

    print(f"\n{name} โหลดอยู่รอแปป" ,end="")
    for i in range(3):
        print("." , end="" ,flush=True)
        time.sleep(0.5)
    print(" \nไปกันต่ออออ\n")

    print(f"""
╔══════════════════════╗
  สวัสดี {name}! 👋         
  อ่อสาขา {sub} นี่เอง      
╚══════════════════════╝
 """)
    
    hobbits()
    power()
    fears()
    nickname()


    print("\n🎊 ยินดีต้อนรับน้อง " + name +"  สู่วงการนอนน้อย! แล้วเจอกันวันที่ 16 🎊")




def hobbits():
    hobbys = ["คุยกับ ai ยันเช้า","F5 รัวๆ เพื่อแก้ BUG", "กรีดร้องเวลาเจอ ERROR" , "หลับ1ตื่นเพื่อเเก้ BUG"]
    hobby = random.choice(hobbys)
    print("งานอกิเรก 💼 : " + hobby)


def power():
    powers = ["ไม่นอนได้ 1 เดือน", "มองเห็น bug ทะลุกำแพง","control c / control v โดยการมอง ", "มองเพดานแเล้วเห็นlogic"]
    Power = random.choice(powers)
    print("พลังวิเศษ 🦸 : " + Power)

def fears():
    Fears = ["Internet หาย", "Ai ล้ม","วัน Deploy", "มันรันได้ยังไง!!!"]
    Fear = random.choice(Fears)
    print("โกโก้ กลัว 😧 : " + Fear)

def nickname():
    nicknames = [
        "เจ้าแห่งบัค",
        "นักล่า Error", 
        "ราชาคอมไพล์",
        "ซูเปอร์ดีบัค",
        "มาสเตอร์โคปี้เพส",
        "เทพแห่ง Stack Overflow",
        "องค์หญิงแห่ง Git",
        "ดาร์คลอร์ดแห่ง Terminal",
        "นินจาโค้ด",
        "ผู้พิทักษ์ Syntax"
    ]
    Nickname = random.choice(nicknames)
    print("ฉายา 😎 : " + Nickname)

if __name__ == "__main__":
    main()
