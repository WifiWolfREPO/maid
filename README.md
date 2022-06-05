# maid
maid - A really simple and MID text editor made with python.

All modules used are built-in so you don't have to download anything with pip

## How does it works
maid (Pronounced maid, all lowercase) is a text editor with simple commands such as :\clr (clear the file) or :\del (delete file).

Why "MID"?
Well, it can't backspace nor delete without clearing or deleting everything!

**Why?**

When I said "All modules are built-in", there is no way I can detect a keypress without **keyboard** or these stuff.
So instead I added these commands just like _vim_.

**How does it works? (again)**
The script can display and write text in real time because instead of opening the file, writing stuff and then close, it uses a function that opens the file, writes a line of the input and closes. Same for reading. That makes it load the file in real time.

You can't see the file update until you press enter because of python input thing.

