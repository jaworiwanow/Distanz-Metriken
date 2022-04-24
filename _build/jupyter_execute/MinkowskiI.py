#!/usr/bin/env python
# coding: utf-8

# # Minkowski-Metriken
# 
# Zur Familie der Minowski-Metriken gehören einige der wichtigsten und am häufigsten verwendeten Metriken. 
# 
# Sie sind von den Minkowski-Normen (auch p-Normen gennant) induzierte Metriken und stellen eine verallgemeinerung des euklidischen Abstands dar. 
# 
# 
# ## Definition
# Sei $p \in [1, \infty) $ und $x, y \in \mathbb{R}^n $. Dann ist 
# 
# 
# $$ \delta_p(x,y) = \left( \sum_{i=1}^n |x_i - y_i|^p  \right)^{\frac{1}{p}} $$  
# 
# die (von der p-Norm induzierte) Minkowski-Distanz. 
# 
# Für $p = \infty$ gilt: 
# 
# $$\delta_\infty (x,y) = max(|x_i - y_i |)$$
# 
# ```{dropdown} Mathematische Notation
# $ [1, \infty) $ ist das halboffene Intervall, dass alle reellen Zahlen $r: 1 \leq r < \infty$ beinhaltet. 
# Eine eckige  klammer bedeutet, dass der Randpunkt dabei ist, eine runde hingegen, dass der Randpunkt nicht dabei ist. 
# 
# $\mathbb{R}^n$ ist die Menge der n-dimensionalen reelwertigen Vektoren, also aller $[x_1, x_2, .... x_n]$ mit $\forall i \in \{1, 2, ... , n \}: x_i \in \mathbb{R}$
# 
# $\sum_{i=1}^n$ ist die Summe über den Index $\{1, 2, ... , n \} $
# 
# ```
# In den [Beweisen](MinkowskiBeweise) findet sich der Beweis dafür, dass die Definition für $p = \infty$ sinnvoll definiert ist.
# 
# 
# 
# ```{admonition} $\mathbb{C}$ und Teilmengen des $\mathbb{R}^n$
# :class: tip
# Die p-Normen und von ihnen induzierte Metriken sind auch auf den komplexen Zahlen definiert. Da wir jedoch selten mit diesen zu tun haben (werden), habe ich der Einfachheit halber hier nur den reellen Fall angeführt. 
# 
# Ebenfalls sind diese Metriken auf Teilmengen des $\mathbb{R}^n$ (bspw. $\mathbb{N}^n$ und $\mathbb{Z}^n$ ) und $\mathbb{C}^n$ definiert. 
# ```
# 
# 
# ```{admonition} $p < 1$
# :class: warning
# Es ist zwar möglich, hier $p \in (0, 1) $ zu wählen, jedoch verliert in diesem Fall die Dreiecksungleichung ihre Gültigkeit, da die Einheitssphäre dann nicht mehr konvex ist.  
# Deswegen ist für den Fall $p < 1$ die Minkowski-Distanz keine Metrik mehr und kein sinnvoller Abstand. 
# 
# Es wurde von manchen Autoren zwar behauptet, man könne durch Verwendung von den bei $p \in (0, 1) $ entstehenden Quasinormen in hoch-Dimensionalen Problemen bessere Klassifikationsergebnisse erzielen, was jedoch bei systematischer Prüfung nicht bestätigt werden konnte{cite:ps}`e22101105`.   
# ```
# 
# ```{admonition} Hinweis
# :class: note
# Die ursprüngliche Konzeption diente nicht dem Zweck eine Metrik zu definieren.
# 
# In der [ursprünglichen Veröffentlichung](https://gallica.bnf.fr/ark:/12148/bpt6k99643x/f128.item){cite:ps}`minkowski1910` wurde eine etwas andere Formulierung verwendet. Es handelt sich um die Minkowski-Norm zuzüglich eines Mittelungsfaktors; Ursprünglich wurde sie verwendet um die Minkowski'sche Ungleichung zu beweisen. 
# Diese Ungleichung ist eine Verallgemeinerung der Dreiecksungleichung für Lebesgue-Räume.
#  
# ```
# 

# ## wichtige Spezialfälle
# 
# ##### $p = 2$  (euklidische Distanz)
# Für $p =2$ ist die Minkowski-Distanz nichts anderes als die euklidische; Sie entspricht der "Luftlinie" beim Messen des Abstandes zweier Punkte und ist die für uns intuitivste. 
# 
# Die Sinnhaftigkeit und Interpretabilität des euklidischen Abstandes setzt jedoch voraus, dass der Pfad im gegebenen Raum wirklich durchschritten werden kann. 
# 
# ##### $p = 1$  (Manhattan)
# Für $p =1$ ergibt sich 
# \begin{equation*} \delta(x,y) = \sum_{i=1}^n |x_i - y_i| \end{equation*}
# , also die Summe der Betragsdifferenzen. 
# 
# Dies ist die aus der Summennorm induzierte, uns bereits bekannte Manhattan-Distanz. 
# 
# Sie ist der euklidischen Norm auf einem Gitter nicht unähnlich, aber eine viel sinnvollere wenn es keine durchquerbare "Luftlinie" im Raum zwischen den einzelnen Punkten gibt. Ihre Interpretabilität ist auch bei kategorischen Daten sehr gut, da sie auch in diesem Fall die Länge durchlaufbarer Pfade beschreibt. .
# 
# 

# ##### $p = \infty $  (Chebyshev Distanz)
# Für $p= \infty$ erhalten wir die Chebyshev-Distanz, die das Betragsmaximum der Koordinaten-Abstände darstellt.  
# 
# Die Chebishev Distanz "bestraft" im Gegensatz zur Manhattan Distanz Abstände in der Diagonale nicht. 
# 
# Diese Metrik wird bspw. in der Optimierung logistischer Systeme verwendet{cite:ps}`langevin2005logistics` . 

# ##### Vergleich der Metriken auf diskreten Gittern

# 
# ````{tabbed} Euklidisch
# ```{image} ../metrikenDE/egrid.svg
# ```
# ````
# 
# ````{tabbed} Manhattan
# ```{image} ../metrikenDE/mgrid.svg
# 
# ```
# ````
# 
# 
# ````{tabbed} Chebyshev
# ```{image} ../metrikenDE/cgrid.svg
# ```
# ````
# 
# 
# 
# 

# Es fällt auf, dass die Metriken auf den Achsen gleich sind, aber in der Diagonale jeweils andere Abstände liefern. 
# 
# Auch sind sich der euklidische und der Manhattan Abstand vom entstehenden Muster sehr ähnlich, der Chebyshev Abstand ein ganz anderes Muster liefert.

# ## Monotonie der Minkowski-Metriken
# 
# #### Monotonie
# Seien $1 \leq p < r \leq \infty, M \neq \emptyset \text{ und } x, y \in M $. 
# 
# Für die Minkowski-Metriken $\delta_p, \delta_r$ gilt dann:  
# 
# $$ \delta_r(x,y) \leq \delta_p(x,y) $$
#  
# Dies bedeutet, dass durch einen größerer p-Wert dem Abstand ein kleineren Wert zugewiesen werden kann. 
# 
# ```{admonition} kann $ \neq $ muss
# :class: warning
# Nicht alle Abstände werden gleich stark von dieser Monotonie beeinflusst und Abstände müssen sich nicht zwangsläufig ändern.
# Dies wird im nächsten Abschnitt visualisiert werden. 
# ```
# 

# #### Visualisierung der Monotonie
# 

# Beterachten wir nun, wie sich die Wahl von $p$ auf die Abstände auswirkt.

# 
# ```{raw} html
# :file: b.html
# ```
# 
# 

# ```{admonition} Wichtige Beobachtungen 
# :class: tip
# Abstände auf den Achsen ändern sich nicht. 
# 
# Die größte Änderung passiert bei einem Winkel von $45°$ zu einer Achse. 
# 
# Mit abnehmendem Winkel zur nähesten Achse nimmt die Änderung ab.
# 
# Die Abstände konvergieren gegen jene von $d_\infty$
# ```

# 
# ````{dropdown} beliebeige Abstände
# Die Monotonie gilt natürlich nicht nur für Abstände zum Null-Punkt. Anbei noch ein Beispiel zur Visualisierung der verringerung des Abstandes zwischen den Punkten [8,1.5] und [-2.5,7]
# ```{raw} html
# :file: b2.html
# ```
# ````

# ### Einheitssphären
# Unter Einheits-Kreisen (2D) und Sphären (3D und höher) versteht man die Mengen aller Punkte, dere Abstand zum Nullpunkt 1 ist.
# 
# Die unten generierten Plots basieren auf von mir erweiterten [Codes](https://mimmackk.github.io/unitball/) und Überlegungen von Kayden Mimmack{cite:ps}`unitsphereplot` 

# ````{tabbed} 2D
# 
# ```{raw} html
# :file: 2d.html
# ```
# 
# ````
# 
# ````{tabbed} 3D
# ```{raw} html
# :file: 3d.html
# ```
# 
# ````

# Die "Expansion" des Kreises oder der Kugel stellen die vorhin schon gezeigte Verringerung der Abstände; 
# das mit dem Volumen expandierende Innere der Sphäre sind alle Punkte, deren Abstand zu 0 kleiner als 1 ist. 
# 
# ```{admonition} Wichtige Beobachtung 
# :class: note
# Der euklidische Fall ($p = 2$) ist der einzige rotationsinvariante. 
# 
# Eine Rotation der Achsen in allen anderen Fällen könnte die Abstände zwischen Punkten verändern.
# ```

# ## Bedeutung von Metriken
# 
# Ein Beleg dafür, wie fundamental Distanz Metriken sind ist, dass sie für alle Formeln für Fläche, Volumen, Umfang, Länge usw. und sogar der Zahl $\pi$  grundlegend sind. 
# 
# Es ist einfach zu übersehen, dass $\pi $ als Verhältnis vom Unfang und Durchmesser eines Kreises definiert ist und Kreise Menge von Punkten sind, die alle den selben Abstand zu einem Zentrum haben. Der Abstandsbegriff ist hier implizit, und verschiedene Normen liefern uns verschiedene Werte.
# 
# Die Manhattan und Chebyshev Norm liefern uns mit $ \pi_1 = \pi_\infty = 4 $ die Maxima. Der uns geläufigere Wert von $\pi_2 = 3.1415...$ ist hierbei auch der Minimale. 
# 
# ```{image} ../metrikenDE/pis.svg
# ```
# 
# Für $p \in [1,2)$ sinkt der Wert von $\pi_p$ streng monoton, für $p \in (2, \infty)\cup \{\infty\} $ steigt er hingegen streng monoton und konvergiert zu 4. 
# 
# 
# 

# ```{admonition} Bedeutung für numerische Verfahren
# :class: tip
# Die Wahl von $p$ hat also interessante Implikationen. Da sie Abstände von Punkten, deren Verbindungsgerade nicht parallel zu einer Achse beeinflusst und größere Winkel stärker betrifft kann sie somit Punkte "näher rücken". 
# 
# Es ist auch zu bedenken, dass bei einer Verkleinerung geringer Abstände Rundungsfehler bedeutsamer werden.
# 
# Die relative Größe ist auch von Bedeutung, wenn Daten sehr Nahe aneinander sind, deren Abstand aber wichtig ist, weswegen der Manhattan-Abstand häufig im statistischen Lernen eingesetzt wird{cite:ps}`Goodfellow-et-al-2016`. 
# ```

# 
