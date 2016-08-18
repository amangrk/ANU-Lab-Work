# COMP1110 Lab Test 2

At your scheduled week seven lab session, you will have the opportunity to sit the second lab exam.   The exam will consist of four questions, drawn randomly from the choices listed below.  You are encouraged to prepare for the exam by working through these questions in your own time and at your scheduled lab.  The lab test is *redeemable* against your final exam mark, so if you are unable to attend your lab, or you do poorly in the lab test, you can recover those marks in the final exam.  You are required to attend your scheduled lab time.

*Note:* If, when you are practicing for this test, you want to repeat the steps in Question 1, you will need to get rid of your previous attempt at Question 1, because the instructions are written on the assumption that you don't already have an IntelliJ project called `comp1110-labtest2`.   You can do this a number of ways.   One is to simply change the name of the project (the very first step of Question 1) each time you practice (`comp1110-labtest2`, `comp1110-labtest2-taketwo`, etc).  Another is to move or delete the  folder from the previous attempt/s (using a file manager or the command line).  You should find the project in the `IdeaProjects` folder in your home directory.

---

*No Materials Permitted.*

## Question 1 (1 Mark)

You will be asked to answer the following question:

* Using IntelliJ, create a new Java project called `comp1110-labtest2`.
* Import the project into git (`VCS` -> `Import into Version Control...` ->
`Create Git Repository...`).   Select the default location (`comp1110-labtest2`)
as the place where the new git repository is created.
* Within your project's `src` directory, create a new Java class called 
`comp1110.labtest2.HelloWorld` (you should add the file to git when prompted).
This should appear as a file `HelloWorld` within a package `comp1110.labtest2`. 
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
* Now add `comp1110-labtest2.jar` to your module's dependencies.   `File` ->
  `Project Structure...`, choose `Modules` and select the `Dependencies` tab. 
  Use `+` and slect `JARs or directories...` then navigate to your 
  `comp1110-labtest2.jar` which you should [download](http://cs.anu.edu.au/courses/COMP1110/comp1110-labtest2.jar)
  if you're practising, or you'll find on your desktop when you're sitting the
  actual lab exam.  Once you've added it, you should see `comp1110-labtest2.jar`
  within your `External Libraries` folder.
* Now copy the `runConfigurations` folder from `comp1110-labtest2.jar` into your
  `.idea` folder.  Look within `External Libraries`, then navigate into `comp1110-labtest2.jar`,
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


## Question 2 (4 Marks)

You will be asked to answer *one* of the following questions:

1.  Within the `comp1110.labtest2` package of the `comp111-labtest2` project, create a class `Names` that will create an `ArrayList` of `String`, read names from the console into it, each on a separate line (until the user indicates the end of the list by typing `ctrl-D`, by pressing the control and 'D' keys, (`ctrl-Z` on Windows)), and print the names out in reverse order on separate lines (using a `for` loop ). Test, add and commit your work.

2. Within the `comp1110.labtest2` package of the `comp111-labtest2` project, create a class, `Mean` that will create an `ArrayList` of `Double`, reading `double`s from the console into it, each on a separate line (until the user types `ctrl-D`, by pressing the control and 'D' keys, (`ctrl-Z` on Windows), to indicate the end of the list), and calculate and print the arithmetic mean of the numbers in this list. Test, add, and commit your work.

3. Within the `comp1110.labtest2` package of the `comp111-labtest2` project, create a class, `People` that will store a table of people's first names and ages (using a `HashMap`, the people's names as the key, and integer ages as the value). Read people and ages from the console (e.g. `Bob 19`) and add to the `HashMap`. For this example, assume ages are integers and names do not contain spaces. After a list of name, age pairs, a name will be entered without an age (e.g. `Mary`) and the user will terminate their input by typing `ctrl-D`, by pressing the control and 'D' keys (`ctrl-Z` on Windows).  Treat the last name (`Mary` in this example) as a query.  Print out the age of the person entered last, or print `unknown` if the person's name is unknown (i.e. it did not appear earlier in the list). Test, add, and commit your work.

4. Within the `comp1110.labtest2` package of the `comp111-labtest2`, create a class, `BMI` that stores information about a person including: name, height, and weight. The class will have a constructor `BMI(String name, double height, double weight)`. The class should have a public instance method, `getBMI()` that returns a `double` reflecting the person's BMI (Body Mass Index = weight (kg) / height2 (m2) ). The class should have a public `toString()` method that returns a `String` like `Fred is 1.9m tall and is 87.0kg and has a BMI of 24.099722991689752kg/m^2` (just print the `double`s without special formatting). Implement this class (if you wish you may implement a main method that demonstrates its use). Test, add, and commit your work.

## Questions 3 (3 Marks) and 4 (2 Marks)

You will be asked to answer *one* of the following variations (A, B, C, or D) on Questions 3 and 4:

---
## A

## Q3 (3 Marks)

Within the `comp1110.labtest2` package of the `comp111-labtest2` project, create an abstract class, `Shape`, that stores information about simple shapes. `Shape` includes two abstract public methods, `double perimeter()`, and `double area()`, which return the length of the perimeter and the area of the shape respectively. Create two additional classes, `Square` and `Circle`, each of which extends `Shape`, and each of which takes a single `double` length argument in its constructor. Add a main method to `Shape` which includes the following code:
```java
Shape s1 = new Square(10);    // a square with sides of 10.0 units
Shape s2 = new Circle(1.0);   // a circle of radius 1.0 units
System.out.println(s1.perimeter());
System.out.println(s1.area());
System.out.println(s2.perimeter());
System.out.println(s2.area());
```
You should produce the following output:
```
40.0
100.0
6.283185307179586
3.141592653589793
```
Test, add, and commit your work.

## Q4 (2 Marks)

Add to the above example the ability of store the xy-position of the center of each shape. Add `x` and `y` fields to `Shape` and for each shape add a second constructor that takes three `double`s as arguments, `length`, `x`, and `y`. Add an abstract public method `boolean overlaps(Shape other)` to `Shape` that takes a single `Shape` as an argument and returns `true` if the other shape overlaps the shape it is called on. Assume the squares are upright (parallel to the axis). Test, add, and commit your work. Demonstrate your solution.

---
## B

## Q3 (3 Marks)

Within the `comp1110.labtest2` package of the `comp1110-labtest2` project, create a class, `Shop`, that maintains information about the inventory of a shop. Create an instance method, `void addItem(String name, int stock, int price)` which is used to add to an internal data structure an item, how many of that item are in the shop, and how much each costs, in cents. Create another instance method, `int totalStockValue()`, which uses the internal data structure to return the sum of the value of all stock, as an `int`, in cents. Test, add, and commit your work.

## Q4 (2 Marks)

Implement another instance method `void addItem(String name, int stock, int price, int rate, int reorderdays)` which allows you to store not only the item name, stock level and price, but also the rate (in items per day) that the item is usually sold, and the number of days it takes to reorder the stock. Implement another instance method `HashMap reorder()` which returns a hash map listing the name (key) and number (value) of all of the items that need to be reorderd today in order to ensure that the expected number of stock is always at least one (ie sufficient to last until the order arrives, assuming average sales). Whenever an item is ordered, seven days worth of average sales minus the current stock of that item is always ordered. Test, add, and commit your work. (2 Marks)

---
## C

## Q3 (3 Marks)

Within the `comp1110.labtest2` package of the `comp1110-labtest2` project, create a class, `Cost`, that tracks the cost of items. Within `Cost`, create a public inner (non-static) class, `Item`, that includes the following:
```java
public class Item {
  String name;
  int cost; // in cents
  public Item(String n, int c) {
    name = n;
    cost = c;
  }
  public String toString() {
    return name + " " + cost;
  }
}
```
Modify your inner Item class so that it implements the `Comparable<Item>` interface. Items should be ordered based on the cost (lowest cost first). If two items cost the same amount then order these items alphabetically based on their name. Add an instance data structure (`HashMap<String, Item>`) to your `Cost` class for storing items, using the item's name as the key. Add an instance method `void addItem(String name, int cost)` to your `Cost` class that allows new items to be added, and a method `printCost()` that prints out all items sorted in the order described above, one item per line, with a single space separating the item name and its cost. Test, add, and commit your work.

## Q4 (2 Marks)

Suppose you are given a gift voucher for the above shop. Assume that the shop does not give change on gift vouchers, and you do not wish to spend any more than what is in the gift voucher. Add an instance method `int voucherWaste(int value)` to `Cost` which will return the difference between the value of the voucher (in cents) and what could be spent given the set of items in the shop. e.g. Say you had a voucher for $100 and the items in the shop were worth: $87, $20, $99, $12, then the most you could spend would be the full $100 (just buy 5 of the $20 item) so there would be zero waste, whereas, if the items in the shop were worth: $87, $22, $30, $45 then the most you could spend would be $97 (remember that your method will express the voucher and the costs in the same units, cents). Test, add, and commit your work.

---
## D

## Q3 (3 Marks)

Within the `comp1110.labtest2` package of the `comp1110-labtest2` project, create a class, `Sum` that extends an `ArrayList` of `Integer` by adding a public method, `int sum()` that returns the sum of all elements in the list of Integers (add the elements up each time the method is called). Test, add, and commit your work. Demonstrate your code.

## Q4 (2 Marks)

Enhance the above solution such that the sum is stored and maintained as a private instance field of `Sum`. Now when the `sum()` method is called, it should just be able to return the value of the sum field rather than having to add everything up. Note that many of the standard methods of the `ArrayList` class must be overwritten so that they are able to adjust the sum as elements are added or removed from the list. For this question you need only override the four 'add' methods (`boolean add(Integer i)`, `void add(int index, Integer i)`, `boolean addAll(Collection<? extends Integer> c)`, and `boolean addAll(int index, Collection<? extends Integer> c) `). Test, add, and commit your work.
