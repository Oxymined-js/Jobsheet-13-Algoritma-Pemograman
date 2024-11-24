def weight_conversion():
berat = int(input("Masukkan berat anda > "))
satuan = int(input("Dalam satuan apa berat yang anda masukkan ? (K untuk K6, L untuj=k LSB)> "))

if satuan.lower() == 'L':
    print(f"Berat anda dikonversi menjadi kilogram adalah {round(berat * 0.453592)} kg")
elif satuan.lower() == 'k':
    print(f"Berat anda dikonversi menjadi pons adalah {round(berat * 2.20462)} lbs")    

