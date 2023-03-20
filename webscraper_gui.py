#####################################################
# File: webscraper_gui.py                           #
# Date: 03/11/2023                                  #
# Course: CS3141                                    #
# Author(s): Evan Vandermate (evanderm)             #
# Desc: Created the main webscrapper gui.           #
# Last Updated:                                     #
#       evanderm @ 03/11/2023 - Initial document    #
#####################################################
import tkinter as tk
from tkinter import ttk

# Web Scrapper GUI Main Class
class scrapperGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Initialize tkinter window
        tk.Tk.__init__(self, *args, **kwargs)

        # Setup window parameters
        self.title("Super Cool Wikipedia Webscraper with GUI and Also Has No Bugs (SCWWwGUIaAHNB)")
        #self.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))

        # Window callbacks
        self.protocol("WM_DELETE_WINDOW", self._quit)

        # Vars
        self.searchterm = tk.StringVar(value="Enter Search Term...")
        self.sortBySelection = tk.StringVar(value="Relevance")
        
        # Frames
        self.frm_searchTools    = tk.LabelFrame(master=self, text="Search Tools")
        self.frm_results        = tk.LabelFrame(master=self, text="Results")
        self.frm_searchTools.grid(row=0, column=0, sticky='news')
        self.frm_results.grid(row=0, column=1, sticky='news')
        
        # Widgets for "frm_searchTools" frame
        self.searchtermEntry        = tk.Entry(master=self.frm_searchTools, textvariable=self.searchterm,
                                               foreground='#c7c7cd')
        self.searchButton           = tk.Button(master=self.frm_searchTools, text="Search", command=self.search)
        self.sortBySelectionLabel   = tk.Label(master=self.frm_searchTools, text="Sort by:")
        self.sortBySelectionMenu    = ttk.Combobox(master=self.frm_searchTools, textvariable=self.sortBySelection,
                                                   values=["Relevance", "Date"], state='readonly')
        # Arrange widgets
        self.searchtermEntry.grid(row=0, column=0, sticky='news')
        self.searchButton.grid(row=0, column=1, sticky='nws')
        self.sortBySelectionLabel.grid(row=1, column=0, sticky='nes')
        self.sortBySelectionMenu.grid(row=1, column=1, sticky='news')
        # Widget callbacks
        self.searchtermEntry.bind("<FocusIn>", self.defaultText)

        # Widgets for "frm_results" frame
        self.resultsTree = ttk.Treeview(master=self.frm_results)
        # Arrange widgets
        self.resultsTree.grid(row=0, column=0, sticky='news')

        # Initialize main-loops
        self.after(0, func=lambda: self.main())
        self.mainloop()

    #################################################
    # main()                                        #
    #-----------------------------------------------#
    # The main loop for the window.                 #
    # All tasks here will run every frame update.   #
    #################################################
    def main(self):
        # TODO: Tasks to update periodically (not implemented yet)

        # Loop
        self.update_idletasks()
        self.after(0, func=lambda: self.main())

    #############################################
    # search()                                  #
    #-------------------------------------------#
    # Callback for searchButton.                #
    # Execute webscrapping for entered term.    #
    #############################################
    def search(self):
        # TODO: implement search function
        print(f"Search for [{self.searchterm.get()}]")

    #########################################
    # defaultText()                         #
    #---------------------------------------#
    # Callback for searchTermEntry widget.  #
    # Clears the placeholder text.          #
    #########################################
    def defaultText(self, args):
        self.searchterm.set("")
        self.searchtermEntry.configure(foreground='black')

    #####################################################
    # _quit()                                           #
    #---------------------------------------------------#
    # Callback for window close command ('X' button).   #
    # Destroys the main window.                         #
    #####################################################
    def _quit(self):
        self.destroy()

if __name__ == "__main__":
    scrapper = scrapperGUI()