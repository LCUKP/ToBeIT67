word = {
  "0" : "rei",
  "1" : "ichi",
  "2" : "ni",
  "3" : "san",
  "4" : "shi",
  "5" : "go",
  "6" : "roku",
  "7" : "shichi",
  "8" : "hachi",
  "9" : "kyu",
  "10" : "ju",
  "100" : "hyuku"
}

num = input()
if num in word :
    print(word[num])
else :
    print("Error")