# Beweise 

(MinkowskiBeweise)=
## Minkowski-Metriken



#### $p=\infty $ 
Seien $x, y \in \mathbb{R} \text{ und } z:= x-y $. Sei ohne Beschränkung der Allgemeinheit $z_1$ der betragsmäßig größte Koeffizient von $z$. Dann: 

$$ \lim\limits_{p \rightarrow \infty} \left( \sum_{i=1}^n |x_i - y_i|^p  \right)^{\frac{1}{p}} = \lim\limits_{p \rightarrow \infty} \left( \sum_{i=1}^n |z_i|^p  \right)^{\frac{1}{p}} = \lim\limits_{p \rightarrow \infty}  \sqrt[p]{\left( \sum_{i=1}^n |z_i|^p  \right)}  = $$ 

$$ =  |z_1|  \lim\limits_{p \rightarrow \infty}  \exp \left( \frac{1}{p}  \log \left(1 + \frac{|z_2|^p}{|z_1|^p} + ... + \frac{|z_n|^p}{|z_n|^p} \right) \right) = $$

$$ = |z_1|  \exp(0) = |z_1| = max(|x_i - y_i|) $$

Dies folgt daraus, dass $\lim\limits_{p \rightarrow \infty} \frac{1}{p} \rightarrow 0 $ und dass $\log \left(1 + \frac{|z_2|^p}{|z_1|^p} + ... + \frac{|z_n|^p}{|z_n|^p} \right) $ beschränkt ist. 

_________________
## Andere Metriken

### Die Levshtein Distanz ist eine Metrik
Die **positive Definitheit** und **Symmetrie** sind offensichtlich; 

Eine Levenshtein Distanz von 0 kann nur Gleichheit bedeuten und da die Levenshtein Distanz durch Addition nicht-negativer Zahlen entsteht, kann diese auch nicht negativ sein. 

Die Umkehrung der Richtung bei der Überführung von Zeichenketten ineinander ändert nur die Reihenfolge, aber nicht die Anzahl nötiger Operationen. 

Dadurch, dass immer die geringste Anzahl an Änderungen ausgeführt wird und Veränderungen immer nur einzelne Zeichen betreffen ist die **Dreiecksungleichung** auch erfüllt. 

