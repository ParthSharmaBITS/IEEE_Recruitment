marks_cutoff = [("Pilani","CS",327),("Pilani","Eco",271),("Pilani","Chemical",247),("Pilani","Bio",236),("Goa","CS",301),("Goa","Eco",263),("Goa","Chemical",239),("Goa","Bio",234),("Hyderabad","CS",298),("Hyderabad","Eco",261),("Hyderabad","Chemical",238),("Hyderabad","Bio",234)]
campus_cutoff = {"Pilani":{},"Goa":{},"Hyderabad":{}}

for Campus, Branch, Marks in marks_cutoff:
    campus_cutoff[Campus][Branch] = Marks

print(campus_cutoff)
    