# -*- coding: utf-8 -*-
'''
Projet Cartographie de la plannet et de ses territoires CPT

Développeurs :  Sasha Wlodaarczyk
                Andrew Carey
                Artiom Filatov

'''

from tkinter import *
from tkinter import ttk
import lib.random as ra


def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """

    return str('#%02x%02x%02x' % eval(rgb))


class Main:
    def __init__(self):
        """Initialised of the window"""

        self.window = Tk()
        self.window.iconbitmap("img/logo/logo.ico")  # logo of the window
        self.lang_config = "en"  # default language
        self.color_config = "0"  # default theme

        self.padx, self.pady = 10, 10
        self.advanced_p = False

        self.initialise()

    def initialise(self):
        """Initiate all variable and text for the window. """

        # Open the file with the translation for the all the text.
        with open("translation/" + str(self.lang_config), "r", encoding='utf-8') as fichier:
            self.settings = eval(fichier.read())

        # Open the file with the color panel for the map and the window.
        with open("color/" + str(self.color_config), "r", encoding="utf-8") as fichier:
            self.color = eval(fichier.read())

        # Settings for the main window.
        self.window.title(self.settings["settings_window_name"])
        self.window.configure(bg=from_rgb(self.color["settings_bg"]))

        self.principal = Frame(self.window, padx=self.padx, pady=self.pady, bg=from_rgb(self.color["settings_bg"]))

        self.main_frame = Frame(self.principal, padx=self.padx, pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.second_frame = Frame(self.principal, padx=self.padx, pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.third_frame = Frame(self.principal, padx=self.padx, pady=self.pady, bg=from_rgb(self.color["settings_bg"]))

        # -------------------- Size of window for the map --------------------
        self.window_size = LabelFrame(self.main_frame, text=self.settings["window_size"], padx=self.padx,
                                      pady=self.pady, bg=from_rgb(self.color["settings_bg"]))

        # Height window
        self.t_window_h = Label(self.window_size, text=self.settings["window_height"] + ': ', padx=self.padx,
                                pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.v_window_h = IntVar()
        self.v_window_h.set(500)
        self.window_h = Entry(self.window_size, textvariable=self.v_window_h, width=9)

        # Width window
        self.t_window_w = Label(self.window_size, text=self.settings["window_width"] + ': ', padx=self.padx,
                                pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.v_window_w = IntVar()
        self.v_window_w.set(800)
        self.window_w = Entry(self.window_size, textvariable=self.v_window_w, width=9)

        # -------------------- Size of the map --------------------
        self.map_size = LabelFrame(self.main_frame, text=self.settings["map_size"], padx=self.padx, pady=self.pady,
                                   bg=from_rgb(self.color["settings_bg"]))

        # Height map
        self.t_map_h = Label(self.map_size, text=self.settings["map_height"] + ': ', padx=self.padx, pady=self.pady,
                             bg=from_rgb(self.color["settings_bg"]))
        self.v_map_h = IntVar()
        self.v_map_h.set(500)
        self.map_h = Entry(self.map_size, textvariable=self.v_map_h, width=9)

        # Width map
        self.t_map_w = Label(self.map_size, text=self.settings["map_width"] + ': ', padx=self.padx, pady=self.pady,
                             bg=from_rgb(self.color["settings_bg"]))
        self.v_map_w = IntVar()
        self.v_map_w.set(800)
        self.map_w = Entry(self.map_size, textvariable=self.v_map_w, width=9)

        # -------------------- Color frame --------------------
        self.color_frame_p = LabelFrame(self.second_frame, text=self.settings["color_frame_name"], padx=self.padx,
                                      pady=self.pady, bg=from_rgb(self.color["settings_bg"]))

        # Select color pannel
        self.t_color_panel = Label(self.color_frame_p, text=self.settings["chose_color"] + ': ', padx=self.padx,
                                   pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.color_panel = ttk.Combobox(self.color_frame_p,
                                        values=[self.settings["chose_color_0"], self.settings["chose_color_1"]],
                                        state="readonly")
        self.color_panel.current(self.current_color())
        self.color_panel.bind("<<ComboboxSelected>>", self.forget)

        # -------------------- Language frame --------------------
        self.lang_frame = LabelFrame(self.second_frame, text=self.settings["lang_frame_name"], padx=self.padx,
                                     pady=self.pady, bg=from_rgb(self.color["settings_bg"]))

        # Select the language
        self.t_language = Label(self.lang_frame, text=self.settings["language"] + ': ', padx=self.padx, pady=self.pady,
                                bg=from_rgb(self.color["settings_bg"]))
        self.language = ttk.Combobox(self.lang_frame, values=["Français", "English"], state="readonly")
        self.language.current(self.current_lang())
        self.language.bind("<<ComboboxSelected>>", self.forget)

        self.advanced_frame = LabelFrame(self.window, text=self.settings["main_frame_name"], padx=self.padx,
                                         pady=self.pady,
                                         bg=from_rgb(self.color["settings_bg"]))

        # color
        self.color_frame = LabelFrame(self.advanced_frame, text=self.settings["color_frame_name"] + ":", padx=self.padx,
                                      pady=self.pady, bg=from_rgb(self.color["settings_bg"]))

        self.t_c_line = Label(self.color_frame, text=self.settings["color_lane_marking"] + ': ', padx=self.padx,
                              pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.v_c_line = StringVar()
        self.v_c_line.set(self.color["line"])
        self.c_line = Entry(self.color_frame, textvariable=self.v_c_line, width=9)

        self.t_c_road = Label(self.color_frame, text=self.settings["color_road"] + ': ', padx=self.padx, pady=self.pady,
                              bg=from_rgb(self.color["settings_bg"]))
        self.v_c_road = StringVar()
        self.v_c_road.set(self.color["road"])
        self.c_road = Entry(self.color_frame, textvariable=self.v_c_road, width=9)

        self.t_c_text = Label(self.color_frame, text=self.settings["color_text"] + ': ', padx=self.padx, pady=self.pady,
                              bg=from_rgb(self.color["settings_bg"]))
        self.v_c_text = StringVar()
        self.v_c_text.set(self.color["text"])
        self.c_text = Entry(self.color_frame, textvariable=self.v_c_text, width=9)

        self.t_c_house = Label(self.color_frame, text=self.settings["color_house"] + ': ', padx=self.padx,
                               pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.v_c_house = StringVar()
        self.v_c_house.set(self.color["house"])
        self.c_house = Entry(self.color_frame, textvariable=self.v_c_house, width=9)

        self.t_c_garden = Label(self.color_frame, text=self.settings["color_garden"] + ': ', padx=self.padx,
                                pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.v_c_garden = StringVar()
        self.v_c_garden.set(self.color["garden"])
        self.c_garden = Entry(self.color_frame, textvariable=self.v_c_garden, width=9)

        self.t_c_bg = Label(self.color_frame, text=self.settings["color_background"] + ': ', padx=self.padx,
                            pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.v_c_bg = StringVar()
        self.v_c_bg.set(self.color["bg"])
        self.c_bg = Entry(self.color_frame, textvariable=self.v_c_bg, width=9)

        # size
        self.size_frame = LabelFrame(self.advanced_frame, text=self.settings["size_frame_name"] + ":", padx=self.padx,
                                     pady=self.pady, bg=from_rgb(self.color["settings_bg"]))

        self.t_s_line = Label(self.size_frame, text=self.settings["size_lane_marking"] + ': ', padx=self.padx,
                              pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.v_s_line = IntVar()
        self.v_s_line.set(2)
        self.s_line = Entry(self.size_frame, textvariable=self.v_s_line, width=9)

        self.t_s_road = Label(self.size_frame, text=self.settings["size_road"] + ': ', padx=self.padx, pady=self.pady,
                              bg=from_rgb(self.color["settings_bg"]))
        self.v_s_road = IntVar()
        self.v_s_road.set(6)
        self.s_road = Entry(self.size_frame, textvariable=self.v_s_road, width=9)

        self.t_s_text = Label(self.size_frame, text=self.settings["size_text"] + ': ', padx=self.padx, pady=self.pady,
                              bg=from_rgb(self.color["settings_bg"]))
        self.v_s_text = IntVar()
        self.v_s_text.set(40)
        self.s_text = Entry(self.size_frame, textvariable=self.v_s_road, width=9)

        self.t_s_chunk = Label(self.size_frame, text=self.settings["size_chunk"] + ': ', padx=self.padx, pady=self.pady,
                               bg=from_rgb(self.color["settings_bg"]))
        self.v_s_chunk = IntVar()
        self.v_s_chunk.set(50)
        self.s_chunk = Entry(self.size_frame, textvariable=self.v_s_chunk, width=9)

        # other
        self.seed_frame = LabelFrame(self.advanced_frame, text=self.settings["advanced_settings_frame_name"] + ":",
                                     padx=self.padx, pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.abc = Label(self.seed_frame, text='                ', bg=from_rgb(self.color["settings_bg"]))

        self.t_seed = Label(self.seed_frame, text=self.settings["seed_key"], padx=self.padx, pady=self.pady,
                            bg=from_rgb(self.color["settings_bg"]))
        self.v_seed = IntVar()
        self.v_seed.set(ra.randint(100000000, 9999999999))
        self.seed = Entry(self.seed_frame, textvariable=self.v_seed, width=14)


        self.v_s_perlin = IntVar()
        self.t_s_perlin = Label(self.seed_frame, text=self.settings["show_perlin_noise"] + ': ', padx=self.padx,
                                pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.c_s_perlin = Checkbutton(self.seed_frame, text="", variable=self.v_s_perlin, bd=0, \
                                      onvalue=1, offvalue=0, padx=self.padx, pady=self.pady,
                                      bg=from_rgb(self.color["settings_bg"]))

        self.t_debug_mode = Label(self.seed_frame, text=self.settings["debug_mode"] + ': ', padx=self.padx,
                                  pady=self.pady, bg=from_rgb(self.color["settings_bg"]))
        self.debug_mode = IntVar()
        self.c_debug_mode = Checkbutton(self.seed_frame, text="", variable=self.debug_mode, bd=0, \
                                        onvalue=1, offvalue=0, padx=self.padx, pady=self.pady,
                                        bg=from_rgb(self.color["settings_bg"]))

        self.t_octaves = Label(self.seed_frame, text=self.settings["octaves"] + ': ', padx=self.padx, pady=self.pady,
                               bg=from_rgb(self.color["settings_bg"]))
        self.v_octaves = IntVar()
        self.v_octaves.set(2)
        self.octaves = Entry(self.seed_frame, textvariable=self.v_octaves, width=9)

        self.advanced_bt = Button(self.third_frame, text=self.settings["advanced_settings"], bg=from_rgb(self.color["settings_bg"]),
                                  highlightthickness=0, bd=0, fg="darkblue", font="Verdana 8 underline",
                                  command=self.advanced, padx=self.padx, pady=self.pady)

        self.button = Button(self.third_frame, text=self.settings["draw"], command=self.create_map)


    def current_lang(self):
        # Return the language for the window
        if self.lang_config == "fr":
            return 0
        elif self.lang_config == "en":
            return 1
        elif self.lang_config == "ru":
            return 2

    def current_color(self):
        # Return the color of the window
        if self.color_config == "0":
            return 0
        elif self.color_config == "1":
            return 1

    def show(self):
        """Draw all component on the different frame."""

        self.principal.grid(row=0, column=0)
        self.main_frame.grid(row=0, column=0)
        self.second_frame.grid(row=1, column=0)
        self.third_frame.grid(row=2, column=0)

        self.map_size.grid(row=0, column=0, sticky=W, padx=self.padx, pady=self.pady)
        self.t_map_h.grid(row=1, column=0, sticky=W)
        self.map_h.grid(row=1, column=1)
        self.t_map_w.grid(row=0, column=0, sticky=W)
        self.map_w.grid(row=0, column=1)

        self.window_size.grid(row=0, column=1, sticky=W, padx=self.padx, pady=self.pady)
        self.t_window_h.grid(row=1, column=0, sticky=W)
        self.window_h.grid(row=1, column=1)
        self.t_window_w.grid(row=0, column=0, sticky=W)
        self.window_w.grid(row=0, column=1)

        self.color_frame_p.grid(row=1, column=0, sticky=W, padx=self.padx, pady=self.pady)
        self.t_color_panel.grid(row=0, column=0, sticky=W)
        self.color_panel.grid(row=0, column=1)

        self.lang_frame.grid(row=2, column=0, sticky=W, padx=self.padx, pady=self.pady)
        self.t_language.grid(row=0, column=0, sticky=W)
        self.language.grid(row=0, column=1)

        self.advanced_bt.grid(row=0, column=0, sticky=E)
        self.button.grid(row=1, column=0)

        if self.advanced_p:

            self.advanced_frame.grid(row=0, column=3)

            # color
            self.color_frame.grid(row=0, column=0, sticky=W, padx=self.padx, pady=self.pady)
            self.t_c_line.grid(row=0, column=0, sticky=W)
            self.c_line.grid(row=0, column=1)
            self.t_c_road.grid(row=1, column=0, sticky=W)
            self.c_road.grid(row=1, column=1)
            self.t_c_text.grid(row=2, column=0, sticky=W)
            self.c_text.grid(row=2, column=1)
            self.t_c_house.grid(row=3, column=0, sticky=W)
            self.c_house.grid(row=3, column=1)
            self.t_c_garden.grid(row=3, column=0, sticky=W)
            self.c_garden.grid(row=3, column=1)
            self.t_c_house.grid(row=4, column=0, sticky=W)
            self.c_house.grid(row=4, column=1)
            self.t_c_bg.grid(row=5, column=0, sticky=W)
            self.c_bg.grid(row=5, column=1)


            # size
            self.size_frame.grid(row=1, column=0, padx=self.padx, pady=self.pady)
            self.t_s_line.grid(row=0, column=0, sticky=W)
            self.s_line.grid(row=0, column=1)
            self.t_s_road.grid(row=1, column=0, sticky=W)
            self.s_road.grid(row=1, column=1)
            self.t_s_text.grid(row=2, column=0, sticky=W)
            self.s_text.grid(row=2, column=1)
            self.t_s_chunk.grid(row=3, column=0, sticky=W)
            self.s_chunk.grid(row=3, column=1)

            # other
            self.seed_frame.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky=W)
            self.t_seed.grid(row=0, column=0, sticky=W)
            self.seed.grid(row=0, column=1)
            self.t_s_perlin.grid(row=1, column=0, sticky=W)
            self.c_s_perlin.grid(row=1, column=1)
            self.t_debug_mode.grid(row=2, column=0, sticky=W)
            self.c_debug_mode.grid(row=2, column=1)
            self.t_octaves.grid(row=3, column=0, sticky=W)
            self.octaves.grid(row=3, column=1)

    def advanced(self):

        print("Change")
        self.advanced_p = not self.advanced_p

        if not self.advanced_p:
            self.advanced_forget()

        self.update()

    def advanced_forget(self):

        lang = self.language.get()
        if lang == "Français":
            self.lang_config = "fr"
        elif lang == "English":
            self.lang_config = "en"

        self.advanced_frame.grid_forget()

        self.update()

    def forget(self, a):
        """Underway all text for change the language."""

        lang = self.language.get()
        if lang == "Français":
            self.lang_config = "fr"
        elif lang == "English":
            self.lang_config = "en"
        elif lang == "Русский":
            self.lang_config = "ru"

        color = self.color_panel.get()
        if color == self.settings["chose_color_0"]:
            self.color_config = "0"
        elif color == self.settings["chose_color_1"]:
            self.color_config = "1"

        self.advanced_forget()
        self.principal.grid_forget()

        self.initialise()
        self.show()

    def update(self):
        """Update the screen, redraw all sprites. """

        self.show()
        self.window.update()

    def create_map(self):
        """ Call the function for create the main frame."""

        import lib.turtle
        from random_density import Generate_town

        # for initialise the random generator
        seed = ra.randint(10000, 99999)

        # Create the dict with all settings
        self.variables = {
            "width": int(self.window_w.get()), \
            "height": int(self.window_h.get()), \
            "width_map": int(self.map_w.get()), \
            "height_map": int(self.map_h.get()), \
            "size_chunk": int(self.s_chunk.get()), \
            "seed": int(self.seed.get()), \
            "color_bg": eval(self.c_bg.get()), \
            "color_house": eval(self.c_house.get()), \
            "color_road": eval(self.c_road.get()), \
            "color_line": eval(self.c_line.get()), \
            "color_text": eval(self.c_text.get()), \
            "color_garden": eval(self.c_garden.get()),\
            "size_road": int(self.s_road.get()), \
            "size_line": int(self.s_line.get()), \
            "size_text" : int(self.s_text.get()),\
            "show_noise": self.v_s_perlin.get(), \
            "debug_mode": self.debug_mode.get(), \
            "octaves": self.octaves.get(), \

            }
        print(self.debug_mode)

        if not self.advanced_p:
            self.variables["seed"] = ra.randint(100000000, 9999999999)

        # Call the class Generate_town for draw the map
        self.dramap_w = Generate_town(self.variables)


# Initialise the object Main()
main = Main()
run = True

while run:
    # update the screen while True
    main.update()
