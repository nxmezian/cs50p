#prints file type of a given file with file extension
filetype = input("What is the name of the file? ").strip().lower()

if filetype.endswith(".gif"):
        print("image/gif")

elif filetype.endswith(".jpg"):
        print("image/jpeg")

elif filetype.endswith(".jpeg"):
        print("image/jpeg")

elif filetype.endswith(".png"):
        print("image/png")

elif filetype.endswith(".pdf"):
        print("application/pdf")

elif filetype.endswith(".txt"):
         print("text/plain")

elif filetype.endswith(".zip"):
        print("application/zip")
else:
    print("application/octet-stream")##
