- https://geogebra.org/python/index.html

    
    - https://tice-c2i.apps.math.cnrs.fr/2023/10/21/pyggb/
    - http://revue.sesamath.net/spip.php?article1601
    - http://revue.sesamath.net/spip.php?article1620
    - https://mathematiques.ac-normandie.fr/Combiner-GeoGebra-et-Python
    - https://www.reddit.com/r/pyggb/
    - https://github.com/othoni-hub/PythonGgb
    - https://www.geogebra.org/u/dric
    
    - https://geogebra.org/python/index.html?name=toto&code=eJxVjssOgjAQRff9ihtWkIxG8RFj4gJ16cI%2FIAQKjMGWlBJ%2FX0oRtatmztxzJwgCcWMlYWuj%2B6qGfWm0mpXthLjKckTziJCpArlWnTV9boeQRONWHgNmVbnBcymcVJTagMEKJlOVDPcRjgLDG01pghPu7hcyIY5%2ByHkmG8LWk8JotjJNHHPXhpOEPhm%2F5kvbb%2BliRweK%2F5pne0srn7qwyZtJSetIvAEe41GS

```python
p=Polygon((A,B,C)) #A, B et C sont des points
p=Polygon([A,B,C])
p=Polygon(A,B,5) #pentagone régulier
Segment(A,B)
Vector(A,B)
Line(A,B)
Line(a,b) #coeff directeur et ordonnée à l’origine
Circle(A, 3) #centre et rayon
Circle(A, 3,color=’green’,line_thickness=10)
Ellipse(A,B,2)
Parabola(a, b, c) # trace la parabole d’équation y=ax²+bx+c
Vector(B, C)
D = Rotate(A, pi/6).with_properties(color=’green’)
   # le centre de la rotation est l’origine
   # pi doit être importé de la bibliothèque math
   # with_properties() permet de modifier les attributs du point
Intersect(parabola, line,2) # 2 objets ggb et le n° pt intersection
z = complex(2, -4)
abs(z) # argument de z
a=Slider(0, 4, increment=0.1)
Distance(A,B)
```