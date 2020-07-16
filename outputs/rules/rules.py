def findDecision(obj): #obj[0]: B365H, obj[1]: B365D, obj[2]: B365A
   if obj[0]<=2.9:
      if obj[1]<=4.1:
         if obj[2]>2.1:
            return 'Ev'
         else:
            return 'Ev'
      elif obj[1]>4.1:
         if obj[2]>2.1:
            return 'Ev'
         else:
            return 'Ev'
      else:
         return 'Ev'
   elif obj[0]>2.9:
      if obj[1]<=4.1:
         if obj[2]<=2.1:
            return 'Deplasman'
         elif obj[2]>2.1:
            return 'Deplasman'
         else:
            return 'Deplasman'
      elif obj[1]>4.1:
         if obj[2]<=2.1:
            return 'Deplasman'
         else:
            return 'Deplasman'
      else:
         return 'Deplasman'
   else:
      return 'Deplasman'
