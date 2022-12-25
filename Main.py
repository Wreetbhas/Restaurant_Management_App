from tkinter import *
from tkinter.messagebox import showinfo
from extract_catalog import items
from transaction import *
import datetime

root = Tk()

root.title("Restaurant Management System")

class Item():
    def __init__(self, row, i_code) -> None:
        self.code = i_code
        self.name = items[i_code]['name']
        self.price = items[i_code]['price']
        self.bQty = items[i_code]['bQty']
        self.value = IntVar(value=0)

        label = Label(root, text = "{} - {}".format(items[i_code]['name'], items[i_code]['bQty']), anchor='w', width=20, fg = 'blue')
        label.grid(row=row,column=0)
        self.entry = Entry(root, textvariable = self.value, fg='red', width=4)
        self.entry.grid(row=row,column=1)
        btn = Button(root, text='+', bg='cyan', command = self.addQty)
        btn.grid(row=row,column=2)

    def addQty(self):
        self.value=IntVar(value=self.value.get()+1)
        self.entry.delete(0,END)
        self.entry.insert(0,self.value.get())

def showCatalog():
    cat_win = Toplevel()
    cat_win.wm_title('Catalog')

    Label(cat_win,text='Item',bg='yellow',fg='green',width=15).grid(row=0,column=0)
    Label(cat_win,text='Quantity',bg='yellow',fg='green',width=15).grid(row=0,column=1)
    Label(cat_win,text='Rate',bg='yellow',fg='green',width=15).grid(row=0,column=2)

    for i in range(len(item_list)):
        Label(cat_win,text=item_list[i].name,fg='blue',width=15).grid(row=i+1,column=0)
        Label(cat_win,text=item_list[i].bQty,fg='purple',width=15).grid(row=i+1,column=1)
        Label(cat_win,text='₹ '+str(item_list[i].price),fg='red',width=15).grid(row=i+1,column=2)

def calculateAmt():
    global amt
    amt = 0

    for item in item_list:
        amt += item.price*item.value.get()

    if amt > 0:
        amt_lbl.config(text="Amount Payable : ₹ "+str(amt))
        ord_btn.config(state='active')

def order():
    date_time = datetime.datetime.now()
    update_transaction(date_time,amt)
    ord_btn.config(state='disabled')
    showinfo('Confirmation', 'Order Placed Successfully')

    amt_lbl.config(text="")

    for i in item_list:
        i.value=IntVar(value=0)
        i.entry.delete(0,END)
        i.entry.insert(0, 0)

def viewHistory():
    hst_win = Toplevel()
    hst_win.wm_title('History')

    frame1 = Frame(hst_win)
    frame1.pack()

    frame2 = Frame(hst_win)
    frame2.pack()

    Label(frame1, text='Date', width=20, fg='green', bg='yellow').grid(row=0, column=0)
    Label(frame1, text='Time', width=20, fg='green', bg='yellow').grid(row=0, column=1)
    Label(frame1, text='Amount', width=20, fg='green', bg='yellow').grid(row=0, column=2)
    Label(frame1, text='Status', width=20, fg='green', bg='yellow').grid(row=0, column=3)

    scroll_bar = Scrollbar(frame2)

    scroll_bar.pack( side = RIGHT, fill = Y )

    listbox = Listbox(frame2,yscrollcommand = scroll_bar.set,font = 'TkFixedFont',activestyle = 'dotbox',width=70)

    trans = extract_history()

    for i in range(len(trans),0,-1):
        tran = trans[i]
        listbox.insert(END,tran['date'].rjust(14)+tran['time'].rjust(20)+("₹ "+tran['amt']).center(21)+tran['status'].rjust(13))
    
    listbox.pack(side = LEFT, fill = BOTH)

    scroll_bar.config( command = listbox.yview )

item_list=[]
row=0
for i_code in items.keys():
    item_list.append(Item(row,i_code))
    row+=1

cal_btn=Button(root,text="Calculate Amount",bg="yellow",fg="green",command=calculateAmt)
cal_btn.grid(row=row,column=0,columnspan=2)

amt_lbl=Label(root,text="",fg='green')
amt_lbl.grid(row=4,column=5)

cat_btn=Button(root,text="View Catalog",bg="yellow",fg="green",width=20,command=showCatalog)
cat_btn.grid(row=0,column=5,padx=10)

hst_btn=Button(root,text="View Transaction History",bg="yellow",fg="green",width=20,command=viewHistory)
hst_btn.grid(row=1,column=5,padx=10)

ord_btn=Button(root,text="Place Order",bg="orange",fg="red",command=order,state="disabled")
ord_btn.grid(row=5,column=5)

root.mainloop()