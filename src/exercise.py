from song import Song
def main():
    #write your code below this line
  jack_sparrow = Song("The Lonely Island", "Jack Sparrow", 196)
  another_sparrow = Song("The Lonely Island", "Jack Sparrow", 196)

  if (jack_sparrow == another_sparrow):
      print("Songs are equal.")

  if (jack_sparrow == "Another object"):
      print("Strange things are afoot.")
if __name__ == '__main__':
  main()
  from song import Song
else:
  from src.song import Song

