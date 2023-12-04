<!-- .slide: class="center slide-title" -->

<h1 class="title">
Applying geophysical inversions to carbon mineralization
</h1>

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

### Geophysics: all about physical properties

<div class="r-stretch centered">

- Density
- Magnetic susceptibility
- Conductivity
- Wave velocity

</div>

---

## Physical properties affect fields

<div class="d-flex flex-row">
<div class="flex-1">
<img src="figs/prism-density-positive.png" alt="" style="width: 90; height:
auto;%">
</div>
<div class="flex-1">
<img src="figs/prism-density-negative.png" alt="" style="width: 90%; height:
auto;">
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


### Mid ocean ridges

<div class="r-stretch">
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

### Inverse problem

Given some **data** ($\mathbf{d}$), can we get a **model** of the subsurface?

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

<!-- .slide: class="center data-auto-animate" -->

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

---

### Real world data: Timmins, ON

Airborne gradiometry and magnetic data <!-- .element: class="font-s" -->

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

# My slides

---

<!-- .slide: class="center" -->

## This is another slide

<div class="centered r-stretch">

- with
- items

</div>

---

1. enumerate
2. lists

---

<!-- .slide: class="center" -->

# Code

```python
import harmonica as hm

hm.prism_gravity(coordinates, prisms, density, field="g_z")
```
