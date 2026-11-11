This is my first read me xD
Project: CLI_FILE_MANAGER
Made by DashMC:

to run it you must need the __pycache__ and
-CLI_ARCHIVE_HANDLER.py
-CLI_CONFIG.py
-CLI_LOGGER.py
-CLI_MAIN.py
-GLOBAL_ROUTE.py
-OWN_FORMATTER.py
and these archives in the same folder IDK what is __pycache__ but need it
here how it works

you need to put first a route put a route like "C:/MY_carpet" for the programm to access
then use one of theese:

-cr or --create : it create a file in the given route(the given route is the first arg) first the name of the archive and then the type example:
text txt result = text.txt

-co or --copy : it copy a file in another folder if the file is already in the folder it create a copy to use
first the route of the archive and then the new route to put if the archive is in the route that you put first then just put the archive name example : i want to copy text.txt in "C:/MY_carpet" i do it

-de or -delete : it delete an archive of the given route example -de text.txt

-re or --rename : it takes a name and a new_name the name is the file name and the new_name the new name to rename can also move files example : -re text.txt text2.txt result : text2.txt (note if you dont put the suffix then it wont be the expected archive)

-vi or --view : is a made window in tkinter that shows the archives in a GUI it takes one argument the suffix use for example txt for show all txt in a route (use folder for all the folders i think it only works with the route that you give first)

and that's all i hope you enjoy the programm use --help for info in the cmd take care !  