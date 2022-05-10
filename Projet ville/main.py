# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import lib.random as ra

class Main():
    def __init__(self):
        """Initialisation the main window. """
        
        self.window = Tk()
        self.window.iconbitmap("img/logo/logo.ico")
        self.lang_config = "en"
        self.color_config = "light"
        
        self.padx, self.pady = 10, 10
        
        self.initialise()
            
            
    def initialise(self):
        '''Create all the settings variables.'''
        
        #Open the file with the translation for the all the text.
        with open("translation/" + str(self.lang_config),"r", encoding='utf-8')as fichier:
            self.settings = eval(fichier.read())
            
        #Open the file with the color panel for the map and the window.
        with open("color/" + str(self.color_config), "r", encoding="utf-8") as fichier:
            self.color= eval(fichier.read())
            
        
        #Settings for the main window.
        self.window.title(self.settings["settings_window_name"])
        self.window["bg"] = self.color["settings_bg"]
        
        self.main_frame = Frame(self.window, padx=self.padx, pady=self.pady, bg=self.color["settings_bg"])
        self.second_frame = Frame(self.window, padx=self.padx, pady=self.pady, bg=self.color["settings_bg"])
        
        #-------------------- Size of window for the map --------------------
        self.window_size = LabelFrame(self.main_frame, text=self.settings["window_size"], padx=self.padx, pady=self.pady, bg=self.color["settings_bg"])
        
        #Height window
        self.t_window_h = Label(self.window_size, text = self.settings["window_height"] + ': ', padx=self.padx, pady=self.pady, bg = self.color["settings_bg"])
        self.v_window_h = IntVar()
        self.v_window_h.set(500)
        self.window_h = Entry(self.window_size, textvariable=self.v_window_h, width = 9)
        
        #Width window
        self.t_window_w = Label(self.window_size, text = self.settings["window_width"] + ': ', padx=self.padx, pady=self.pady, bg = self.color["settings_bg"])
        self.v_window_w = IntVar()
        self.v_window_w.set(800)
        self.window_w = Entry(self.window_size, textvariable=self.v_window_w, width = 9)
        
        #-------------------- Size of the map --------------------
        self.map_size = LabelFrame(self.main_frame, text=self.settings["map_size"], padx=self.padx, pady=self.pady, bg=self.color["settings_bg"])
        
        #Height map
        self.t_map_h = Label(self.map_size, text = self.settings["map_height"] + ': ', padx=self.padx, pady=self.pady, bg = self.color["settings_bg"])
        self.v_map_h = IntVar()
        self.v_map_h.set(500)
        self.map_h = Entry(self.map_size, textvariable=self.v_map_h, width = 9)
        
        #Width map
        self.t_map_w = Label(self.map_size, text = self.settings["map_width"] + ': ', padx=self.padx, pady=self.pady, bg = self.color["settings_bg"])
        self.v_map_w = IntVar()
        self.v_map_w.set(800)
        self.map_w = Entry(self.map_size, textvariable=self.v_map_w, width = 9)
        
        #-------------------- Color frame --------------------
        self.color_frame = LabelFrame(self.second_frame, text=self.settings["color_frame_name"], padx=self.padx, pady=self.pady, bg=self.color["settings_bg"])
        
        #Select color pannel
        self.t_color_panel = Label(self.color_frame, text = self.settings["chose_color"] + ': ', padx=self.padx, pady=self.pady, bg = self.color["settings_bg"])
        self.color_panel = ttk.Combobox(self.color_frame, values=[self.settings["chose_color_0"], self.settings["chose_color_1"]], state="readonly")
        self.color_panel.current(self.current_color())
        self.color_panel.bind("<<ComboboxSelected>>", self.forget)
        
        #-------------------- language frame --------------------
        self.lang_frame = LabelFrame(self.second_frame, text=self.settings["lang_frame_name"], padx=self.padx, pady=self.pady, bg=self.color["settings_bg"])
        
        #Select the language
        self.t_language = Label(self.lang_frame, text=self.settings["language"] + ': ', padx=self.padx, pady=self.pady, bg = self.color["settings_bg"])
        self.language = ttk.Combobox(self.lang_frame, values=["Français", "English", "Русский"], state="readonly")
        self.language.current(self.current_lang())
        self.language.bind("<<ComboboxSelected>>", self.forget)
        
        
    def current_lang(self):
        #Return the language for the window
        if self.lang_config == "fr":
            return 0
        elif self.lang_config == "en":
            return 1
        elif self.lang_config == "ru":
            return 2
        
    def current_color(self):
        #Return the color of the window
        if self.color_config == "light":
            return 0
        elif self.color_config == "dark":
            return 1

        
    def show(self):
        """Draw all component on the different frame."""
        
        self.main_frame.grid(row = 0, column = 0)
        self.second_frame.grid(row = 1, column = 0)
        
        self.map_size.grid(row = 0, column = 0, sticky = W, padx = self.padx, pady = self.pady)
        self.t_map_h.grid(row = 1, column = 0, sticky = W)
        self.map_h.grid(row = 1, column = 1)
        self.t_map_w.grid(row = 0, column = 0, sticky = W)
        self.map_w.grid(row = 0, column = 1)
        
        self.window_size.grid(row = 0, column = 1, sticky = W, padx = self.padx, pady = self.pady)
        self.t_window_h.grid(row = 1, column = 0, sticky = W)
        self.window_h.grid(row = 1, column = 1)
        self.t_window_w.grid(row = 0, column = 0, sticky = W)
        self.window_w.grid(row = 0, column = 1)
        
        self.color_frame.grid(row = 1, column = 0, sticky = W, padx = self.padx, pady = self.pady)
        self.t_color_panel.grid(row = 0, column = 0, sticky = W)
        self.color_panel.grid(row = 0, column = 1)
        
        self.lang_frame.grid(row = 2, column = 0, sticky = W, padx = self.padx, pady = self.pady)
        self.t_language.grid(row = 0, column = 0, sticky = W)
        self.language.grid(row = 0, column = 1)
        
    def forget(self, a):
        '''Undraw all text for change the language.'''
        
        lang = self.language.get()
        if lang == "Français":
            self.lang_config = "fr"
        elif lang == "English":
            self.lang_config = "en"
        elif lang == "Русский":
            self.lang_config = "ru"
            
        color = self.color_panel.get()
        if color == "light":
            self.color_config = "light"
        elif color == "dark":
            self.color_config = "dark"
            
        self.main_frame.grid_forget()
        self.second_frame.grid_forget()
        
        self.initialise()
        self.show()
        
   

    def update(self):
        """Update the screen, redraw all sprites. """
        
        self.show()
        self.window.update()
    
    def create_map(self):
        """ Call the fonction for create the main frame."""
        
        import lib.turtle            
        from random_density import Generate_town
        
        #for initialise the random generator
        seed = ra.randint(10000,99999)
        
        #Create the dict with all settings
        self.settings = {
            "width" : int(self.width.get()),\
            "height" : int(self.height.get()),\
            "widtmap_h" : int(self.map_w.get()),\
            "height_map" : int(self.map_h.get()),\
            "size_chunk" : int(self.s_chunk.get()),\
            "seed" : int(self.seed.get()),\
            "color_bg" : eval(self.c_bg.get()),\
            "color_house" : eval(self.c_house.get()),\
            "color_road" : eval(self.c_road.get()),\
            "color_line" : self.c_line.get(),\
            "color_text" : self.c_text.get(),\
            "size_road" : int(self.s_road.get()),\
            "size_line" : int(self.s_line.get()),\
            "show_noise" : self.v_s_perlin.get(),\
            "debug_mode" : self.debug_mode.get(),\
            "octaves" : self.octaves.get(),\
            "chose_color" : self.chose_color,\
            "save" : int(self.v_save.get())
            }
        
        #Call the class Generate_town for draw the map
        self.dramap_w = Generate_town(self.settings)

#Initialise the object Main()
main = Main()
run = True 

while run:
    #update the screen while True
    main.update()
    
    