#!/usr/bin/env python
# coding: utf-8

# ## Exkurs: das Dimensionsproblem
# 
# Es ist nicht nur die Wahl der Metriken, die Abstände oder deren Unterscheidbarkeit beeinflusst. Hochdimensionelle Räume haben einige sehr unintuitive Eigenschaften, die für uns jedoch relevant sind.

# ### Abstände zum Nullpunkt
# Betrachten wir die Abstände zum Nullpunkt von 5000 gleichverteilt aus der d-dimensionalen Einheitskugel gesampleten Punkten.
# 
# 
# ```{raw} html
# :file: fighist.html
# ```
# 
# Anfangs sieht die Verteilung nach einer Gleichverteilung aus, extreme Werte werden aber mit höherer Dimension immer seltener und die Abstände zum Nullpunkt rücken immer näher zusammen; die Abstände der gesampleten Punkte zueinander werden dadurch auch kleiner.
# 
# Das mag schon schlimm genug wirken, jedoch bedeutet dies auch, dass je höher die Dimension, desto wahrscheinlicher Daten sparse sind. 
# 
# Diese Entwicklung scheint jedoch zu einer Art Quasi-Normalverteilung hin zu konvergieren; In Dimensionen um und höher als 10 haben wir schon eine Art Normalverteilung, an der sich wenig nennenswertes ändert. 

# ### Unterscheidbarkeit der Abstände
# 
# Abstände in hohen Dimensionen sind schwerer zu unterscheiden. Das liegt daran, dass mit steigender Dimension Differenzen in den einzelnen Koordinaten immer weniger zu tragen kommen; da die koordinatenweisen Abstände nicht nach Größe gewichtet sind, werden größere Abstände "rausgemittelt".
# 
# Dies hat nicht nur negative Auswirkungen auf die Vergleichbarkeit sondern auch auf das Signal-Rausch-Verhältnis.
# 
# ```{admonition} Skalierung
# :class: warning
# Wir verwenden zwar oft Skalierung um Ausprägungen in vergleichbare Wertebereiche zu überführen und nicht eine Ausprägung stärker zu gewichten, 
# jedoch verschlimmert Skalierung das Problem der Unterscheidbarkeit. 
# 
# Besonders eine Stauchung der Werte auf dem Intervalll $[0,1]$, wie es mit dem MinMaxScaler üblich ist, ist für die Unterscheidbarkeit nachteilig und die Wahrscheinlichkeit von Rundungsfehlern wird erhöht. 
# ```

# ### Verhältnis Einheitssphäre und Einheitswürfel
# 
# Betrachten wir das Verhältnis zwischen Einheitssphäre udn Einheitswürfel (dem vom Intervall $[-1,1]$ auf jeder Achse aufgespanntem Hyperwürfel).
# 
# ```{image} ../metrikenDE/ratio.svg
# ```
# 
# Mit steigender Dimension konvergiert dieses gegen 0; das Volumen des Einheitswürfels wächst im Vergleich jenes der Einheitssphäre rasant.
# Hierbei ist zu beachten, dass die beiden immer gemeinsame Punkte auf den Achsen haben.
# 
# Je höher die Dimension ist, desto mehr Punkte befinden sich also in den "Ecken" außerhalb der Einheitssphäre. 
# 
# 
# ### Volumen in hochdimensionalen Räumen
# 
# Falls wir genauer untersuchen, wie sich die Volumen der Einheitssphäre und des Hyperwürfels verhalten, erhalten wir erneut überraschende Ergebnisse. 
# 
# Das extreme Wachstum des Hyperwürfelvolumens ist schon aus dem Verhältnis der Volumen ersichtlich, aber das Ausmaß möchte ich dennoch unterstreichen:
# ```{image} ../metrikenDE/HCvols.svg
# ```
# 
# Das Volumen der Einheitssphäre steigt hingegen überraschenderweise nur bis zur vierten Dimension und konvergiert danach gegen 0:
# ```{image} ../metrikenDE/USvols.svg
# ```
# 
# 
# 

# ### $p < 1$ zur Abhilfe?
# 
# Wie bereits erwähnt, wurde von manchen vorgeschlagen, über der Wahl des Parameters $p < 1$ die Differenzen zu maximieren. 
# 
# Dies ist jedoch nicht zielführend, da dann
# - die Dreiecksungleichung verletzt ist
# - Abstände verschieden stark betroffen sind und
# - die Größenordnungen aus dem Ruder laufen kann.
# 

# Betrachten wir ein paar Problempunkte ein wenig genauer:
# 
# ##### keine Metrik mehr
# Im Falle $p \in (0,1)$ verliert die Einheitssphäre ihre Konvexität und die Dreiecksungleichung gilt nicht mehr. 
# 
# Allgemeine Beweise dessen sind ein wenig aufwendig für nicht-Mathematiker zu vermitteln (da Konvexitätseigenschaften genutzt werden oder die Hölder-Ungleichung), ein anschauliches Beispiel ist deswegen glaube ich eher angebracht.
# 
# Seien also $p = \frac{1}{2}, x = \left[0,-\frac{1}{2}\right], y = \left[\frac{1}{2}, 0\right] \in \mathbb{R}^2$. Dann gilt:
# 
# $$\delta_p(x,y) = \left(\sum_{k=1}^2 \left| x_k -y_k \right|^p \right)^\frac{1}{p} =  \left(\sum_{k=1}^2 \sqrt{\left| x_k - y_k \right|} \right)^2 = \left(\sqrt{\frac{1}{2}} +\sqrt{\frac{1}{2}} \right)^2 = \sqrt{2}^2 = 2 $$
# 
# Aber es gilt weiteres, dass
# 
# $$\delta_p(x,0) =\left(\sum_{k=1}^2 \left| x_k \right|^p \right)^\frac{1}{p} = \sqrt{\frac{1}{2}}^2 = \frac{1}{2} = \delta_p(0,y)$$
# 
# und somit dass
# 
# $$1 = \delta_p(x,0) + \delta_p(0,y) < \delta_p(x,y) = 2$$
# 
# Das beduetet, dass die direkte Verbindung dieser Punkte einen größeren Abstand als der Umweg über den 0-Punkt liefert; die Dreiecksungleichung stimmt nicht und wir haben **keinen sinnvollen Abstandsbegriff** mehr. 
# 
# ##### Visualisierung der nicht mehr konvexen Einheitskreise
# 
# ```{raw} html
# :file: quasi.html
# ```
# 
# Hier merkt man wieder, dass die Punkte an der Diagonale wieder viel stärker betroffen sind. 
# 
# Das Ausmaß ist aber nicht ganz offensichtlich. Für $p= \frac{1}{4}$ hat bspw. $\left[\frac{1}{16},\frac{1}{16} \right]$ den selben Abstand zum Nullpunkt wie $[0,1]$ und $[1,0] $. Für die euklidische Distanz wäre es nur $0.088388$ und nicht $1$.
# 
# 
# ##### Größenordnungen
# 
# Sei $d \in \mathbb{N}_{>0}.$ Für $k \in \mathbb{N}_{>0} $ mit $k \leq d$ definiert $e_k = [0,0,...0,1,0,0,...0] \in \mathbb{R}^d $ den $k$-ten Einheitsvektor, der in der $k$-ten Koordinate 1 und an allen anderen Stellen 0 ist. 
# 
# Sei
# 
#  $$\mathbf{1}_d = \sum_{k=0}^d e_k$$
# und sei $\mathbf{0}_d = 0 \in \mathbb{R}^d$
# 
# Folgende Tabelle zeigt $d_p(\mathbf{1}_d, \mathbf{0}_d)$ für bestimmte $p<1$:
# 
# |    |   p=1 |   p=0.5 |   p=0.25 |           p=0.1 |      p=0.01 |
# |----:|------:|--------:|---------:|----------------:|------------:|
# |   **d = 1** |     1 |       1 |        1 |     1           | 1           |
# |   **d = 2** |     2 |       4 |       16 |  1024           | 1267650600228229401496703205376 |
# |   **d = 3** |     3 |       9 |       81 | 59049           | 5.15378e+47 |
# |   **d = 5** |     5 |      25 |      625 |  9765625 | 7.88861e+69 |
# |  **d = 10** |    10 |     100 |    10000 |   10000000000      | 1e+100      |
# 
# Um die Größenordnung hier in Kontext zu stellen, möchte ich daran erinnern, dass $\forall p \in (0, \infty) : \forall d \in \mathbb{N}_{>0} :\delta_p(e_k, \mathbf{0}_d) = 1$
# 

# ### Weitere Probleme, die uns hochdimensionale Räume bringen
# 
# Als wären Sparseheit und die schlechtere Unterscheidbarkeit nicht schlimm genug, haben hochdimensionale Räume weitere unvorteilhafte Eigenschaften. Mit steigender Dimension
# - sinkt die Performanz
# - erhöht sich der Ressourcenbedarf
# - sinkt die Interpretierbarkeit 
# 
# ### Mögliche Vorteile hoher Dimensionen
# 
# 

# 
