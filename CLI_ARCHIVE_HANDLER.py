import time
import tkinter
from pathlib import Path
import tkinter as tk
import colorama
import shutil
import re

#Class archive
class ARCHIVE:
    #Init
    def __init__(self,route,use):
        self.route = Path(route)
        self.color = colorama.Fore
        self.win2 = None
        self.use = use
        self.routes = []
        self.get = "Program was ended before an item was selected"
    #Yeah, be repetitive it's not an option so there's a func for all #^_^#
    def _logic(self,value):
        print(self.color.RESET)
        if "y" in value.lower():
           return True
        else:
           return False
    #change log if carpet or archive
    @staticmethod
    def _change(value):
       type_name = ""
       if value.suffix:
           type_name = "Archive"
       else:
           type_name = "Carpet"
       return type_name
    #Handle duple
    def _duple(self,file,mode,question,action,confirm,route,num=0):
        pattern = rf"^{re.escape(file.stem)}(?:_\d+)?$"
        return_name = self._change(file)
        archive = route / file.name
        archives = []
        for arch in route.glob(f"*{file.suffix}" if return_name != "Carpet" else "*"):
            if re.match(pattern, arch.stem):
                archives.append(arch.name)
            if arch.stem == file.stem:
                archives.append("0")
        numbers = re.findall(r"[0-9]+", "".join(archives))
        if numbers:
            numbers = list(map(int, numbers))
            g_numbers = [n1 for n1 in range(0, int(max(numbers)) + 1)]
            holes = list(set(g_numbers[1:]) - set(numbers[1:]))
            if holes:
                num = int(max(holes) * 1)
            else:
                num = int(max(numbers)) + 1
        rename = route / (file.stem + "_" + str(num) + file.suffix)
        if confirm:
           if return_name == "Archive":
               archive.rename(rename)
               archive.touch()
               return f"{return_name} {archive.name} was {action} in {route}"
           else:
               archive.rename(rename)
               archive.mkdir()
               return f"{return_name} {archive.name} was {action} in {route}"
        else:
           if self._confirm(archive,mode,question,self.route.name):
               if return_name == "Archive":
                   archive.rename(rename)
                   archive.touch()
                   return f"{return_name} {rename.name} was {action} in {route}"
               else:
                   archive.rename(rename)
                   archive.mkdir()
                   return f"{return_name} {rename.name} was {action} in {route}"
           else:
               return f"{return_name} {rename.name} was not {action} cause user decision"
    #Confirm it's a func for some logics
    def _confirm(self,archive,mode,question,route="None"):
        text = (self.color.BLUE + f"Are you sure to {question} " +
               self.color.MAGENTA + f"{archive.name} " +
               self.color.BLUE + "in " +
               self.color.MAGENTA + f"{route} " +
               self.color.BLUE + "y/n:" )
        if mode == "cr":
            ask = input(text)
            return self._logic(ask)
        elif mode == "co":
            ask = input(text)
            return self._logic(ask)
        elif mode == "de":
            ask = input(text)
            return self._logic(ask)
        elif mode == "re":
            ask = input(text)
            return self._logic(ask)
        else:
            return "How do you change the mode HOW!"
    #The func to create archives
    def create_(self,archive_name,archive_type,confirm):
        if archive_type != "folder":
           archive = self.route / Path(archive_name+"."+archive_type)
        else:
           archive = self.route / Path(archive_name)
        return_name = self._change(archive)
        if not archive.exists():
            if not confirm:
                 if self._confirm(archive, "cr", "create", self.route.name):
                     if return_name == "Archive":
                         archive.touch()
                     else:
                         archive.mkdir()
                     return f"{return_name} {archive.name} was created in {self.route}"
                 else:
                     return f"{return_name} {archive.name} was not created cause user decision"
            else:
               if return_name == "Archive":
                   archive.touch()
               else:
                   archive.mkdir()
               return f"{return_name} {archive.name} was created in {self.route}"
        else:
            return self._duple(archive,"cr","create","created",confirm,self.route)
    #The func to copy archives
    def copy_(self,archive_name,new_route,confirm):
        archive = self.route / archive_name
        return_name = self._change(archive)
        new_route = Path(new_route)
        duple = False
        if not new_route.exists():
            return f"Route ({new_route}) don't exist"
        for arch in new_route.glob("*"):
            if archive.name in str(arch):
               duple = True
        if archive.exists():
           if not duple:
               if not confirm:
                   if self._confirm(archive,"co","copy",new_route.name):
                       if return_name == "Archive":
                           shutil.copy(archive, new_route)
                           return f"{return_name} {archive_name} was copied in {new_route}"
                       else:
                           shutil.copytree(archive,new_route)
                           return f"{return_name} {archive_name} was copied in {new_route}"
                   else:
                       return f"{return_name} {archive_name} was not copied cause user decision:"
               else:
                   if return_name == "Archive":
                       shutil.copy(archive, new_route)
                       return f"{return_name} {archive_name} was copied in {new_route}"
                   else:
                       shutil.copytree(archive, new_route)
                       return f"{return_name} {archive_name} was copied in {new_route}"
           else:
               return self._duple(archive, "co", "copy", "copied", confirm,new_route)
        return f"{return_name} ({archive_name}) don't exist"
    #The func to delete archives
    def delete_(self,archive_name,confirm):
        archive = self.route / archive_name
        return_name = self._change(archive)
        if archive.exists():
           if not confirm:
               if self._confirm(archive,"de","delete",self.route.name):
                   if return_name == "Archive":
                       archive.unlink()
                       return f"{return_name} {archive.name} was deleted in {self.route}"
                   else:
                       archive.rmdir()
                       return f"{return_name} {archive.name} was deleted in {self.route}"
               if archive.suffix:
                   return f"{return_name} {archive.name} was not deleted cause user decision"
               else:
                   return f"{return_name} {archive.name} was not deleted cause user decision"
           else:
               if return_name == "Archive":
                   archive.unlink()
                   return f"{return_name} {archive.name} was deleted in {self.route}"
               else:
                   archive.rmdir()
                   return f"{return_name} {archive.name} was deleted in {self.route}"
        return f"{return_name} {archive.name} not exist in the specified route"
    #The func to rename archives
    def rename_(self,archive_name,new_name,confirm):
        name = self.route / archive_name
        return_name = self._change(name)
        if name.exists():
           news_name = self.route / (new_name + name.suffix)
           if not confirm:
               if self._confirm(name,"re","rename",self.route.name):
                   name.rename(news_name)
                   return f"{return_name} {name.name} was renamed to {news_name.name} in {self.route}"
               else:
                   return f"{return_name} {name.name} was not renamed cause user decision"
           else:
               name.rename(news_name)
               return f"{return_name} {name.name} was renamed to {news_name.name} in {self.route}"
        else:
           return f"{return_name} {name.name} don't exist"
    #show a window with the archives to see them more
    def view_(self,suffix):
       #win config
       win = tk.Tk()
       win.title(str(self.route))
       win.config(bg="black")
       win.geometry("500x500+770+0")
       win.attributes("-topmost", True)
       win.resizable(False, False)
       #tutorial text
       text = "Use ↑: For move selection Up\n\nUse ↓: For move selection Down\n\nUse Enter: For show the selected item info\n\nUse Esc: To close the program\n\nPress any key to continue"
       def _exit_tutorial():
           listbox.place(x=0, y=0)
           win.bind("<Up>", buttons)
           win.bind("<Down>", buttons)
           win.bind("<Escape>", buttons)
           win.bind("<Return>", buttons)
           win.bind("<Unmap>", states)
           win.bind("<Map>", states)
       tutorial_text = tk.Label(win,text=text,fg="white",bg="black",font=("Arial",18))
       #listbox
       listbox = tk.Listbox(win, selectmode="single",
                            width=43, height=20,
                            bg="black",
                            bd=10,
                            fg="white",
                            font=("Arial", 15),
                            selectbackground="gray",
                            selectforeground="purple"
       )


       #key detect & action
       def buttons(event):
           #move in the listbox
           selection = listbox.curselection()
           if selection:
               index = selection[0]
           else:
               index = -1
           if event.keysym == "Escape":
               win.destroy()
           elif event.keysym == "Up":
               listbox.selection_clear(0,tk.END)
               listbox.select_set(index - 1)
               listbox.see(index)
           elif event.keysym == "Down":
               listbox.selection_clear(0, tk.END)
               listbox.select_set(index + 1)
               listbox.see(index)
           elif event.keysym == "Return":
               get = ""
               try:
                   get = listbox.get(listbox.curselection())
               except tkinter.TclError:
                   pass
               def _sum_archives(route):
                   to = 0
                   for ar in route.rglob("*"):
                       if ar.is_file():
                           to += ar.stat().st_size
                   return to
               #get archive info
               info = "No for now ^_^"
               path = "No for now 0_<"
               size_text = "None for now.."
               for r in self.routes:
                   if r["name"] == get:
                       path = r["route"] / r["name"]
               #size get logic
               if listbox.curselection():
                   if path.suffix:
                       info = path.stat()
                       if info.st_size <= 999:
                           size_text = f"{info.st_size} bytes"
                       else:
                           size_text = f"{info.st_size / 1000:.2f} KB"
                   else:
                       info = path.stat()
                       total = _sum_archives(path)
                       if total < 1000:
                           size_text = f"{total} bytes"
                       elif total < 1_000_000:
                           size_text = f"{total / 1000:.2f} KB"
                       else:
                           size_text = f"{total / 1_000_000:.2f} MB"
               #-------------

               if get :
                   if self.win2 is not None and self.win2.winfo_exists(): #logic for just one window at time
                       self.win2.destroy()
                   #win2 config
                   self.win2 = tk.Toplevel(win)
                   self.win2.config(bg="black")
                   self.win2.attributes("-topmost", True)
                   self.win2.geometry(f"300x200+{win.winfo_x() - 350 if win.winfo_x() >= 350 else win.winfo_x() + 550}+{win.winfo_y() + 50 if win.winfo_y() <= 450 else win.winfo_y() - 180}")
                   self.win2.overrideredirect(True)
                   #borders
                   tk.Frame(self.win2,bg="gray",border=10,height=200,width=300).place(x=0,y=0)
                   tk.Frame(self.win2, bg="black", border=10, height=190, width=280).place(x=10,y=4)
                   #text
                   tk.Label(self.win2,text=f"NAME : {get}" if len(get) <= 22 else f"NAME : {get[0:15]}...",fg="white",bg="black",font=("Arial",13)).place(x=10,y=20)
                   tk.Label(self.win2, text=f"SIZE: {size_text}", fg="white", bg="black", font=("Arial", 13)).place(x=10, y=60)
                   tk.Label(self.win2, text=f"CREATED: {time.strftime("%m/%d/%Y at %H : %M",time.localtime(info.st_ctime))}", fg="white", bg="black", font=("Arial", 13)).place(x=10, y=80)
                   tk.Label(self.win2,text=f"MODIFIED: {time.strftime("%m/%d/%Y at %H : %M", time.localtime(info.st_mtime))}",fg="red", bg="black",height=3, font=("Arial", 13)).place(x=10, y=120)
                   self.get = path
       #win2 logic for minimize
       def states(event):
           state = win.state()
           try:
               if state == "iconic":
                   self.win2.withdraw()
               elif state == "normal":
                   self.win2.deiconify()
           except AttributeError:
               pass
       #detect buttons or events
       if not self.use:
           win.bind("<Up>",buttons)
           win.bind("<Down>",buttons)
           win.bind("<Escape>",buttons)
           win.bind("<Return>",buttons)
           win.bind("<Unmap>",states)
           win.bind("<Map>",states)
       #insert listbox
       for arch in self.route.rglob(f"*.{suffix}" if suffix != "*" else "*"):
           listbox.insert(tk.END,arch.name)
           self.routes.append({"route" : Path(arch.parent) , "name" : arch.name})
       if not self.routes:
           listbox.insert(tk.END, f"No item with the prefix {suffix} in {self.route}")
           listbox.config(state="disabled")

       #draw or place
       if not self.use:
           listbox.place(x=0,y=0)
       else:
           tutorial_text.place(x=20, y=100)
           win.bind("<Key>",lambda event: _exit_tutorial())
           win.bind("<Escape>",lambda event: win.destroy())

       #run
       win.mainloop()
       return f"Last item selected: {self.get}"