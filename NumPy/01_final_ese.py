import numpy as np

studenti = np.array([
    [80,79,90],
    [60,75,90],
    [88,93,90],
    [55,68,70]
])

mean = np.mean(studenti)
media_stud = np.mean(studenti, axis=1)
media_materia = np.mean(studenti, axis=0)

studenti_norm=((studenti-max)/(max-min))
print(studenti_norm)

print(studenti)
print(mean)
print(media_stud)
print(media_materia)


