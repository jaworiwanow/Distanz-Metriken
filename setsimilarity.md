# Exkurs: Ähnlichkeitsmetriken für Mengen

## Motivation
Wie bereits gesehen, ist der Abstandsbegriff für Mengen nicht hilfreich, wenn die Mengen gemeinsame Punkte haben. 

Für uns als Data Scientists kann es von Interesse sein, wie Ähnlich sich zwei Mengen sind. 

Ähnlichkeit ist auf einer Art invers zum Abstand und Ähnlichkeitsmetriken sind keine Distanz-Metriken. Oft sind diese jedoch eine Art Umkehrung der Distanzmetriken; 

Jede Menge hat Ähnlichkeit 1 zu sich selbst, Ähnlichkeiten können nicht negativ sein und die Ähnlichkeit ist symmetrisch.

Die Dreiecksgleichung lässt sich jedoch nicht einfach übertragen; Ihre Umkehrung $\sigma (M,O) \geq \sigma(M,N) + \sigma(N,O) $ gilt im Allgemeinen nicht. 

Seien $M = [-1,0), O = [0,1), N = [-\frac{1}{2},\frac{1}{2}]$. Dann müsste für eine Ähnlichkeitsmetrik gelten, dass $0 \geq  \frac{1}{2} +\frac{1}{2} =1 $.




````{dropdown} Notation

Seien $M, N \neq \emptyset$ zwei Mengen. Dann sind:

$$ \begin{aligned}
M \cup N &= \{ x: x \in M \wedge \} & \text{  die Vereinigung von M und N} \\
M \cap N &= \{ x: x \in M \land x \in N \} & \text{ der Durchschnitt von M und N} \\
M\setminus N &= \{ x:\in M \land x \notin N  \}  & \text { die Differenz von M und N }
\end{aligned}

$$

```{admonition}
:class: note
$M\setminus N \neq N \setminus M$ falls $ M \cap N \notin \{ \emptysetset, M, N \} $
```

Hier sind $\land $ das logische "und" und $\wedge$ das logische "oder" (einschließendes "und-oder") ist.
````


_________
### Tversky-Index

Seien $M, N \neq \emptyset$ zwei mengen. Dann ist für $\alpha, \beta \geq 0$

$$T_{\alpha, \beta}(M,N) = \frac{|M \cap N|}{|M \cap N| + \alpha |M \setminus N| + \beta |N \setminus M|} $$ 

der Tversky-Index von $M$ und $N$.


### Der Jaccard Index
#### Definiton

Seien $M, N \neq \emptyset$ zwei Mengen, dann ist 

$$ J(M,N) = \frac{|M \cap N|}{|M \cup N|} = \frac{|M \cap N |}{|M|+|N| - |M \cap N|} $$ 

der Jaccard Index von $M \text{ und } N$.

Der Jaccard Index ist hierbei der Tversky Index für $\alpha = 1 = \beta$

#### Eigenschaften

Für die Mengen $M, N \neq \emptyset$ gilt immer, dass $0 \leq J(M,N) \leq 1$. 

$J(N,M) = 1$ entspricht dem Fall, dass die Vereinigung und der Schnitt von $M$ und $N$ die gleiche Anzahl an Elementen haben, also, dass $M = N$. 

$J(N,M) = 0$ entspricht dem Fall, dass die beiden Mengen keine gemeinsamen Elemente haben. 

#### Anwendung
Der Jaccard Index kann für die object detection nützlich sein, um die Überschneidung von bounding boxes zu messen. 

Verwendung findet er auch in vieler Art Wissenschaft und ist vor allem für binäre oder binärisierte Daten nützlich und wird auch für Clustering verwendet. 



