#!/usr/bin/env python
# coding: utf-8

# # Andere Metriken
# 
# Dieses Kapitel ist einigen wenigen, aber für die Data Science und das statistische Lernen wichitige Metriken. 

# ## Metriken für nicht-numerische Objekte
# ### Metriken für Zeichenketten 
# #### Hamming Distanz
# 
# Die Hamming Distanz zählt die Anzahl an Abweichungen zwischen zwei Elementen eines Raumes. Sie ist für $x, y \in M \neq \emptyset$ als
# 
# $$ \delta_H (x,y) = |\{i: x_i \neq y_i\}|  $$
# 
# definiert. 
# 
# 
# Dadurch lässt sie sich auch für nicht-numerische Daten wie bspw. Wörter anwenden und findet häufig Anwendungen in Fehlersuche{cite:ps}`4348227`  und natural language processing. 
# 
# Die Hamming Distanz findet ebenfalls Anwendung in der DNA-Sequenzanalyse{cite:ps}`sequence`.
# 
# 
# ```{admonition} $d_h$ ist eine Metrik
# :class: note
# Die Hamming Distanz ist für Elemente gleicher Länge eine Metrik, da sie alle Eigenschaften einer erfüllt{cite:ps}`robinson2003`. 
# ```
# ```{admonition} Interpretabilität
# :class: tip
# $\delta_H$ ist sehr gut für rein-kategorische Daten geeignet und macht am meisten Sinn, wenn diese nur zwei Ausprägungen haben oder kein sinnvoller Abstand zwischen den Ausprägungen gebildet werden kann.
# 
# Beispiel hierfür wäre ein Risikogruppen-Klassifikations-Datensatz der Informationen zu Geschlecht, Hautfarbe, Augenfarbe, Haarfarbe und einem binären Merkmal, ob Verwandte an Hautkrebs erkrankt sind, enthält. 
# 
# ```
# 
# ```{admonition} unintuitive Eigenschaften
# :class: warning
# Für die Hamming Distanz zählen nur die Anzahl der Abweichungen, nicht deren Größe(nordnung)! Auf einer Ebene hätten die Punkte 
# $[-\infty ,0]$ und $[\infty, 0]$ beide Abstand 1 zueinander, zum Nullpunkt und zu jedem Punkt auf der Gerade zwischen ihnen. 
# 
# Der Einheitskreis der Hamming Metrik in reellen Räumen mit Dimension $d \geq 2$ sind die Achsen. Alle anderen Punkte hätten Abstand $d$ zum Nullpunkt. 
# ```
# 
# #### Levenshtein Distanz
# Die Levenshtein Distanz ist auch als Editierdistanz bekannt und beschreibt die minimale Anzahl an nötigen Modifikationen an einer Zeichenkette, um sie in eine andere Zeichenkette zu überführen. 
# 
# Die Modifikationen können Löschung, Hinzufügen oder Ersetzen von Zeichen sein.
# 
# 
# Seien $a, b$ Zeichenketten mit Längen $|a|, |b|$. Dann ist die Levenshtein Distanz für sie als 
# 
# $$
# 
# \delta_L(a,b) = \begin{cases} 
# |a| & \text{falls } |b| = 0 \\
# |b| & \text{falls } |a| = 0 \\
# \delta_L(a_{1,2,...,|a|}, b_{1,2,...,|b|}) & \text{falls } a_0 = b_0 \\
# 1+ \min \begin{cases}
#         \delta_L(a_{1,2,...,|a|}, b) \\
#         \delta_L(a, b_{1,2,...,|b|})  \hspace{3cm} \text{sonst} \\
#         \delta_L(a_{1,2,...,|a|}, b_{1,2,...,|b|}) \\
#         \end{cases}
#     
# \end{cases}
# 
# $$
# 
# definiert. 
# 
# Die Definiton ist rekursiv und die Berechnung der Distanz geschieht meistens über Matritzen. (Eine genauere Ausführung wird in späteren Versionen dieses JupyterBooks folgen)
# 
# 
# Die Levenshtein Distanz wird häufig für unscharfe Suchen, Rechtschreibprüfungen und Duplikatssuche verwendet, findet aber auch in der Linguistik zur Ähnlichkeitsanalyse von Sprachen{cite:ps}`thije2007receptive` gebrauch. 
# 
# ```{admonition} Hamming vs Levenshtein Distanz
# :class: tip
# Die Hamming und Levenshtein Distanz können für manche Zeichenketten zwar die selben Abstände liefern, tun es aber im allgemeinen nicht. So ist bspw 
# $d_H(\text{abcdefg}, \text{bcdefgh}) = 7 \neq 2 = d_L(\text{abcdefg}, \text{bcdefgh})$
# 
# Im Gegensatz zur Levenshtein Distanz, lässt die Hamming Distanz nur Ersetzungen zu.
# 
# Die unintuitiven Eigenschaften der Hamming Distanz sind jedoch auch der Levenshtein Distanz eigen. 
# ```
# 
# ```{admonition} Erweiterungen der Levenshtein Distanz
# :class: note
# Es gibt zwar Erweiterungen wie die Damerau–Levenshtein-Distanz, die auch Transposition von Zeichen erlaubt, jedoch ist diese keine Metrik mehr, da sie die Dreiecksungleichung im Allgemeinen nicht erfüllt.
# 
# Auch die fälschlicherweise "Jaro-Winkler-Metrik" genannte Jaro-Winkler-Distanz, die nur Transpositionen zulässt, ist keine Metrik, da sie gegen die Dreiecksungleichung verstößt.
# 
# ```
# 
# #### Longest common subsequence
# ##### Motivation
# In der Sequenzanalyse ist in manchen Anwendungen (bspw. Linguistik und Bioinformatik) die Ähnlichkeit interessanter als der Abstand. Ein Ähnlichkeitsmaß ist die längste gemeinsame Teilsequenz. 
# 
# Teilsequenzen sind allgemeiner als Teilzeichenketten, da die Zeichen nicht nebeneinander liegen müssen; z.B.: ist TAGTACC die längste gemeinsame Teilsequenz der Zeichenketten A**T**GA**GT**C**AC**T**C** und **TA**C**G**CC**TACC**. 
# 
# ##### Definition
# Seien $a,b$ Zeichenketten der Längen $|a|, |b|$ mit $|a|>0$ oder $|b| > 0$ und einer längsten gemeinsamen Teilsequenz $c$. Dann ist 
# 
# $$ \delta_{LSC}(a,b) = 1 - \frac{|c|}{\max(|a|,|b|)} $$
# 
# eine Metrik. 
# 
# Die Definiton dieser geht auf Daniel Bakkelund{cite:ps}`bakkelund2009lcs`  zurück. 
# 
# Informell ausgedrückt wird hier gemessen, inwieweit sich die längste gemeinsame Teilsequenz von der längsten Zeichenkette unterscheidet; der Wertebereich ist immer $[0,1]$
# 
# ```{admonition} Vergleich zur Levenshtein Distanz
# :class: note
# Im Gegensatz zur Levenshtein Distanz ist bei der LSC-Problemstellung nur die Löschung erlaubt.
# 
# ```
# 

# ### Metriken für Mengen
# 
# #### Distanz zweier Teilmengen des $\mathbb{R}^d$
# 
# Seien $M, N \subset \mathbb{R}^d$. Dann ist die Distanz zwischen diesen für eine Metrik
# $\delta : \mathbb{R}^d \times \mathbb{R}^d \rightarrow \mathbb{R} $
# als 
# $$\delta_S(M,N) = \inf_{\substack{x \in M \\ y\in N}} \delta(x,y)$$
# definiert.
# 
# Dabei ist das Infimum $\inf$ die größte untere Schranke. Im Falle, dass das Minimum angeommen wird, sind Infimum und Minimum gleich.
# 
# ```{admonition} gegebenenfalls keine Metriken!
# :class: warning
# Die oben angeführte Funktion ist zwar für allgemeine Mengen definiert, jedoch nur eine Metrik, falls $M \cap N  \in \{ \emptyset, M, N \} $, also wenn die Mengen keine gemeinsamen Punkte haben oder eine Teilmenge der anderen ist.  
# ```
# ```{admonition} Eindeutigkeit
# :class: warning
# Wie erwähnt liefern uns verschiedene Metriken andere Distanzen, weswegen sich die Infima für verschiedene Metriken unterscheiden können. Die Distanz zweier Teilmengen des $\mathbb{R}^d$ ist deswegen nicht eindeutig. 
# ```
# 

# 

# 
