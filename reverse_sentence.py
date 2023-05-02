'''
PROBLEM: 
Given a sentence, reverse the order of its words 
without affecting the order of letters within a given word.

''' 

def reverse_words(sentence):
   # write you code

   # Easy Way to do Things: 
   # rev_list = sentence.split()
   # rev_list.reverse()
   # return ' '.join(rev_list)

   # More algorithmic way to do things

   rev_str = sentence[::-1]
   start = 0
   end = 0
   space = 0
   res = []

   while start < len(rev_str) :

      while end < len(rev_str) and rev_str[end] != ' ' :
         end += 1
      
      space = end
      if end == len(rev_str) : end -= 1
      if rev_str[end] == ' ' : end -= 1

      print("end: ", end, ", start: ", start)

      str = []
      while end >= start :
         
         str.append(rev_str[end])
         end -= 1
      
      res.append(''.join(str))

      start = space
      while start < len(rev_str) and rev_str[start] == ' ' :
         start += 1
      
      end = start

   return " ".join(res)






