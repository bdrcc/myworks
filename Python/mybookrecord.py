# 本の読書記録（後から編集も可能）アプリ
import tkinter as tk
import tkinter.ttk as ttk
import datetime
import json
import requests

# 基本設定
w_x, w_y, y_re, y_bl = 500, 400, 70 ,40
# mo_f1, mo_f2 = 'UD デジタル 教科書体 NK-B','UD デジタル 教科書体 NK-R'
mo_f1, mo_f2 = 'メイリオ','メイリオ'
app_mode = ('記録モード','編集モード','確認モード','オフライン')
h1_mo = 'モード'
c = '#ffffaa'
c_t  = '#000'

# 要素の出現有無
def button_onof(area:list, onof:int):
    """画面表示の有無を行う関数"""
    global w_x, w_y, y_re, y_bl
    # オフ一覧
    if onof==0:
        for a in area:
            if a=='main':
                title.place_forget()
                button_re.place_forget()
                button_of_re.place_forget()
                button_ed.place_forget()
                button_che.place_forget()
            elif a=='to_ho':
                h1.place_forget()
                button_home.place_forget()
            elif a=='isbn':
                h2.place_forget()
                p1.place_forget()
            elif a=='isbn_se':
                button2.place_forget()
            elif a=='b_content':
                h3.place_forget()
                h4.place_forget()
                h5.place_forget()
                h6.place_forget()
                h7.place_forget()
                h8.place_forget()
                p2.place_forget()
                p3.place_forget()
                p4.place_forget()
                p6.place_forget()
                sel1.place_forget()
                memo1.place_forget()

    # オン一覧(基本は1にしておく)
    else:
        for a in area:
            if a=='main':
                title.place(x=130, y=120)
                button_re.place(x=80, y=210)
                button_of_re.place(x=100, y=260)
                button_ed.place(x=200, y=210)
                button_che.place(x=320, y=210)
            elif a=='to_ho':
                h1.place(x=10, y=10)
                button_home.place(x=w_x-90, y=w_y-y_bl)
            elif a=='isbn':
                h2.place(x=10, y=y_re)
                p1.place(x=85, y=y_re)
            elif a=='isbn_se':
                button2.place(x=300, y=y_re)
            elif a=='b_content':
                h3.place(x=10, y=y_re+y_bl)
                h4.place(x=10, y=y_re+y_bl*2)
                h5.place(x=10, y=y_re+y_bl*3)
                h6.place(x=150, y=y_re+y_bl*3)
                h7.place(x=10, y=y_re+y_bl*4)
                h8.place(x=10, y=y_re+y_bl*5)
                p2.place(x=65, y=y_re+y_bl)
                p3.place(x=170, y=y_re+y_bl*2)
                p4.place(x=75, y=y_re+y_bl*3)
                p6.place(x=65, y=y_re+y_bl*4)
                sel1.place(x=210, y=y_re+y_bl*3)
                memo1.place(x=80, y=y_re+y_bl*5+2)


def to_home(target):
    """ホーム画面に戻る"""
    button_onof(['main'],1)
    button_onof(['to_ho','isbn','isbn_se','b_content'],0)
    p5.place_forget()
    button3.place_forget()
    h10.place_forget()
    sel_re.place_forget()
    button4.place_forget()
    button5.place_forget()


def repla():
    """行った操作に対して、GUI上に出力したものを時間差で消す"""
    h_do.place_forget()
    h_do["font"]=(mo_f1,12)

def str_check(x,n):
    """記録前に , を操作する関数"""
    s=[]
    # 書き込みは0で
    if n==0:
        for i in x:
            if i==',':
                s.append('^')
            else:
                s.append(i)
        return ''.join(s)
    # 読み込み再現は1で
    elif n==1:
        if type(x) is float:
            return ''
        else:
            for i in x:
                if i=='^':
                    s.append(',')
                else:
                    s.append(i)
            return ''.join(s)

def mode_re(target):
    """読んだ本を記録するモードへ移行する"""
    button_onof(['main'],0)
    button_onof(['to_ho','isbn','isbn_se'],1)
    h1["text"] = app_mode[0]
    p1.delete(0,tk.END)

def bookse(target):
    """読んだ本を検索する"""
    # 入力されたISBNを取得    
    e=p1.get()
    e_text=[]
    for i in e:
        if i!='-':
            e_text.append(i)
    e=''.join(e_text)
    # 先頭が978または979で取得可能
    if len(e)==13 and 9780000000000 <= int(e) < 9800000000000:
        u = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'+str(e)
        res = requests.get(u)
        b_data = json.loads(res.text)
        b_tit = b_data['items'][0]['volumeInfo']['title']
        b_a = b_data['items'][0]['volumeInfo']['authors']
        if type(b_a) is list:
            b_aut='/'.join(b_a)
        else:
            b_aut=b_a
        b_p = b_data['items'][0]['volumeInfo']['pageCount']

        button_onof(['b_content'],1)
        
        # 内容を出力
        p2.delete(0,tk.END)
        p2.insert(tk.END,b_tit)
        p3.delete(0,tk.END)
        p3.insert(tk.END,b_aut)
        p4.delete(0,tk.END)
        p4.insert(tk.END,b_p)
        # 他に入力するサブ項目、ボタンを出現
        sel1.set('')
        # 日付は / 表記
        date = '/'.join(str(datetime.date.today()).split('-'))
        p6.delete(0,tk.END)
        p6.insert(tk.END,date)
        memo1.delete(0.,tk.END)
        button3.place(x=w_x-170, y=w_y-y_bl)
        h_do["text"]=f'本の情報を取得しました'
        h_do.place(x=10, y=360)
        root.after(2000, repla)
    # 入力がうまくいかない場合は、入力を再度要求
    else:
        h_do["text"]=f'ISBNを正しく入力してください'
        h_do.place(x=10, y=360)
        root.after(2000, repla)

def add_combobox_subgen(target):
    """新しいジャンルを記入したいときに、記入場所を作成する"""
    gen_se = sel1.get()
    if gen_se == '新規作成':
        p5.place(x=330, y=y_re+y_bl*3)
        p5.delete(0,tk.END)
    else:
        p5.place_forget()

def bookre(target):
    """読んだ本を記録する"""
    e=p1.get()
    e_text=[]
    for i in e:
        if i!='-':
            e_text.append(i)
    isbn = ''.join(e_text)
    b_tit = str_check(p2.get(),0)
    b_aut = str_check(p3.get(),0)
    b_p = p4.get()
    # ジャンルに対して新規作成の場合はp5から、元からあるものにはsel1から
    gen_se = sel1.get()
    if gen_se == '新規作成':
        b_gen = p5.get()
    else:
        b_gen = gen_se
    b_d = p6.get()
    b_memo = str_check(memo1.get(0.,tk.END),0)
    # memoの改行は、strip,split,join で一行に収める
    b_me = ''.join(b_memo.strip().split())
    # 空白でない場合、書き込む
    if b_d != '' and isbn != '' and b_tit != '' and b_aut != '' and b_p != '' and b_gen != '' and b_me != '':
        all_data.append([b_d, isbn, b_tit, b_aut, b_p, b_gen, b_me])
        with open('mybookrecord.csv','a', encoding='shift-jis') as f:
            f.write(f'{b_d},{isbn},{b_tit},{b_aut},{b_p},{b_gen},{b_me}\n')
        # 新規作成で追加した項目を即座に反映させるには→リストに追加してから、辞書形式で認識させる
        gen.append(b_gen)
        sel1["values"] = sorted(list(set(gen)))
        h_do["text"]='本の記録を完了しました'
    else:
        h_do["text"]='未入力の項目があり、記録できません'
    h_do.place(x=10, y=360)
    root.after(2000, repla)

def book_of_re(target):
    """オフラインで記録するモードへ移行する"""
    button_onof(['main'],0)
    button_onof(['to_ho','isbn','b_content'],1)
    h1["text"] = f'{app_mode[3]} 記録モード'
    p1.delete(0,tk.END)
    p2.delete(0,tk.END)
    p3.delete(0,tk.END)
    p4.delete(0,tk.END)
    sel1.set('')
    date = '/'.join(str(datetime.date.today()).split('-'))
    p6.delete(0,tk.END)
    p6.insert(tk.END,date)
    memo1.delete(0.,tk.END)
    button3.place(x=w_x-170, y=w_y-y_bl)


def mode_edit(target):
    global all_data
    """今までの記録を編集するモードへ移行する"""
    # 必要なボタンを出現
    button_onof(['main'],0)
    button_onof(['to_ho'],1)
    h1["text"] = app_mode[1]
    h10.place(x=250, y=25)
    sel_re.place(x=320, y=25)
    # データを読み込む
    if len(all_data)!=1:
        num = len(all_data)-1
        sel_re['values'] = list(range(1,num+1))
        sel_re.set('未選択')


def search_re(target):
    """csvデータから、対象のデータを読み込んで出力する"""
    global all_data
    button_onof(['isbn','b_content'],1)
    num = int(sel_re.get())
    re_l=all_data[num]
    p1.delete(0,tk.END)
    p1.insert(tk.END, re_l[1])
    p2.delete(0,tk.END)
    p2.insert(tk.END, str_check(re_l[2],1))
    p3.delete(0,tk.END)
    p3.insert(tk.END, str_check(re_l[3],1))
    p4.delete(0,tk.END)
    p4.insert(tk.END, re_l[4])
    sel1.set(str_check(re_l[5],1))
    date = re_l[0]
    p6.delete(0,tk.END)
    p6.insert(tk.END,date)
    memo1.delete(0.,tk.END)
    memo1.insert(tk.END, str_check(re_l[6],1))
    button4.place(x=w_x-240, y=w_y-y_bl)
    button5.place(x=w_x-160, y=w_y-y_bl)
    h_do["text"]=f'{num}番目の記録を読みこみました'
    h_do.place(x=10, y=360)
    root.after(2000, repla)

def bookrere(target):
    """読んだ本を改めて記録する"""
    global all_data
    num = int(sel_re.get())
    isbn = p1.get()
    b_tit = str_check(p2.get(),0)
    b_aut = str_check(p3.get(),0)
    b_p = p4.get()
    gen_se = sel1.get()
    if gen_se == '新規作成':
        b_gen = p5.get()
    else:
        b_gen = gen_se
    b_d = p6.get()
    b_memo = str_check(memo1.get(0.,tk.END),0)
    b_me = ''.join(b_memo.strip().split())

    if b_d != '' and isbn != '' and b_tit != '' and b_aut != '' and b_p != '' and b_gen != '' and b_me != '':
            all_data[num]=[b_d, isbn, b_tit, b_aut, b_p, b_gen, b_me]
            with open('mybookrecord.csv','w', encoding='shift-jis') as f:
                for a in all_data:
                    for i in range(len(a)-1):
                        f.write(f'{a[i]},')
                    f.write(f'{a[len(a)-1]}\n')
            gen.append(b_gen)
            sel1["values"] = sorted(list(set(gen)))
            h_do["text"]=f'{num}番目の記録の編集を完了しました'
    else:
        h_do["text"]='未入力の項目があり、記録できません'
        h_do["font"]=(mo_f1,10)
    h_do.place(x=10, y=360)
    root.after(2000, repla)
    gen.append(b_gen)
    sel1["values"] = sorted(list(set(gen)))

def re_del(target):
    """指定されたデータ記録を削除する"""
    global all_data
    num = int(sel_re.get())
    all_data.pop(num)
    with open('mybookrecord.csv','w', encoding='shift-jis') as f:
        for a in all_data:
            for i in range(len(a)-1):
                f.write(f'{a[i]},')
            f.write(f'{a[len(a)-1]}\n')

    # データ再編成
    n = len(all_data)-1
    sel_re['values'] = list(range(1,n+1))
    sel_re.set('未選択')
    h_do["text"] = f'{num}番目の記録を削除しました'
    h_do.place(x=10, y=360)
    root.after(2000, repla)
    button4.place_forget()
    button5.place_forget()

def all_check(target):
    h_do["text"]='鋭意制作中のため、しばしお待ちを！'
    h_do.place(x=135, y=320)
    root.after(2000, repla)

# 基本画面
root = tk.Tk()
root.title("読書記録アプリ")
root.minsize(w_x, w_y)

# ジャンルデータ読み込み、csvがなければ作成
try:
    with open('mybookrecord.csv','r', encoding='shift-jis') as f:
        all_data = [l.strip().split(',') for l in f]
    gen = []
    for a in all_data:
        gen.append(a[5])
    gen.remove('ジャンル')
    gen = ['','新規作成'] + sorted(list(set(gen)))
except FileNotFoundError:
    p_l = '日付,ISBN,タイトル,著者,ページ数,ジャンル,感想・メモ\n'
    all_data=[[p_l]]
    with open('mybookrecord.csv','w', encoding='shift-jis') as f:
        f.write(p_l)
    gen = ['','新規作成']
except ValueError:
    p_l = '日付,ISBN,タイトル,著者,ページ数,ジャンル,感想・メモ\n'
    all_data=[[p_l]]
    with open('mybookrecord.csv','w', encoding='shift-jis') as f:
        f.write(p_l)
    gen = ['','新規作成']


# ホームレイアウト
title = tk.Label(text='読書記録アプリ',font=(mo_f1,28),bg=c)

button_re = tk.Button(text=app_mode[0],font=(mo_f1,14), fg = '#000')
button_re.bind('<Button-1>',mode_re)

button_of_re = tk.Button(text=app_mode[3],font=(mo_f1,10), fg = '#fff', bg = '#50d050')
button_of_re.bind('<Button-1>',book_of_re)

button_ed = tk.Button(text=app_mode[1],font=(mo_f1,14), fg = '#fff', bg = '#50d050')
button_ed.bind('<Button-1>',mode_edit)

button_che = tk.Button(text=app_mode[2],font=(mo_f1,14), fg = '#fff', bg='#cc0033')
button_che.bind('<Button-1>',all_check)

button_onof(['main'],1)


# 共通項目色々
h1 = tk.Label(text='',font=(mo_f1,20),bg=c)

button_home = tk.Button(text='ホームへ',font=(mo_f1,10),padx=0,pady=0)
button_home.bind('<Button-1>',to_home)

h_do = tk.Label(text='待機中',font=(mo_f1,12),fg='#f00',bg=c)
h_do.place_forget()

# 記録モード用
h2 = tk.Label(text='ISBN_13：',font=(mo_f2,10),bg=c)

p1 = tk.Entry(width=17,font=(mo_f2,10))

button2 = tk.Button(text='検索する',font=(mo_f1,10),padx=0,pady=0,fg=c_t)
button2.bind('<Button-1>',bookse)

h3 =tk.Label(text='タイトル：',font=(mo_f2,10),bg=c)

p2 = tk.Entry(width=40,font=(mo_f2,10))

h4 = tk.Label(text='著者（複数名は / 区切り）:',font=(mo_f2,10),bg=c)

p3 = tk.Entry(width=30,font=(mo_f2,10))

h5 = tk.Label(text='ページ数：',font=(mo_f2,10),bg=c)

p4 = tk.Entry(width=5,font=(mo_f2,10),justify=tk.CENTER)

h6 = tk.Label(text='ジャンル：',font=(mo_f2,10),bg=c)

sel1 = ttk.Combobox(root, values = gen, width = 15, state='readonly')
sel1.set(gen[0])
sel1.bind('<<ComboboxSelected>>', add_combobox_subgen)

p5 = tk.Entry(width=15,font=(mo_f2,10))
p5.place_forget()

h7 = tk.Label(text='読了日：',font=(mo_f2,10),bg=c)

p6 = tk.Entry(width=12,font=(mo_f2,10),justify=tk.CENTER)

h8 = tk.Label(text='感想・メモ：',font=(mo_f2,10),bg=c)

memo1 = tk.Text(width=40, height=5,font=(mo_f2,10))

button3 = tk.Button(text='記録する',font=(mo_f1,10),padx=0,pady=0,fg=c_t)
button3.bind('<Button-1>',bookre)
button3.place_forget()

# 編集モード用
h10 = tk.Label(text='記録番号',font=(mo_f2,10),bg=c)
h10.place_forget()

sel_re = ttk.Combobox(root, values = '', width=5,font=(mo_f2,10), state='readonly')
sel_re.set('')
sel_re.bind('<<ComboboxSelected>>', search_re)
sel_re.place_forget()

button4 = tk.Button(text='上書きする',font=(mo_f1,10),padx=0,pady=0,fg=c_t)
button4.bind('<Button-1>',bookrere)
button4.place_forget()

button5 = tk.Button(text='削除する',font=(mo_f1,10),padx=0,pady=0,fg=c_t)
button5.bind('<Button-1>',re_del)
button5.place_forget()

button_onof(['to_ho','isbn','isbn_se','b_content'],0)

root.configure(bg=c)
root.mainloop()
