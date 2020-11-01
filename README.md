[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3538703&assignment_repo_type=AssignmentRepo)
# Exercise 5.11 Song

In the exercise base there is a class called `Song` that can be used to create new objects that represent songs. Add to that class the `__eq__` method so that the similarity of songs can be examined.

```python
jack_sparrow = Song("The Lonely Island", "Jack Sparrow", 196)
another_sparrow = Song("The Lonely Island", "Jack Sparrow", 196)

if (jack_sparrow == another_sparrow):
    print("Songs are equal.")

if (jack_sparrow == "Another object"):
    print("Strange things are afoot.")
```

```plaintext
Songs are equal
```
