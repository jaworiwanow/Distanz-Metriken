# Definition

## Motivation
Erst durch eine Metrik können wir Abstand, Nähe und Ähnlichkeit quantifizieren. 

Einige Verfahren die wir bereits kennengelernt haben (z.b.: kNN Regressoren und Classifier, k-Means, DBSCAN, Agglomerative Clustering ) und weitere noch unbekannte (bspw. in image recognition und NLP ) basieren explizit auf einen Abstandsbegriff. 

Doch dieser ist weitaus fundamentaler; Geometrie, Stochastik, Integralrechnung und Differenzialrechnung benötigen einen Abstandsbegriff.

Da verschiedene Metriken jedoch unterschiedliche Eigenschaften haben, kann ein Verständnis dieser von Vorteil sein. 



## Definition
Distanz-Metriken sind mathematische Fuktionen zur Abbildung eines Abstandbegriffes. 

````{panels}
Definition
^^^
Wir erwarten und von einem sinnvollen Abstandsbegriff, dass

1. ... ein Punkt keinen Abstand zu sich selbst hat und ungleiche Punkte nicht-negative Abstände zueinander haben.
2. ... der Abstand richtungs-unabhängig ist.
3. ... die direkte Verbindung zwischen zwei Punkten den kürzesten Abstand liefert. 

---

Mathematische Definition
^^^
Sei $M \neq \emptyset $ eine Menge. Eine Funktion $ \delta: M \times M \rightarrow \mathbb{R}_{0}^{+}  $ ist eine Metrik auf $M$, falls  $\forall \text{ } x,y \in M :$

1. $\delta(x,y) \geq 0 \text{   und   } \delta(x,y)= 0 \Leftrightarrow x = y$
2. $\delta(x,y) = \delta(y,x) $ 
3. $\delta(x,y) \leq \delta(x,z) + \delta(z,y) $

Dann ist $(M,\delta)$ ein metrischer Raum.
````

```{dropdown} Mathematische Symbole
$\emptyset$ ist die leere Menge, die kein Element enthält

$M \times M $ ist die Menge aller Paare von Elementen aus $M$

$\mathbb{R}_{0}^{+} = [0, \infty ) $, die Menge der nicht-negativen, reellen Zahlen ("floats $\geq 0$")

$\forall $ bedeutet "für alle", $\in$ bedeutet "in"

"$\Leftrightarrow $" bedeutet "genau dann, wenn"
```
```{admonition} Hinweis
:class: tip
Über die Gewünschten Eigenschaften können wir den Abstandsbegriff verallgemeinern und potentiell auf jede Menge (bspw. Wörter, DNA-Sequenzen, usw.) definieren. 

Es ist in der Tat möglich, auf jeder nicht-leeren Menge eine Metrik zu definieren. Bspw. ist die diskrete Metrik 
$\delta_\delta(x,y) = \begin{cases} 
0 & \text{falls } x = y \\
1 & \text{sonst}
\end{cases} $ 
auf jeder Menge definierbar.

Es ist sogar möglich Abstände auf hoch-abstrakte Konzepte wie z.B.: Spielstrategien (Helly Metrik) zu definieren. 
```

```{admonition} Geschichte
:class: note
Die [früheste](https://archive.org/details/grundzgedermen00hausuoft/page/211/mode/2up) bekannte Formulierung einer Metrik über diese Entfernungsaxiome ist von Felix Hausdorf {cite:ps}`hausdorff1914` . 

Die heute geläufige Formulierung stammt jedoch von Pavel Alexandrov{cite:ps}`walz2016lexikon`.

Das Konzept dieser Axiome ist jedoch [älter](http://www.lpsm.paris/pageperso/mazliak/Frechet_1906.pdf) und wurde von Maurice Fréchet{cite:ps}`frechet1906` acht Jahre früher, jedoch im Kontext der Konvergenz in der Funktionenanalysis eingeführt. 

```

```{admonition} Vokabular
:class: note
Mathematisch ausgedrückt handelt es sich bei Metriken also um positiv definite, symmetrische Funktionen, die Paaren von Elementen einer nicht-leeren Menge nicht-negative reelle Werte zuordnet und die Dreiecksungleichung erfüllen.
```

