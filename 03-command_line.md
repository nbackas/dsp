# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
pushd - takes current directory and 'pushes' it into a temporary place to save for later
popd - retrieves directory that was last pushed, makes it current directory
cat - prints file all at once
less - views a file in pages instead of all at once, good for larger files
hostname - displayed network name of current machine
apropos - searches through manual for given keyword to find relevant help
mv - moves files towards specified directory
mkdir - creates new directory
cd - changes working directory
rmdir - removes directory

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > 'ls' lists items in a directory. 'ls -a' lists all items, including hidden items. 'ls -l' lists files & directories along with date modified and size. 'ls -lh' lists items along with size in a more readable format. Combining '-a' with either of the other two flags will show relevant information for hidden files in directory as well.

---


---

What does `xargs` do? Give an example of how to use it.

> > 'xargs' is used to execute longer lists of arguments, which can create errors. It is useful for executing an argument on a list of files. It is especially useful when used in conjunction with 'find' or 'grep.' 
Example:
find /temp -name "*.txt" | xargs rm
The above example will remove all .txt files from the 'temp' directory.

---

