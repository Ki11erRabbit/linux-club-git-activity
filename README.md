# Linux Club Git Activity

Today your job is to complete a simple calculator application. To start simply clone the repository by doing `git clone https://github.com/Ki11erRabbit/linux-club-git-activity` in your terminal of choice.

If you don't have git installed, you can download it [here](https://git-scm.com/downloads).

Once you have done that, you will add your changes to the branch `start-here`. You will need a text editor of some kind and python to be installed.

## How to change branches
To change branches, simply do `git checkout <Branch Name>` where `<Branch Name>` is the name of the branch you would like to change to.

Once you have changed branches, your task is to change line 49 from `print(value)` to instead say something like:
* "The result of expression: <expression> is ..."
* "The answer is..."
* "Your calculation is..."
* etc

Once you have made this change, you should add and commit your changes to the branch `start-here`.

A commit is git's way of tracking changes made to files.

## How to add and commit
To add a file, it is as simple as doing `git add <filename>` where `<filename>` is the name of the file you are changing.

To commit your changes, simply do `git commit -m <commit message>` where `<commit message>` is the message for the commit.
Always add meaningful messages to your commits.

If you didn't do `git commit -m` and instead `git commit`, you will likely find yourself in Vim. To enter a message through Vim, simply press the `i` key to enter into insert mode.
Then you can start typing your commit message.

To Leave Vim, press `Esc` then type `:wq` to save and quit. This will add the message

## How to run the script
To run the Python script, simply use either `python` or `python3` (whichever one works) with the script name (calculator.py), then in either single or double quotes, the math expression that may use addition, subtraction, multiplication, or division.
To have a well formed math expression, there must be whitespace between the numbers and symbols.

## Merging changes back onto main
The next step is to merge your changes back into the main branch.
To do so, simply checkout the main branch.

Then, to merge the branch, do `git merge <branch name>` where `<branch name>` is the name of the branch you wish to merge onto the current branch. In this case, it is the `start-here` branch.

## How to solve merge conflicts
When you merged `start-here` onto `main`, you likely triggered a merge conflict. Not to worry, it is easy to fix.

Simply open the `calculator.py` file and you will see something that looks like this:
```
<<<<<<< HEAD
some code here
=======
some other code here
>>>>>>> start-here
```
`HEAD` is simply where the most recent commit is located, and in this case it is in `main`.
The code beneath it is the code that is conflicting with your merge from branch `start-here`
The code beneath the `=======` is the code that is coming from `start-here` that conflicting with `HEAD`'s code.

To resolve the merge conflict, simply pick one of the lines of code and delete the brackets and equal signs around the code.

Once you have fixed the conflict, simply add and commit the file with the conflicts.

## Now try running the program
Try all sorts of different expressions to see if there are any problems with the math. (I recommend trying division)

## Locating bugs
While with this simple toy program, you likely can find it with a good set of eyes. In larger codebases, it gets much harder to do so.
To help us find the bug, we will use a feature of git called bisect.

Git Bisect automates a binary search on your commits to find bugs.
To begin, simply type `git bisect start`.

If you get an error, make sure you are in the folder `linux-club-git-activity`.

You first start by marking the current commit as bad by typing `git bisect bad`.
Now you need to select a good commit. Since you don't know when it was good, here is the commit that was "good". `59d1e99`
You do this by typing `git bisect good <commit identifier>` where `<commit identifier>` is something that identifies the commit, in this case it is `59d1e99`.

Now git will have selected a commit for you to check, run the script with a test case and see if it is good, if so, type `git bisect good`. If bad, simply type `git bisect bad`.
Do this until it it selects a commit where the bug was added. To view the changes made to the code, type `git show` to see the changes made. It should print out in red the removed code and in green the added code. See if there is anything out of the ordinary in this code. Once you have found it type `git bisect reset` to go back to `HEAD`.

With the knowledge you have about where the bug is, go and find the error in `calculator.py` in the main branch and fix it. Once you have fixed it, add and commit your changes to the main branch.




