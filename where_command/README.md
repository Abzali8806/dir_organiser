As of now this program has been tested and used on a debian system. I will be sure to clone it onto a windows vm soon and, after a few adjustments, run it on there. However, feel free to clone, experiment and build upon it.

This program is reliant on the program in the Abzali8806/dir_organiser repository, mainly because it creates and adds to and holds the logs.csv file.


If not already installed, you'll need to install:
 -> sys 
 -> csv
 -> pyperclip

<!-- file execcution  -->
(side-note: "<filename>" = the name of the file you're looking for.)

To run the program you can enter "python3 file_path <filename>" into the terminal, or you can make your life easier by following what I did.
I created an alias for the "python3 file_path" part of the above command and set it to "where" so instead of entering ("python3 file_path <filename>") into the terminal I enter ("where <filename>).


to create a bash alias follow the instruction @:
https://linuxize.com/post/how-to-create-bash-aliases/


<!-- How it works -->

-> user enter <command> <filename> into terminal.
-> <filename> saved as filename variable in python script.
-> program retrieves entries with for file with <filename>.
-> sorts entry's log date from oldest to latest.
-> returns path for <filename> logged in latest entry and
copies file path to clipboard.