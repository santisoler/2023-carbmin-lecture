<!-- .slide: class="center" -->

# Applying geophysical inversions to carbon mineralization

## Santiago Soler

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

<!-- Cartoon of dense object and gravity anomaly -->

<!-- Cartoon of sus object and magnetic anomaly -->

---

## What's in the subsurface?

- Geophysical surveys

---

### Gravity data

<!-- Global bouguer map -->

---

### Magnetic data

<!-- Global magnetic anomaly -->
<!-- Maybe zoom in the mid-ocean ridge -->

---

## Forward model

<iframe class="d-flex flex-row justify-center" src="figs/3d-plot-l2-distance.html" frameborder="0" style="width: 100%; height: 100vh;"></iframe>

---

### Inverse model

---

## Carbon mineralization

---

### Physical properties of ultramafic rocks

<!-- plots of cutts, see slides -->

---

### Real world data: Timmins, ON

<!-- maps -->

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
