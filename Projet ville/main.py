# -*- coding: utf-8 -*-

from lib.tkinter import *
from lib.tkinter import ttk
import lib.random as ra

class Main():
    def __init__(self):
        """Initialisation the main window. """
        
        self.window = Tk()
        self.window.iconbitmap("img/logo/logo.ico")
        self.lang_config = "en"
        self.setting()
            
            
    def setting(self):
        '''Create all the settings variables.'''
        
        #Open the file with the translation for the all the text
        with open("translation/" + str(self.lang_config),"r", encoding='utf-8')as fichier:
            self.settings = eval(fichier.read())
            
        #Settings of the settings window
        self.window.title(self.settings["settings_window_name"])
        self.color = "grey"
        self.padx, self.pady = 10, 10
        self.window['bg'] = self.color
        self.main_frame = LabelFrame(self.window, text=self.settings["main_frame_name"], padx=self.padx, pady=self.pady, bg = self.color)
      
        #Settings of the colors
        self.color_frame = LabelFrame(self.main_frame, text = self.settings["color_frame_name"] + ":", padx=self.padx, pady=self.pady, bg = self.color)
        
        self.t_c_line = Label(self.color_frame, text = self.settings["color_lane_marking"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_c_line = StringVar()
        self.v_c_line.set("yellow")
        self.c_line = Entry(self.color_frame, textvariable=self.v_c_line, width = 9)
        
        self.t_c_road = Label(self.color_frame, text = self.settings["color_road"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_c_road = StringVar()
        self.v_c_road.set("(253,226,147)")
        self.c_road = Entry(self.color_frame, textvariable=self.v_c_road, width = 9)
        
        self.t_c_text = Label(self.color_frame, text = self.settings["color_text"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_c_text = StringVar()
        self.v_c_text.set("darkred")
        self.c_text = Entry(self.color_frame, textvariable=self.v_c_text, width = 9)
                
        self.t_c_house = Label(self.color_frame, text = self.settings["color_house"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_c_house = StringVar()
        self.v_c_house.set("(212,213,215)")
        self.c_house = Entry(self.color_frame, textvariable=self.v_c_house, width = 9)
        
        self.t_c_bg = Label(self.color_frame, text = self.settings["color_background"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_c_bg = StringVar()
        self.v_c_bg.set("(248,249,250)")
        self.c_bg = Entry(self.color_frame, textvariable=self.v_c_bg, width = 9)
        
        #Settings of the size
        self.size_frame = LabelFrame(self.main_frame, text = self.settings["size_frame_name"] + ":", padx=self.padx, pady=self.pady, bg = self.color)
        
        self.t_s_line = Label(self.size_frame, text = self.settings["size_lane_marking"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_s_line = IntVar()
        self.v_s_line.set(2)
        self.s_line = Entry(self.size_frame, textvariable=self.v_s_line, width = 9)
        
        self.t_s_road = Label(self.size_frame, text = self.settings["size_road"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_s_road = IntVar()
        self.v_s_road.set(6)
        self.s_road = Entry(self.size_frame, textvariable=self.v_s_road, width = 9)
        
        self.t_width = Label(self.size_frame, text = self.settings["width_map"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_width = IntVar()
        self.v_width.set(1000)
        self.width = Entry(self.size_frame, textvariable=self.v_width, width = 9)
        
        self.t_height = Label(self.size_frame, text = self.settings["height_map"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_height = IntVar()
        self.v_height.set(1000)
        self.height = Entry(self.size_frame, textvariable=self.v_height, width = 9)
        
        #Other settings
        self.seed_frame = LabelFrame(self.window, text = self.settings["advanced_settings_frame_name"] + ":", padx=self.padx, pady=self.pady, bg = self.color)
        self.abc = Label(self.seed_frame, text = '                ', bg = self.color)
        
        self.t_seed = Label(self.seed_frame, text = self.settings["seed_key"], padx=self.padx, pady=self.pady, bg = self.color)
        self.v_seed = IntVar()
        self.v_seed.set(ra.randint(100000000,9999999999))
        self.seed = Entry(self.seed_frame, textvariable=self.v_seed, width = 14)
        
        self.t_s_chunk = Label(self.seed_frame, text = self.settings["size_chunk"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_s_chunk = IntVar()
        self.v_s_chunk.set(50)
        self.s_chunk = Entry(self.seed_frame, textvariable=self.v_s_chunk, width = 9)
        
        self.t_h_map = Label(self.seed_frame, text = self.settings["height"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_h_map = IntVar()
        self.v_h_map.set(500)
        self.h_map = Entry(self.seed_frame, textvariable=self.v_h_map, width = 9)
        
        self.t_w_map = Label(self.seed_frame, text = self.settings["width"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_w_map = IntVar()
        self.v_w_map.set(800)
        self.w_map = Entry(self.seed_frame, textvariable=self.v_w_map, width = 9)
        
        self.t_language = Label(self.seed_frame, text = self.settings["language"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.language = ttk.Combobox(self.seed_frame, values=["Français", "English", "Русский"], state="readonly")
        self.language.current(self.current_lang())
        self.language.bind("<<ComboboxSelected>>", self.forget)


        self.v_s_perlin = IntVar()
        self.t_s_perlin = Label(self.seed_frame, text = self.settings["show_perlin_noise"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.c_s_perlin = Checkbutton(self.seed_frame, text = "", variable = self.v_s_perlin, bd = 0, \
                 onvalue = 1, offvalue = 0, padx=self.padx, pady=self.pady, bg = self.color)
        
        self.v_save = IntVar()
        self.t_save = Label(self.seed_frame, text = self.settings["save"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.c_save = Checkbutton(self.seed_frame, text = "", variable = self.v_save, bd = 0, \
                 onvalue = 1, offvalue = 0, padx=self.padx, pady=self.pady, bg = self.color)
        
        
        self.debug_mode = IntVar()
        self.t_debug_mode = Label(self.seed_frame, text = self.settings["debug_mode"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.c_debug_mode = Checkbutton(self.seed_frame, text = "", variable = self.debug_mode, bd = 0, \
                 onvalue = 1, offvalue = 0, padx=self.padx, pady=self.pady, bg = self.color)
        
        self.t_octaves = Label(self.seed_frame, text = self.settings["octaves"] + ': ', padx=self.padx, pady=self.pady, bg = self.color)
        self.v_octaves = IntVar()
        self.v_octaves.set(2)
        self.octaves = Entry(self.seed_frame, textvariable=self.v_octaves, width = 9)
        
        self.button = Button(self.seed_frame, text = self.settings["drawn"], command = self.create_map)
        
        self.settings = {}
        
        
    def current_lang(self):
        #Return the language for the window
        if self.lang_config == "fr":
            return 0
        elif self.lang_config == "en":
            return 1
        elif self.lang_config == "ru":
            return 2
        
    def show(self):
        """Draw all component on the different frame."""

        self.main_frame.grid(row = 0, column = 0)
        
        #Draw settings for the color
        self.color_frame.grid(row = 0, column = 0, sticky = W, padx = self.padx, pady = self.pady)
        self.t_c_line.grid(row = 0, column = 0, sticky = W)
        self.c_line.grid(row = 0, column = 1)
        self.t_c_road.grid(row = 1, column = 0, sticky = W)
        self.c_road.grid(row = 1, column = 1) 
        self.t_c_text.grid(row = 2, column = 0, sticky = W)
        self.c_text.grid(row = 2, column = 1)  
        self.t_c_house.grid(row = 3,column = 0, sticky = W)
        self.c_house.grid(row = 3, column = 1)  
         
        #Draw settings for the size
        self.size_frame.grid(row = 0, column = 1, padx = self.padx, pady = self.pady)
        self.t_width.grid(row = 0, column = 0, sticky = W)
        self.width.grid(row = 0, column = 1)
        self.t_height.grid(row = 1, column = 0, sticky = W)
        self.height.grid(row = 1, column = 1)
        self.t_s_line.grid(row = 2, column = 0, sticky = W)
        self.s_line.grid(row = 2, column = 1)
        self.t_s_road.grid(row = 3, column = 0, sticky = W)
        self.s_road.grid(row = 3, column = 1)
        
        #Draw the other settings
        self.seed_frame.grid(row = 1, column = 0, padx = self.padx, pady = self.pady, sticky = W)
        self.t_seed.grid(row = 0, column = 0, sticky = W)
        self.seed.grid(row = 0, column = 1)
        self.t_s_chunk.grid(row = 1, column = 0, sticky = W)
        self.s_chunk.grid(row = 1, column = 1)
        self.t_h_map.grid(row = 3, column = 0, sticky = W)
        self.h_map.grid(row = 3, column = 1)
        self.t_w_map.grid(row = 2, column = 0, sticky = W)
        self.w_map.grid(row = 2, column = 1)
        self.t_s_perlin.grid(row = 4, column = 0, sticky = W)
        self.c_s_perlin.grid(row = 4, column = 1)
        self.t_save.grid(row = 5, column = 0, sticky = W)
        self.c_save.grid(row = 5, column = 1)
        self.t_language.grid(row = 6, column = 0, sticky = W)
        self.language.grid(row = 6, column = 1)
        self.t_debug_mode.grid(row = 7, column = 0, sticky = W)
        self.c_debug_mode.grid(row = 7, column = 1)
        self.t_octaves.grid(row = 8, column = 0, sticky = W)
        self.octaves.grid(row = 8, column = 1)
       
        #Draw the button
        self.button.grid(row = 3, column = 6)
        
        
    def forget(self, a):
        '''Undraw all text for change the language.'''
        
        lang = self.language.get()
        if lang == "Français":
            self.lang_config = "fr"
        elif lang == "English":
            self.lang_config = "en"
        elif lang == "Русский":
            self.lang_config = "ru"
        
        self.main_frame.grid_forget()
        
        #color
        self.color_frame.grid_forget()
        self.t_c_line.grid_forget()
        self.t_c_road.grid_forget()
        self.t_c_text.grid_forget()
        self.t_c_house.grid_forget()
         
        #size
        self.size_frame.grid_forget()
        self.t_width.grid_forget()
        self.t_height.grid_forget()
        self.t_s_line.grid_forget()
        self.t_s_road.grid_forget()
        
        #other
        self.seed_frame.grid_forget()
        self.t_seed.grid_forget()
        self.t_s_chunk.grid_forget()
        self.t_h_map.grid_forget()
        self.t_w_map.grid_forget()
        self.t_s_perlin.grid_forget()
        self.t_save.grid_forget()
        self.t_language.grid_forget()
        self.t_debug_mode.grid_forget()
        self.t_octaves.grid_forget()

        #button
        self.button.grid_forget()
        
        self.setting()
        self.update()
        

    def update(self):
        """Update the screen, redraw all sprites. """
        
        self.show()
        self.window.update()
        
        self.lang_config= self.language.get()
        self.setting
    
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
            "width_map" : int(self.w_map.get()),\
            "height_map" : int(self.h_map.get()),\
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
            "save" : int(self.v_save.get())
            }
        
        #Call the class Generate_town for draw the map
        self.draw_map = Generate_town(self.settings)

#Initialise the object Main()
main = Main()
run = True 

while run:
    #update the screen while True
    main.update()
    