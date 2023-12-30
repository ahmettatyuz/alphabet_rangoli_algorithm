def print_rangoli(size):
    letters = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
    loop = 1
    rows1 = []
    for i in range(size*2-1):
        if(i<size):
            tersStr = ""
            for j in range(loop):
                if(j<=loop//2):
                    letter = letters[size-j-1]
                    tersStr +=letter
            duzStr = tersStr
            tersStr = tersStr[::-1]
            tersStr = tersStr[1:len(tersStr)]
            rows1.append(duzStr+tersStr)
            loop+=2
            
    rows2 = rows1.copy()
    rows2 = rows2[::-1]
    rows2.pop(0)
    allRows = rows1 + rows2
    
    for i in allRows:
        a = "-".join(i)
        length = len(a)
        maxLength = (size*2-1) + (size*2-2)
        tireSayisi = (maxLength - length)//2
        tire = "-"*tireSayisi
        print(tire,end="")
        print(a,end="")
        print(tire)       
            
            
            

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)