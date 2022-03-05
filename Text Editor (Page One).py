import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application = tk.Tk()
main_application.geometry("1000x700")
main_application.title("Text Editor")

# **********************************************Main Menu*******************************************
main_menu = tk.Menu(main_application)

file = tk.Menu(main_menu,tearoff = 0 )
#add icon
new_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/new.png" )
open_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/open.png" )
save_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/save.png" )
save_as_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/save_as.png" )
exit_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/exit.png" )

edit = tk.Menu(main_menu,tearoff = 0 )
# icons
copy_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/copy.png" )
paste_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/paste.png" )
cut_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/cut.png" )
clear_all_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/clear_all.png" )
find_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/find.png" )


view = tk.Menu(main_menu,tearoff = 0)
tool_bar_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/tool_bar.png" )
status_bar_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/status_bar.png" )


colour_theame = tk.Menu(main_menu,tearoff = 0 )

light_default_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/light_default.png" )
light_plus_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/light_plus.png" )
dark_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/dark.png" )
red_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/red.png" )
monokai_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/monokai.png" )
night_blue_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/night_blue.png" )

theame_choise = tk.StringVar()
color_icon = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

colour_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus': ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
}
#cascade

main_menu.add_cascade(label = "File",menu = file)
main_menu.add_cascade(label = "Edit",menu = edit)
main_menu.add_cascade(label = "View",menu = view)
main_menu.add_cascade(label = "Colour",menu =colour_theame)

# ----------------------------------------------End Main Menu---------------------------------------


# **********************************************Tool Bar*******************************************

tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP , fill = tk.X)


#font box
font_tuple = tk.font.families()
font_families = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width = 30 ,textvariable = font_families,state = 'readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row = 0 ,column= 1,padx=5)

# font size
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width = 20 , textvariable = size_var,state = 'readonly')
font_size['values'] = tuple(range(10,70))
font_size.current(10)
font_size.grid(row = 0, column = 2,padx =5)

#bold button
bold_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/bold.png")
bold_button = ttk.Button(tool_bar,image = bold_icon)
bold_button.grid(row = 0 ,column = 3,padx=5)

#italic button
italic_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/italic.png")
italic_button = tk.Button(tool_bar,image = italic_icon)
italic_button.grid(row = 0,column = 4,padx=5)
#underline button
underline_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/underline.png")
underline_button = tk.Button(tool_bar,image = underline_icon)
underline_button.grid(row = 0,column = 5,padx=5)

#font colour button

font_colour_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/font_color.png")
font_colour_button = ttk.Button(tool_bar,image = font_colour_icon)
font_colour_button.grid(row = 0 ,column = 6,padx=5)

#align left

align_left_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/align_left.png")
align_left_button = ttk.Button(tool_bar,image = align_left_icon)
align_left_button.grid(row = 0 ,column = 7,padx = 5)

#align center
align_center_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/align_center.png")
align_center_button = ttk.Button(tool_bar,image = align_center_icon)
align_center_button.grid(row = 0 ,column = 8,padx = 5)

#align centre
align_right_icon = tk.PhotoImage(file=r"C:\Users\jadon\PycharmProjects\Page_One\icon/align_right.png")
align_right_button = ttk.Button(tool_bar,image = align_right_icon)
align_right_button.grid(row = 0, column = 9,padx=5)

# ----------------------------------------------End Tool Bar---------------------------------------

# **********************************************Text editor*******************************************
text_editor = tk.Text(main_application)
text_editor.config(wrap = 'word',relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

#font family and font size functonality

current_font_family = 'Arial'
current_font_size = 0

def change_font(abhishek):
    global current_font_family
    current_font_family=font_families.get()
    text_editor.configure(font = (current_font_family,current_font_size))

def change_font_size(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font = (current_font_family,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_font_size)

# buttons functionality
#bold button

def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
         text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
bold_button.configure(command=change_bold)

#italic functionality

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
         text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
italic_button.configure(command=change_italic)

#underline functionality

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
         text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
underline_button.configure(command=change_underline)


#change font colour functionality

def change_font_colour():
    colour_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=colour_var[1])
font_colour_button.configure(command = change_font_colour)

#align functionality

def align_left():
    text_content =text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_button.configure(command=align_left)

# align center

def align_center():
    text_content =text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
align_center_button.configure(command=align_center)


#align right

def align_right():
    text_content =text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
align_right_button.configure(command=align_right)










# ----------------------------------------------End Text editor---------------------------------------


# **********************************************status bar************************************

status_bar = ttk.Label(main_application,text = "Status Bar")
status_bar.pack(side=tk.BOTTOM)
text_modified = False
def changed(event = False):
    if text_editor.edit_modified():
        global text_modified
        text_modified = True
        word = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text = f'Words : {word} characters : {characters}')
    text_editor.edit_modified(0)
text_editor.bind('<<Modified>>',changed)


# ----------------------------------------------End status bar--------------------------------

# **********************************************main menu functionality*******************************************
##variable
url = ''

#new functionality
def new(event = None):
    global url
    url = ''
    text_editor.delete(1.0 , tk.END)

# file command

file.add_command(label = 'New',image= new_icon,compound = tk.LEFT,accelerator = 'Ctrl+N',command = new)

#open functionality
def open_file(event = None):
    global  url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title = 'Select File',filetype=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
file.add_separator()
file.add_command(label = 'Open',image= open_icon,compound = tk.LEFT,accelerator = 'Ctrl+O',command = open_file)
##save functionality

def save(event = None):
    global  url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding="utf-8") as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension = '.txt',filetype=(('Text File','*.txt'),('All Files','*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
file.add_separator()
file.add_command(label = 'Save',image= save_icon,compound = tk.LEFT,accelerator = 'Ctrl+S',command = save)
## save as funtionality

def save_as(event = None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetype=(('Text File', '*.txt'), ('All Files', '*.*')))
        url.write(content)
        url.close()
    except:
        return
file.add_separator()
file.add_command(label = 'Save as',image= save_as_icon,compound = tk.LEFT,accelerator = 'Ctrl+Alt+S',command = save_as)

## exit functionality

def exit(event = None):
    global text_modified,url
    try:
        if text_modified:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file  ?')
            if mbox == True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetype=(('Text File', '*.txt'), ('All Files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
    except:
        return

##find functionality

def find_func( event = None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match',1.0,tk.END)
        match = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                match += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground = 'red',background = 'yellow')

    def replace():
        word = find_input.get()
        replace_text =replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)




    find_dialog = tk.Toplevel()
    find_dialog.geometry('450x250')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)

    ## frame
    find_frame = tk.LabelFrame(find_dialog,text = 'Find/Replace')
    find_frame.pack(pady = 20)

    ##labels

    text_find_label = ttk.Label(find_frame,text = 'Find ')
    text_replace_label = ttk.Label(find_frame,text = 'Replace ')

    ##entry

    find_input=ttk.Entry(find_frame,width = 30)
    replace_input=ttk.Entry(find_frame,width = 30)

    ##button
    find_button = ttk.Button(find_frame,text='Find',command = find)
    replace_button = ttk.Button(find_frame,text='Replace',command = replace)

    ##levilgrid
    text_find_label.grid(row = 0,column = 0,padx = 4,pady = 4)
    text_replace_label.grid(row = 1,column = 0,padx = 4,pady = 4)

    find_input.grid(row = 0,column = 1,padx = 4,pady = 4)
    replace_input.grid(row = 1,column = 1,padx = 4,pady = 4)


    find_button.grid(row = 2,column = 0,padx=8,pady = 4)
    replace_button.grid(row = 2,column = 1,padx=8,pady = 4)

    find_dialog.mainloop()










file.add_separator()
file.add_command(label = 'Exit',image= exit_icon,compound = tk.LEFT,accelerator = 'Ctrl+Q',command = exit)


#file commands
edit.add_command(label = 'Copy',image= copy_icon,compound = tk.LEFT,accelerator = 'Ctrl+C',command = lambda :text_editor.event_generate('<Control c>'))
edit.add_separator()
edit.add_command(label = 'Paste',image= paste_icon,compound = tk.LEFT,accelerator = 'Ctrl+V',command = lambda :text_editor.event_generate('<Control v>'))
edit.add_separator()
edit.add_command(label = 'Cut',image= cut_icon,compound = tk.LEFT,accelerator = 'Ctrl+X',command = lambda :text_editor.event_generate('<Control x>'))
edit.add_separator()
edit.add_command(label = ' Clear All',image= clear_all_icon,compound = tk.LEFT,accelerator = 'Ctrl+Alt+X',command = lambda :text_editor.delete(1.0,tk.END))
edit.add_separator()
edit.add_command(label = 'Find',image= find_icon,compound = tk.LEFT,accelerator = 'Ctrl+F',command = find_func)

#view commands

show_tool_bar = tk.BooleanVar()
show_tool_bar.set(True)
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)

def hide_tool_bar():
    global  show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand = True)
        status_bar.pack(side = tk.BOTTOM)
        show_tool_bar=True


def hide_status_bar():
    global  show_status_bar,status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar=False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_status_bar = True



view.add_checkbutton(label= 'Tool Bar',onvalue = 1,offvalue = 0,variable = show_tool_bar, image= tool_bar_icon,compound = tk.LEFT,command = hide_tool_bar)
view.add_separator()
view.add_checkbutton(label= 'Status  Bar',onvalue = 1,offvalue = 0,variable = show_status_bar,image= status_bar_icon,compound = tk.LEFT,command = hide_status_bar)

#colour theme
def theme_change():
    chosen_theme = theame_choise.get()
    color_tuple = colour_dict.get(chosen_theme)
    fg_color ,bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background = bg_color,fg= fg_color)
count = 0
for i in colour_dict:
    colour_theame.add_radiobutton(label = i,image = color_icon[count] , variable = theame_choise,compound = tk.LEFT ,command = theme_change)
    colour_theame.add_separator()
    count += 1

# ----------------------------------------------End main menu functionality---------------------------------------
main_application.config(menu= main_menu)

main_application.bind('<Control-n>',new)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save)
main_application.bind('<Control-Alt-s>',save_as)
main_application.bind('<Control-q>',exit())
main_application.bind('<Control-f>',find_func)




main_application.mainloop()


