# COMP1110 Lab Test 1

At your scheduled week three lab session, you will have the opportunity to sit a lab exam.   The exam will consist of four questions, drawn randomly from the choices listed below.  You are encouraged to prepare for the exam by working through these questions in your own time and at your scheduled lab.  The lab test is *redeemable* against your final exam mark, so if you are unable to attend your lab, or you do poorly in the lab test, you can recover those marks in the final exam.  You are required to attend your scheduled lab time.

*Note:* I have created a [video](http://cs.anu.edu.au/courses/COMP1110/howto/labtest1.mp4) showing how to complete Question one, step-by-step.  If, when you are practicing for this test, you want to repeat the steps in Question 1, you will need to get rid of your previous attempt at Question 1, because the instructions are written on the assumption that you don't already have an IntelliJ project called `comp1110-labtest1`.   You can do this a number of ways.   One is to simply change the name of the project (the very first step of Question 1) each time you practice (`comp1110-labtest1`, `comp1110-labtest1-taketwo`, etc).  Another is to move or delete the  folder from the previous attempt/s (using a file manager or the command line).    You should find the project in the `IdeaProjects` folder in your home directory.

---

*No Materials Permitted.*

## Question 1 (3 Marks)

You will be asked to answer the following question:

* Using IntelliJ, create a new Java project called `comp1110-labtest1`.
* Import the project into git (`VCS` -> `Import into Version Control...` ->
`Create Git Repository...`).   Select the default location (`comp1110-labtest1`)
as the place where the new git repository is created.
* Within your project's `src` directory, create a new Java class called 
`comp1110.labtest1.HelloWorld` (you should add the file to git when prompted).
This should appear as a file `HelloWorld` within a package `comp1110.labtest1`. 
This detail is important because the tests assume that your work appears in
exactly this location.
* Force JUnit to be added to your project's classpath.  Place your cursor within
your `HelloWorld` class, and type `Ctrl+Shift+T` (or `Navigate` -> `Test`). 
This should bring up the `Create Test` dialogue.  From the `Testing library:`
drop-down, select `Junit4`.   Use the `Fix` button to add Junit to your module.
In the next dialogue, stick with the default to use the library in the IntelliJ 
distribution, and press OK.  You can then press `Cancel` at the bottom of the
`Create Test` dialogue (you don't actually need to create a test, you just want
to add Junit to your path).
* Now add `comp1110-labtest1.jar` to your module's dependencies.   `File` ->
  `Project Structure...`, choose `Modules` and select the `Dependencies` tab. 
  Use `+` and slect `JARs or directories...` then navigate to your 
  `comp1110-labtest1.jar` which you should [download](http://cs.anu.edu.au/courses/COMP1110/comp1110-labtest1.jar)
  if you're practising, or you'll find on your desktop when you're sitting the
  actual lab exam.  Once you've added it, you should see `comp1110-labtest1.jar`
  within your `External Libraries` folder.
* Now copy the `runConfigurations` folder from `comp1110-labtest1.jar` into your
  `.idea` folder.  Look within `External Libraries`, then navigate into `comp1110-labtest1.jar`,
  and find `runConfigurations`.  Right-click on that folder, and select `Copy`
  (or use a keyboard shortcut).  Then navigate to your `.idea` folder, which 
  should the topmost folder within your project.  Select `.idea`, and then
  paste (either right-click and select `Paste`, or else use the keyboard shortcut).
  You will see a dialogue confirming the copy; select `OK`.   If prompted, 
  add the files to Git.   You should now see `Q1 HelloWorld` next to the green run
  arrow, which means you are now ready to run tests.
* Navigate back to your `HelloWorld` class, and modify it so that its main method prints `Hello world!`.
* Test your `HelloWorld` class by selecting the `Q1 HelloWorldTest` option in the 
  drop-down next to green arrow.
* Once your `HelloWorld` class passes the tests, commit it to your git repo.

## Question 2 (3 Marks)

You will be asked to answer *one* of the following questions:

1. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `ShoeSize`, that will estimate your shoe size by reading in your height (in meters) from the console, multiplying by 5.0, rounding it to the nearest integer (rounding up on ties), and printing the result. Test your program using the `Q2 ShoeSizeTest` test. Add and commit your work.

2. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Square`. The class will read from the console an integer that represents the length of a side and then calculate and print an integer that reprents the area of a square. Test your solution using the `Q2 SquareTest` test. Once you have it working, add and commit your work.

3. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Greet` that reads in from the console a string, and then outputs a greeting `Hi ...!`, where the name replaces the elipses. e.g. If the input is `Hugh` then your output should be `Hi Hugh!`. Test your solution using the `Q2 GreetTest` test. Once you have it working, add and commit your work.

4. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Name` that reads in your name from the console and then prints out your name in upper case (hint: use the `toUpperCase()` method of `String`), and then on a new line, print the number of characters in your name. e.g. if your name is Bill the program should print out `BILL` on one line and `4` on the next. Test your solution using the `Q2 NameTest` test. Once you have it working, add and commit your work.

## Question 3 (2 Marks)

You will be asked to answer *one* of the following questions:

1. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Even` that reads an integer (`n`) from the console and then prints all the even numbers between 1 and n, inclusive of n, each on a new line. Test your solution using the `Q3 EvenTest` test. Once you have it working,  working, add and commit your work.

2. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Movie` that reads in the name of a movie and its length in minutes, entered one line after the other at the console. The program must print the name of the film followed by `runs for `, then its length in hours and minutes. e.g. if the inputs are `Finding Nemo` and `104`, then the program would output `Finding Nemo runs for 1 hour and 44 minutes`. If the movie is less than one hour, you should not print hours, if it is greater than one hour you should print `hours` instead of `hour`. Likewise for minutes; if there are no minutes, do not print them, if there is one, print `minute`, and if more than one, print `minutes`. (Hint - use the `%` operator). Test your solution using the `Q3 MovieTest test`. Once you have it working, add and commit your work.

3. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Grade` that reads a mark for a subject (an integer) from the console and then prints the final grade based on this mark. Assume final grades are calculated using the following: marks between and including 0 and 49 will given a grade of `N`, 50 and 59 will give `P`, 60 and 69 will give `C`, 70 and 79 will give `D`, and finally 80 and 100 will give `HD`. If the mark is less than zero or greater than 100, print `Bad mark`. Test your solution using the `Q3 GradeTest` test. Once you have it working, add and commit your work.

4. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Odd` that reads an integer from the console and then determines whether it is odd. If the input is a number, X, the program will print X is odd. if X is odd, otherwise it will print X is even. For exanple, if the number was 3, the program would print `3 is odd`. This program must use a method with the signature `public static boolean isOdd(int i)`. Test your solution using the `Q3 OddTest` test. Once you have it working, add and commit your work.

## Question 4 (2 Marks)

You will be asked to answer *one* of the following questions:

1. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Prime` that reads a positive integer from the console and then prints all of the prime numbers from 1 to n (inclusive), one on each line. Test your solution using the `Q4 PrimeTest test`. Once you have it working, add and commit your work.

2. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Permute` that reads in two strings one line after the other from the console then determines whether the characters of one string are some permutation of the characters of another string (a permutation is a strict reordering, no additions, no deletions). The strings will be made up only of lower case letters and not contain white spaces (e.g. tab, space character). If the strings are perumtations of each other, print `Yes` otherwise print `No`. So for exampl `cats` is a permutation of `acst`, so you would print `Yes` whereas, neither `cats` nor `catt` are permutations of `cate`, so you would print `No` (Hint - use `.length` to find the length of a `String` and the `charAt()` method to get the character at a given position in a `String`). Test your solution using the `Q4 PermuteTest` test. Once you have it working, add and commit your work.

3. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Ones` that reads from the console a positive integer and prints out the number of '1's in the underlining binary pattern representation. This program need only work with positive numbers. e.g. The integer 5 has 2 '1's its binary representation, so you would print out `2`. Test your solution using the `Q4 OnesTest` test. Once you have it working, add and commit your work.

4. Within the `comp1110.labtest1` package of the `comp1110-labtest1` project, create a class `Radix` that is able to convert numbers between different radices (also known as bases) (for simplicity we restrict the possible radices to 2, 3, 4, ... , 10). The program should read in three variables from the console one line after another; an integer, the source base, an integer, the destination base, and a string. The program should interpret the string as a number in source base and output it as a number in destination base (using the source and destination base number system). e.g. Say your source base was 3 and the destination base was 5. Then if the string was 21, then `12` should be printed. You do not need to handle negative numbers. Test your solution using the `Q4 RadixTest` test. Once you have it working, add and commit your work.
