#!/usr/bin/env python3
#############################################################
# File: webscraper_gui.py.py                                #
# Date: 03/11/2023                                          #
# Course: CS3141                                            #
# Author(s): Evan Vandermate (evanderm)                     #
# Desc: Created the main webscrapper gui.                   #
# Last Updated:                                             #
#       evanderm @ 03/11/2023 - Initial document            #
#       evanderm @ 03/25/2023 - Implement wiki libraries to #
#                               search for related pages.   #
#############################################################
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import wiki_scrapper.search_results as wikiresults
import wikipediaapi
import webbrowser

# Web Scrapper GUI Main Class
class scrapperGUI(ctk.CTk):
    def __init__(self):
        # Initialize tkinter window
        super().__init__()

        # Setup window parameters
        self.title("Super Cool Wikipedia Webscraper with GUI and Also Has No Bugs (SCWWwGUIaAHNB)")
        #self.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))

        # Window callbacks
        self.protocol("WM_DELETE_WINDOW", self._quit)

        # Vars
        self.relatedPages = None
        self.wiki = wikipediaapi.Wikipedia('en')
        self.searchterm = tk.StringVar(value="Enter Wiki Title...")
        self.resultsAmount = tk.StringVar(value="5")

        # Frames
        self.frm_results = ctk.CTkFrame(master=self)
        self.frm_searchTools    = ctk.CTkFrame(master=self)
        self.frm_results.grid(row=0, column=0, sticky='news')
        self.frm_searchTools.grid(row=1, column=0, sticky='news')

        # Widgets for "frm_searchTools" frame
        self.searchtermEntry    = ctk.CTkEntry(master=self.frm_searchTools, textvariable=self.searchterm)
        self.searchButton       = ctk.CTkButton(master=self.frm_searchTools, text="Search", command=self.search)
        self.resultsAmountLabel = ctk.CTkLabel(master=self.frm_searchTools, text="Number of results: ")
        self.resultsAmountEntry = ctk.CTkComboBox(master=self.frm_searchTools, variable=self.resultsAmount,
                                                  values=['1', '5', '10', '20'])

        # Arrange widgets
        self.searchtermEntry.grid(row=0, column=0, sticky='news')
        self.searchButton.grid(row=0, column=1, sticky='nws')
        self.resultsAmountLabel.grid(row=1, column=0, sticky='nes')
        self.resultsAmountEntry.grid(row=1, column=1, sticky='news')

        # Widget callbacks
        self.searchtermEntry.bind("<FocusIn>", self.defaultText)

        # Widgets for "frm_results" frame
        self.resultsTree = ttk.Treeview(master=self.frm_results, columns=['title', 'similarity', 'url'], show='headings')
        # Setup resultsTree
        self.resultsTree.heading('title', text='Title')
        self.resultsTree.heading('similarity', text='Similarity')
        self.resultsTree.heading('url', text='URL')
        self.resultsTree.column("url", minwidth=0, width=300, stretch=tk.YES)
        self.resultsTree.bind("<Double-Button-1>", self.onResultsClick)
        # Arrange widgets
        self.resultsTree.grid(row=0, column=0, sticky='news')

        # Initialize main-loops
        self.mainloop()

    #################################################
    # main()                                        #
    #-----------------------------------------------#
    # The main loop for the window.                 #
    # All tasks here will run every frame update.   #
    #################################################
    def main(self):
        # Tasks to update periodically (not implemented yet)

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
        # Get wiki page from title
        page = self.wiki.page(self.searchterm.get())

        # Check if page exists
        if not page.exists():
            print(f"No wiki page found with title [{self.searchterm.get()}]")
            return

        # Find related pages
        self.relatedPages = wikiresults.related_pages(self.searchterm.get(), int(self.resultsAmount.get()))

        # Display results
        self.updateResults()
        print(f"Search for [{self.searchterm.get()}]")
        print(f"Results: {self.relatedPages}")

    #################################################
    # updateResults()                               #
    #-----------------------------------------------#
    # Updates the results table with similar pages. #
    #################################################
    def updateResults(self):
        # Create list of results
        results = []
        for page in self.relatedPages:
            title = page[0]
            similarity = page[1]
            results.append((title, str(similarity), f"https://en.wikipedia.org/wiki/{title}"))
            if len(results) >= int(self.resultsAmount.get()):
                break

        # Clear old results
        for item in self.resultsTree.get_children():
            self.resultsTree.delete(item)

        # Add results to table
        for result in results:
            self.resultsTree.insert('', tk.END, values=result)

    #################################################
    # onResultsClick()                              #
    #-----------------------------------------------#
    # Callback for double-clicking on table entry.  #
    #################################################
    def onResultsClick(self, event):
        # Get selected result
        item = self.resultsTree.selection()[0]

        # Get selected url
        url = self.resultsTree.item(item)['values'][2]

        # Open url
        webbrowser.open_new_tab(url)

    #########################################
    # defaultText()                         #
    #---------------------------------------#
    # Callback for searchTermEntry widget.  #
    # Clears the placeholder text.          #
    #########################################
    def defaultText(self, args):
        self.searchterm.set("")

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