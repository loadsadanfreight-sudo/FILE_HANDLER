from CLI_ARCHIVE_HANDLER import ARCHIVE
import argparse

#argparse section---
parser = argparse.ArgumentParser()

parser.add_argument(
       "route",
                    default="D:/",
                    type=str,
                    help="Give a route to work with it"
)
parser.add_argument(
      "--create",
                   "-cr",
                   dest="cr",
                   nargs=2,
                   metavar=("NA","SU"),
                   help="create a new file with the given name and suffix (NA=NAME,SU=SUFFIX) (use folder for carpets in suffix)"
)
parser.add_argument(
      "--copy",
                   "-co",
                   dest="co",
                   nargs=2,
                   metavar=("NA","RO"),
                   help="copy the specified file to the given route (NA=NAME,RO=ROUTE)"
)
parser.add_argument(
      "--delete",
                   "-de",
                   dest="de",
                   nargs=1,
                   metavar="NAME",
                   help="Delete the specified file (NA=NAME)"
)
parser.add_argument(
      "--rename",
                   "-re",
                   dest="re",
                   nargs=2,
                   metavar=("NA","WNA"),
                   help="Rename the specified archive name to a new archive name (NA=NAME,WNA=NEW_NAME)"
)
parser.add_argument(
                   "--no-confirm",
                   "-n-c",
                   dest="show_confirmation",
                   action="store_true",
                   default=False,
                   help="If in the confirmation mode will be disable don't recommend to do it can be dangerous"
)
parser.add_argument(
                   "--view",
                   "-vi",
                   dest="vi",
                   nargs=1,
                   metavar="SUFFIX",
                   help="Search all the archives with the given suffix and show them in a Window (SU=SUFFIX)",
)
parser.add_argument(
                   "--tutorial",
                   "-tu",
                   dest="tu",
                   action="store_true",
                   default=True,
                   help="If in it will disable to show the help in the --view mode"
)

args = parser.parse_args()
#---------------------

#Archive manager--------
def main():
   archive_tool = ARCHIVE(args.route,args.tu)
   call = "No for now"

   if args.cr:
       call = archive_tool.create_(*args.cr,confirm=args.show_confirmation)
   elif args.co:
       call = archive_tool.copy_(*args.co,confirm=args.show_confirmation)
   elif args.de:
       call = archive_tool.delete_(*args.de,confirm=args.show_confirmation)
   elif args.re:
       call = archive_tool.rename_(*args.re,confirm=args.show_confirmation)
   elif args.vi:
       call = archive_tool.view_(*args.vi)
   return call
#--------------
if __name__ == "__main__":
    main()