#1. Üçrəqəmli tam ədəd verilmişdir. Onun soldan birinci rəqəmini silib, sağ tərəfə yazdılar. Alınan ədədi çıxışa verin.
def reqemleri_ayir(eded):
    a = eded // 100
    b = (eded // 10) % 10
    c = eded % 10

    yeni = b * 100 + c * 10 + a
    print(yeni)

# İstifadə
reqemleri_ayir(357)

#2. Üçrəqəmli müsbət tam ədəd verilib. Həmin ədədin başlanğıcına və sonuna 3 rəqəmini yazmaqla yeni ədəd alın.

def yeni_eded(eded):
    yeni = int("3" + str(eded) + "3")
    print(yeni)

# İstifadə
yeni_eded(125)

#3. Üçrəqəmli həqiqi ədədlər verilmişdir. Bu ədələrin ədədi ortasını və həndəsi ortasını tapın

def reqemler(eded):
    a = eded // 100
    b = (eded // 10) % 10
    c = eded % 10

    ededi_orta = (a + b + c) / 3
    hendesi_orta = (a * b * c) ** (1/3)

    print("Ədəd:", eded)
    print("Ədədi orta:", ededi_orta)
    print("Həndəsi orta:", hendesi_orta)

# İstifadə
reqemler(357)

#4. Həqiqi a, b, c, d, e ədədlərindən ibarət ardıcıllıq verilmişdir. Birinci və axırıncıdan başqa hər bir ədədi öz qonşularının ədədi ortası ilə əvəz edin.

def reqemler(a,b,c,d,e):


    print("a", a)
    print("b", (a+c)/2)
    print("c", (b+d)/2)
    print("d", (c+e)/2)
    print("e", e)

# İstifadə
reqemler(a=3,b=6,c=5,d=9,e=10)

#5. Beşrəqəmli natural ədəd verilmişdir. Bu ədədin ilk iki rəqəminin cəmi ilə son iki rəqəminin cəmi arasındakı fərqi tapın.

def reqemler(eded):

    a = eded // 10000
    b = (eded // 1000) % 10
    d = (eded // 10) % 10
    e = eded % 10

    ferq = (a + b) - (d + e)

    print("Fərq:", ferq)


# İstifadə
reqemler(56783)





