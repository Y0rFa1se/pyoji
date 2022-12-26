import tkinter as tk

from tkinter import filedialog
from PIL import Image, ImageTk


#사진 편집
def add_listbox_pics(pictures):
	pic_listbox = tk.Listbox(ui, height = 6, width = 35)
	pic_listbox.grid(row = 3, column = 1)
	pic_listbox.yview()
	for i in pictures:
		pic_listbox.insert(0, i)

#마스크 편집
def add_listbox_mask(_mask):
	mask_listbox = tk.Listbox(ui, height = 1, width = 35)
	mask_listbox.grid(row = 3, column = 3, sticky = 'n')
	mask_listbox.insert(0, _mask)

#표지 편집
def add_listbox_cover(_cover):
	cover_listbox = tk.Listbox(ui, height = 1, width = 35)
	cover_listbox.grid(row = 3, column = 5, sticky = 'n')
	cover_listbox.insert(0, _cover)


#사진 선택하는 버튼
def select_pics(event):
	global pics
	pics = filedialog.askopenfilenames(parent = ui, initialdir = '/', title = '사진 선택', filetypes = (('png', '*.png'), ('jpg', '*.jpg'), ('걍 암거나', '*.*')))
	add_listbox_pics(pics)

#마스크 선택하는 버튼
def select_mask(event):
	global mask
	mask = filedialog.askopenfilename(parent = ui, initialdir = '/', title = '마스크 선택', filetypes = (('png', '*.png'), ('jpg', '*.jpg'), ('걍 암거나', '*.*')))
	add_listbox_mask(mask)

#표지 선택하는 버튼
def select_cover(event):
	global cover
	cover = filedialog.askopenfilename(parent = ui, initialdir = '/', title = '표지 선택', filetypes = (('png', '*.png'), ('jpg', '*.jpg'), ('걍 암거나', '*.*')))
	add_listbox_cover(cover)


#내보내는 링크 설정
def output_link(event):
	global output_dir
	output_dir = filedialog.askdirectory(parent = ui, initialdir = '/', title = '경로 선택')
	save_dir['text'] = output_dir

#시작
def run_program(event):
	#pics: 사진
	#mask: 마스크
	#cover: 표지
	#output_dir: 저장할 장소
	pass


#창 생성
ui = tk.Tk()
ui.title('ㅇㅇ')
ui.resizable(width = False, height = False)

tk.Label(text = ' ').grid(row = 0, column = 0)
tk.Label(text = ' ').grid(row = 1, column = 0)


#사진 프리뷰/선택 버튼
pic_preview = Image.open('pyoji/imgs/500.png').resize((250, 315), Image.ANTIALIAS)
pic_preview = ImageTk.PhotoImage(pic_preview)
pic = tk.Button(ui, image = pic_preview)
pic.bind('<Button-1>', select_pics)
pic.grid(row = 1, column = 1)

tk.Label(text = ' ').grid(row = 1, column = 2)


#마스크 프리뷰/선택 버튼
mask_preview = Image.open('pyoji/imgs/500.png').resize((250, 315), Image.ANTIALIAS)
mask_preview = ImageTk.PhotoImage(mask_preview)
mask = tk.Button(ui, image = mask_preview)
mask.bind('<Button-1>', select_mask)
mask.grid(row = 1, column = 3)

tk.Label(text = ' ').grid(row = 1, column = 4)


#표지 프리뷰/선택 버튼
cover_preview = Image.open('pyoji/imgs/500.png').resize((250, 315), Image.ANTIALIAS)
cover_preview = ImageTk.PhotoImage(cover_preview)
cover = tk.Button(ui, image = cover_preview)
cover.bind('<Button-1>', select_cover)
cover.grid(row = 1, column = 5)

tk.Label(text = ' ').grid(row = 1, column = 6)
tk.Label(text = ' ').grid(row = 2, column = 0)


#사진 링크
pic_listbox = tk.Listbox(ui, height = 6, width = 35)
pic_listbox.grid(row = 3, column = 1)
pic_listbox.yview()

tk.Label(text = ' ').grid(row = 2, column = 2)


#마스크 링크
mask_listbox = tk.Listbox(ui, height = 1, width = 35)
mask_listbox.grid(row = 3, column = 3, sticky = 'n')

tk.Label(text = ' ').grid(row = 2, column = 4)


#표지 링크
cover_listbox = tk.Listbox(ui, height = 1, width = 35)
cover_listbox.grid(row = 3, column = 5, sticky = 'n')

tk.Label(text = ' ').grid(row = 4, column = 0)
tk.Label(text = ' ').grid(row = 5, column = 0)


#내보내는 링크
save_dir = tk.Button(ui, text = '내보낼 경로 설정', width = 70, height = 2)
save_dir.bind('<Button-1>', output_link)
save_dir.grid(row = 5, column = 1, columnspan = 3, rowspan = 2)

tk.Label(text = ' ').grid(row = 5, column = 4)


#시작
run = tk.Button(ui, text = '시작', width = 20, height = 2)
run.bind('<Button-1>', run_program)
run.grid(row = 5, column = 5, rowspan = 2)


tk.Label(text = ' ').grid(row = 6, column = 0)
tk.Label(text = ' ').grid(row = 7, column = 0)
tk.Label(text = ' ').grid(row = 8, column = 0)
tk.Label(text = ' ').grid(row = 9, column = 0)
tk.Label(text = ' ').grid(row = 10, column = 0)
tk.Label(text = ' ').grid(row = 11, column = 0)
tk.Label(text = ' ').grid(row = 12, column = 0)
tk.Label(text = ' ').grid(row = 13, column = 0)
tk.Label(text = ' ').grid(row = 14, column = 0)

ui.mainloop()