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
    print(" มาต่อกันนนน\n")



main()