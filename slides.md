<!-- .slide: class="center slide-title" -->

<div class="r-stretch">
<h1 class="title">
Applying geophysical inversions to carbon mineralization
</h1>
</div>

<h2 class="authors">
Santiago Soler
</h2>

<h3 class="affiliation">
Geophysical Inversion Facility (GIF) - UBC
</h3>

<div class="logos">
<img src="figs/ubc-dark.png" alt="" style="max-width: 200px">
<img src="figs/gif-dark.png" alt="" style="max-width: 250px">
</div>

---

## Geophysics

<!-- - Gravity field -->
<!-- - Magnetic field -->
<!-- - Electromagnetic fields -->
<!-- - Mechanical waves propagation -->

<div class="d-flex flex-row">
  <div class="flex-1">
    <p class="font-s mb-0">Gravity field</p>
    <img src="/figs/gravity-earth.jpg" alt="" style="max-height: 350px">
  </div>
  <div class="flex-1">
    <p class="font-s mb-0">Magnetic field</p>
    <img src="/figs/earth-magnetic-field.jpg" alt="" style="max-height: 350px">
  </div>
</div>

<div class="d-flex flex-row">
  <div class="flex-1">
    <p class="font-s mb-0">Electromagnetic fields</p>
    <img src="/figs/skytem_view.jpg" alt="" style="max-height: 350px">
  </div>
  <div class="flex-1">
    <p class="font-s mb-0">Wave propagation</p>
    <img src="/figs/seismic-waves.jpg" alt="" style="max-height: 350px">
  </div>
</div>

---

<!-- .slide: class="center" -->

### Geophysics: all about physical properties

- Density
- Magnetic susceptibility
- Conductivity
- Wave velocity

---

## Physical properties affect fields

<div class="d-flex flex-row">
<div class="flex-1">
<img src="figs/prism-density-positive.png" alt="">
</div>
<div class="flex-1">
<img src="figs/prism-density-negative.png" alt="">
</div>
</div>


---


## What's in the subsurface?

<div class="r-stretch">
<div class="centered">
<img src="figs/surveys.svg" alt="" style="width: 70%">
</div>
</div>

---

### Gravity disturbances

<!-- Global bouguer map -->

<div class="r-stretch">
<img src="figs/earth-bouguer.png" alt="">
</div>


---

### Magnetic anomalies

<div class="r-stretch">
<img src="figs/earth-mag.png" alt="">
</div>

---

<!-- .slide: class="center slide-title" data-auto-animate -->

### Mid ocean ridges

<div class="centered">

<div>
<p>Gravity disturbances</p>
<img src="figs/ridge-gravity.png" alt="">
</div>

<div>
<p>Magnetic anomalies</p>
<img src="figs/ridge-mag.png" alt="">
</div>

</div>

---

<!-- .slide: class="center slide-title" data-auto-animate -->

### Mid ocean ridges

<div class="centered">

<div>
<img src="figs/oceanic-stripe.png" alt="" style="background: #eaeaea; padding: 0.5em;">
</div>

<div>
<p>Magnetic anomalies</p>
<img src="figs/ridge-mag.png" alt="">
</div>

</div>

---

### Forward problem

Given a **model** ($\mathbf{m}$) of the subsurface, we can <br>
_forward model_ the gravity or magnetic fields (**data** $\mathbf{d}$):

<div class="d-flex flex-row">

<div class="flex-1 d-flex flex-column justify-center">

`$$ \mathbf{d} = f(\mathbf{m}) $$`

</div>

<div class="flex-1">

<img src="figs/model-cartoon.png" alt="">

</div>

</div>

---

<!-- .slide: class="center" -->

### Inverse problem

Given some **data** ($\mathbf{d}$),
<br> can we get a **model** of the subsurface?

<div class="r-stretch">
<img src="figs/model-unknown-cartoon.png" alt="">
</div>

---

<div class="r-stretch">

<div class="centered">

<img src="figs/forward-inverse-chart.svg" alt="" style="width: 65%">

</div>
</div>

---

## Inverse problem

$$
  \operatorname*{min}\limits_{\mathbf{m}} \phi(\mathbf{m}) =
  \textcolor{#a6da95}{\phi_d}(\mathbf{m}) +
  \beta \textcolor{#ee99a0}{\phi_m}(\mathbf{m})
$$
$$
  \text{s.t.}
  \quad
  \phi_d \le \phi_d^*
  \quad
  ,
  \quad
  \mathbf{m}_L \le \mathbf{m} \le \mathbf{m}_U
$$


<div class="d-flex flex-row justify-center align-center gap-3 font-s">

<p style="color: #a6da95;">Data misfit:</p>

$$
  \phi_d(\mathbf{m}) =
  \lVert \mathbf{W}_d \left( \mathbf{d} - f(\mathbf{m}) \right) \rVert^2
$$

</div>

<div class="d-flex flex-row justify-center align-center gap-3 font-s">

<p style="color: #ee99a0;">Regularization term:</p>

$$
  \phi_m(\mathbf{m})
$$

</div>

---

<!-- .slide: class="center" -->

## Carbon mineralization

---

<!-- .slide: class="center" -->

<div class="r-stretch d-flex flex-column justify-center">

### Alterations

<img src="figs/reactions.svg" alt="" style="width: 100%;">

</div>

<div class="footnote">

Mitchinson et al. (2020)

</div>

---

<!-- .slide: class="center" data-auto-animate -->

### Physical properties of ultramafic rocks

<div class="d-flex flex-row justify-around align-center gap-1">

<div class="flex-1">
<img src="figs/phys-properties.png" alt="" style="padding: 0.1em; background-color: #eaeaea;">
</div>

<div class="d-flex flex-column align-start font-s">

**Loss of Ignition** (LOI):

- Proxy variable for alteration
- 5%-13%: **high** carbonation potential
- **Density** and **susceptibility** change with LOI

<p></p>

Serpentinized rocks with **good potential**:

- **Low** density
- ~**High** susceptibility

</div>

</div>

<div class="footnote">

Cutts et al. (2021).
doi: [10.1029/2021GC009989](https://doi.org/10.1029/2021GC009989)

</div>

---

<!-- .slide: class="center" data-auto-animate -->

### Physical properties of ultramafic rocks

<div class="d-flex flex-row justify-around align-center gap-1">

<div class="flex-1">
<img src="figs/phys-properties.png" alt="" style="padding: 0.1em; background-color: #eaeaea;">
</div>

<div class="flex-1">
<img src="figs/cross-plot-phys-props.png" alt="" style="width: 80%;">
</div>

</div>

<div class="footnote">

Cutts et al. (2021).
doi: [10.1029/2021GC009989](https://doi.org/10.1029/2021GC009989)

</div>

---

### Real world data: Timmins, ON

Airborne gravity gradiometry and magnetic data <!-- .element: class="font-s" -->

<div class="r-stretch">

<div class="d-flex centered flex-row justify-center">

<div class="flex-2">
<img src="figs/timmins-data-maps.png" alt="">
</div>
<div class="flex-1">
<img src="figs/ontario-map.png" alt="">
</div>

</div>

</div>

<div class="d-flex justify-end flex-row">
<img src="figs/canada-nickel.png" alt="">
</div>

---

### Inversion of magnetic data

<div class="r-stretch">
<div class="centered">
<img src="figs/l2-mag-result.png" alt="" style="width: 90%">
</div>
</div>

---

### Inversion of gravity data

<div class="r-stretch">
<div class="centered">
<img src="figs/l2-gravity-result.png" alt="" style="width: 90%">
</div>
</div>

---

### Inversion of gravity data

<div class="r-stretch">
<div class="centered">
<img src="figs/l2-gravity-results-highlighted.png" alt="" style="width: 90%">
</div>
</div>

---

### Cross plot of physical properties

<div class="r-stretch">
<div class="centered">
<img src="figs/l2-cross-plot.png" alt="" style="height: 80%">
</div>
</div>

---

### Estimations of carbonation potential

<div class="r-stretch">
<div class="centered">
<img src="figs/l2-potential-estimation.png" alt="" style="height: 80%">
</div>
</div>

---

### Estimations of carbonation potential

<div class="d-flex justify-center" style="height: 100vh">
<iframe src="figs/3d-plot-l2-distance.html" frameborder="0" style="height: 100%; width: 100%;"></iframe>
</div>

---

<!-- .slide: class="center" data-visibility="hidden" -->

<h2> Is this model <em class="green">the truth</em>? </h2>

### Not necessarily! <!-- .element: class="fragment" -->

<br>


<ul>
  <li class="fragment">
    Inversions are <strong class="orange">ill-posed problems</strong>:
  <ul>
    <li class="fragment"> Non-unique solution </li>
    <li class="fragment"> Small changes in the model can lead to large changes in the data </li>
  </ul>
  </li>
</ul>

---

<!-- .slide: class="center" -->

<h2> Is this model <em class="green">the truth</em>? </h2>

### Not necessarily! <!-- .element: class="fragment" -->

<br>

<p class="fragment">
  Inversions are <strong class="orange">ill-posed problems</strong>:
  <br>
  Non-unique solution
<p>

---

<!-- .slide: class="center" -->

### Changing the regularization term

$$
  \operatorname*{min}\limits_{\mathbf{m}} \phi(\mathbf{m}) =
  \textcolor{#a6da95}{\phi_d}(\mathbf{m}) +
  \beta
  \underbrace{
    \textcolor{#ee99a0}{\phi_m}(\mathbf{m})
  }_{\mathclap{\text{\textcolor{#ee99a0}{regularization term}}}}
$$


<div class="d-flex flex-row justify-center align-center gap-3 font-s">

<p><span class="orange">L<sub>2</sub></span> norm:</p>

$$
{\phi_m^2}(\mathbf{m}) =
\lVert
\mathbf{W}_s (\mathbf{m} - \mathbf{m}_\text{ref})
\rVert^{\textcolor{#c44500}{2}}
$$

</div>

<div class="d-flex flex-row justify-center align-center gap-3 font-s">

<p>Sparse (<span class="orange">L<sub>p</sub></span>) norm:</p>

$$
{\phi_m^2}(\mathbf{m}) =
\lVert
\mathbf{W}_s (\mathbf{m} - \mathbf{m}_\text{ref})
\rVert^{\textcolor{#c44500}{p}}
,\quad
p \in [0, 2)
$$

</div>

---

<!-- .slide: class="center" -->

<div class="d-flex flex-row">

<div class="flex-1">
<p>L2 inversion result</p>
<img src="figs/l2-potential-estimation.png" alt="">
</div>

<div class="flex-1">
<p>Sparse inversion result</p>
<img src="figs/sparse-potential-estimation.png" alt="">
</div>

</div>

---

<div class="r-stretch centered flex-column">
<div>

### Petrophysically Guided Inversion (PGI)

Including petrophysical data in the inversion

<div class="d-flex flex-row justify-center align-center">

<div class="flex-1">
<img src="figs/pgi-cross-plot.png" alt="">
</div>
<div class="flex-2">
<img src="figs/pgi-membership.png" alt="">
</div>

</div>

</div> <!-- unclassed div -->
</div> <!-- r-stretch -->

<div class="footnote">

Astic et al. (2019, 2020):
[10.1093/gji/ggz389](https://doi.org/10.1093/gji/ggz389)
and
[10.1093/gji/ggaa378](https://doi.org/10.1093/gji/ggaa378)

</div>

---

<!-- .slide: class="center slide-conclusions" -->

## Conclusions

- **Geophysical inversions** allow us to **estimate CO<sub>2</sub> sequestration potential** of serpentinized rocks
- Not a silver bullet: different inversion results provide different knowledge.
- **Geologic interpretation** of the inversion results is crucial to better
  understand the subsurface.

---

<!-- .slide: class="center" -->

## Open-source software

<img
src="figs/stack-logos/geopython-stack.svg"
alt=""
style="width: 100%; margin-top: 1em; background-color: #eaeaea; padding: 1em;">

---

<!-- .slide: class="center" -->

# Thank you!

