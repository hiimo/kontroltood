#hiimo töö
#raske töö
from tkinter import *
#akna seaded
aken = Tk()
aken.geometry("300x200")
aken.title("hiimo raske töö")
aken.resizable(False, False)
#teeb nii et kui paned numbri siis ta paneb teksti, \n paneb enteri, {j+1} i on numbri arv ja +1 on sellepärast et python alustab 0ist vmdagi
def kysija():
    number = int(prygi2.get())
    for j in range(number):
        h = f"Võõrustaja: 'Tere!' \n Täna {j+1}. korda tervitada, mõtiskleb võõrustaja \n  Külaline: 'Tere, suur tänu kutse eest!'"
        aa.config(text=h)

#kysib mitu inimest laheb
prygi = Label(aken, text="mitu inimest lheb")
prygi.grid(row=1, column=1)
#koht kuhu kirjutad mitu inimest laheb
prygi2 = Entry(aken)
prygi2.grid(row=2,column=1)
#vajutatav nupp mis paneb asja tööle 
sisesta = Button(aken, text= 'sisesta', command = kysija, width=15)
sisesta.grid(row=3, column=1)
#koht kuhu laheb see pikk tekst ehk h
aa = Label(aken, text = "siin ytleb")
aa.grid(row=7, column=1)
#paneb asja loopi et ära ei lõpeks
aken.mainloop()