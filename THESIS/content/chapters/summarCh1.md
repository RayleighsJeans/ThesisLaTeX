# Chapter 1: Bolometry at W7-X - Summary

## Overview
Comprehensive technical chapter describing the W7-X bolometer diagnostic system: design, construction, measurement principles, calibration procedures, and data analysis methods for measuring plasma radiation power.

## Chapter Structure (854 lines)

### 1. Introduction (lines 1-11)
**Etymology:** Bolometer from Greek βολή (beam) + μετερ (measure)
**History:** Invented by Samuel Pierpont Langley (1878), used for infrared measurements at Allegheny Observatory
**Applications:** Particle detectors, cosmic radiation (Herschel, SOFIA), thermal cameras (microbolometers)

### 2. Overview (Section, lines 12-38)

#### Purpose and Requirements (lines 14-16)
- Measure spatial and temporal evolution of irradiated power
- Spectral range: infrared to soft X-ray
- Must withstand: temperature changes, thermal loads, neutron radiation, EM fields, pressure perturbations
- Critical: consistency, reliability, accurate geometry (for tomographic inversion)
- In-situ calibration capability essential
- Long-distance signal transfer in noisy environment

#### Detector Species (Subsection, lines 18-38)

**Metal Resistor Bolometer (lines 23-26):**
- Most common in fusion devices
- Thin metal film absorbers on non-conductive thermal transmission layers
- Optional carbon coat for IR enhancement
- Advantages: operational reliability, resilience, low sensitivity to perturbations

**AXUV Bolometer (lines 28-31):**
- P-n junction photodiodes
- Spectral range: UV to X-ray
- Very fast temporal response
- Limitations: nonlinear frequency response, degradation in fusion environments, not for absolute measurements
- Used complementary to resistive systems for fast events

**IRVB/SIB Bolometer (lines 33-36):**
- Single large metal foil behind slit aperture/pinhole
- IR camera measures temperature from backside
- SIB: clamped between copper masks
- IRVB: no masks (40% more detector area, no shadowing)
- Requires 2D heat transport equation solution
- Good spatial/temporal resolution
- Drawbacks: complicated diffusion modeling, spectral sensitivity

**W7-X Choice:** Metal resistor bolometer most promising for long-term D-T reactor operation

### 3. W7-X Bolometer Diagnostic (Section, lines 40-544)

#### 3.1 Requirements (Subsection, lines 51-64)

**W7-X Specifications:**
- Steady-state: 10 MW ECRH at 140 GHz for 30 min
- Non-absorbed microwave: 1 MW (90 kW/m² stray radiation)
- Thermal load: multiple 10 kW/m² on plasma-facing components
- Baking: RF discharge at ~150°C
- Neutron resilience for D-T operation

**Design Constraints:**
- Cylindrical insertion port
- Wide spectral absorption (visible to soft X-ray)
- Minimal servicing requirements
- Accurate line of sight geometry

#### 3.2 Construction (Subsection, lines 66-99)

**Detector Chip (Fig. 1.1, 1.2):**
- Absorber: 3.8×1.3 mm, 5 mm² area
- Layers (bottom to top):
  * 5 μm Si₃N₄ substrate
  * 5 μm gold film
  * 0.6 mm Si front plate frame
  * 150 nm aluminum layer
  * 50 nm carbon coat
- Two 1 kΩ Pt meanders for Wheatstone bridge
- 4 measurement + 4 reference absorbers per chip
- Reference absorbers hidden behind solid Si frame
- Pressure equilibration holes near reference foils

**Alternative Absorbers:**
- Be or Al covered for soft X-ray analysis (high-Z impurities)

**Camera Assembly (Fig. 1.3):**
- Two cameras: Horizontal (HBC) and Vertical (VBC)
- Each camera: multiple 32-channel detector arrays
- Graphite front plate with pinholes
- Rotary shutter between pinhole and detectors
- Water cooling (coupled to W7-X central system)
- Pt100 thermometer for temperature monitoring
- Group heads: 4 channels per unit, fan-shaped arrangement

**Data Acquisition:**
- 40 m shielded UHV cables
- LEMO® 10-pole connectors
- 4 master PCBs, 32 DAQ cards each (128 channels total)
- ADC: AD7730 (National Instruments)
- NI 7813R FPGA controller
- LabVIEW software control
- Data: RAM → local HDD → W7-X archive

#### 3.3 Line of Sight Geometry (Subsection, lines 101-167)

**Camera Locations (Fig. 1.4):**
- Both at ~108° toroidally (triangular plane)
- HBC: outer side, horizontal view
- VBC: below, vertical view
- Intrinsic tilt: 68.75° → ~5° toroidal extension

**Camera Specifications:**
- HBC: 32 channels (one subarray design)
- VBC: 2×24 channels (48 total, overlapping at poloidal center)
- Aperture-detector distances:
  * HBC: 175 mm
  * VBC: 84 mm
- Viewing angles:
  * VBC: 53°
  * HBC: 138°

**Aperture Design:**
- HBC: single 5×10 mm (50 mm²) pinhole
- VBC: two separate apertures for VBCl and VBCr
- Detectors elongated in toroidal direction
- Individual chip angling toward pinhole for maximum optical transmission

**Transmission Function (Fig. 1.5, 1.6):**
- d < a (detector smaller than aperture) → triangular LoS cone
- Partial shadowing at detector edges
- Etendue K̃_M calculation [Eq. 6]:
  K̃_M = ∬(cos α cos β)/(4πd²) dA_M dA_A

**Etendue Analysis (Fig. 1.7):**
- Normalized transmission maps for detector pairs
- Partial shadowing impact on outermost parts
- Maximum transmission at detector center
- Gradients vary with orientation

#### 3.4 Bolometer Equations (Subsection, lines 168-375)

**Measurement Principle (lines 173-199):**

**Wheatstone Bridge (Fig. 1.8, 1.9):**
- Measurement (M) and Reference (R) resistors
- AC excitation: U_ex = 5 V at adjustable kHz frequency
- Bridge imbalance: ΔU/U_ex ≈ ΔR/(2R) [Eq. 7]
- DC coupling avoided (1/f noise)
- Signal-to-noise doubled (both R_M change simultaneously)

**Temperature-Power Relation [Eq. 8, 9]:**
```
ΔT = 2ΔU/(αU_ex)
κ(dΔT/dt) = P_bol - κΔT/τ
P_bol = (2Rκ)/(U_ex R̂τ)(ΔU + τ dΔU/dt)
```
- κ: heat capacity
- τ: cooling time
- R̂: temperature coefficient of resistance

**Signal Example (Fig. 1.10):**
- Power stage response shows gain + time derivative
- Sum reconstructs input power

**Calibration (lines 220-285):**

**Ohmic Heating Method (Fig. 1.11, 1.12):**
- Two voltage stages: U_cal = 1.2 V and 2.5 V (each 1.6 s)
- Measures baseline current I₀
- Resistance from equilibrium [Eq. 10]:
  R_M = 2(U_cal/(I(∞) - I₀) - R_L - R_C)
  - R_L = 10 Ω (load resistor)
  - R_C = 40 Ω (cable resistance)

**Cooling Time [Eq. 11]:**
```
ΔI(t) = -ΔI(0)[1 - exp(-t/τ_M)]
```
- Exponential decay fit yields τ_M and ΔI(0)
- First few ms excluded from fit (initial response dominated by substrate)

**Heat Capacity [Eq. 12, 13]:**
```
κ_M = ΔI⁴(0)/(4I(∞)(I(∞) - I₀))
```

**Calibration Results (Fig. 1.13):**
- Small groups of 4 consecutive detectors show composition similarities
- Channel 32 shows low κ (thermal contact issue)

**Temperature Effects (lines 272-285):**
- Drift: 50-150 μV/K depending on composition
- Pressure sensitivity: 2-8 W/(m²·Pa) for ΔP up to 20 Pa
- W7-X pressure: ~10⁻² Pa (negligible)
- Grey body radiation from camera housing: ∝ εAΔT⁴
- Water cooling perturbations cause signal drifts (Fig. 1.14)
- Future: temperature-dependent calibration lookup tables

**Radiation Power Measurement (lines 287-375):**

**Line Radiation [Eq. 14]:**
```
P_rad ∝ ∫_LoS Σ_Z n_e n_Z L_Z(T_e, T_i, T_Z, ...) dl/(4π)
```

**Bolometer Equation [Eq. 15, 16]:**
```
P̃_M = (2/V_eff)(R_M + 2R_C)κ_M√g_C(τ_M dΔU_M/dt + f_τ ΔU_M)
```

**Parameters:**
- V_eff = 5V · R_M/(R_M + 2R_C)
- g_C = 1 + (ω(R_M + R_C))²
- β = (1 - (ωR_M)² + (ωR_C)²)/(1 + (ω(R_M + R_C))²)
- ω = 2πf_bridge C_C
- f_τ = 1 - V_eff²β/(4κ_M(R_M + R_C)²)
- f_bridge = 625 or 1250 Hz
- C_C = 2 nF

**Typical Values [Eq. 17]:**
- R_M ≈ 1 kΩ, τ_M ≈ 110 ms, κ_M ≈ 0.8 mW/kΩ
- P̃_M ≈ 25.74 W/V(dΔU_M + 0.014ΔU_M)
- ΔU ~ 10⁻³ V, dΔU ~ 10⁻⁵ V
- Raw signal dominates, but derivative important for transients

**Signal Corrections:**

**Offset [Eq. 18]:**
```
V_off = (1/(t₂-t₁))∫[t₁ to t₂] ΔU_M(t)dt,  t₁ < t₂ < T₀
```

**Drift [Eq. 19, 20]:**
- Linear fit: f(t, β₁, β₂)
- Least squares minimization
- V_drift(t) = β₁·t + β₂ for t₁ < t < t₂

**Filtering [Eq. 21]:**
- Savitzky-Golay polynomial (order p, width N)
- Boxcar filter (moving mean, width N)
- Convolution: ΔŨ_M,j = Σc_i ΔU*_M,j+i

**Final Form [Eq. 22]:**
```
F_M = (2τ_M/V_eff)(R_M + 2R_C)κ_M√g_C
f_M = f_τ/τ_M
P_M = F_M(dΔŨ_M/dt + f_M ΔŨ_M)
```

#### 3.5 Performance (Subsection, lines 376-544)

**Spectral Efficiency (Fig. 1.15, 1.16):**
- Gold absorber: unity efficiency 600-0.2 nm
- Reflectivity reduced by carbon coating
- Sensitivity: 200 nW
- Absolute calibrated measurements possible
- Si frame + Al layer: thermal diffusion to camera housing
- Max temperature: 250°C

**Microwave Protection (Fig. 1.17):**
- Wire mesh: 90 μm thickness, 0.24 mm spacing
- Ceramic TiO₂/Al₂O₃ coating on camera interior
- CuBe springs for tight front plate fit
- MISTRAL tests: 3% of 10 mW per detector → <0.1 mW
- Expected 10 kW/m² stray → 0.04 μW on detector (negligible)

**ADC Specifications (lines 417-424):**
- Range: ±80 mV (16-bit) → 2.44 μV resolution
- Minimum: ±10 mV → 0.31 μV resolution
- Master clock: 4.9152 MHz
- FPGA latency: 10-100 ns
- Sample times: {0.8, 1.6, 3.2, 6.4, 12.8} ms
- ΔT_sample = 0.0095 ms, Δf_sample = 0.0254 kHz

**Signal-to-Noise (lines 425-436):**
- Noise background: 0.5-6 μV (no radiation)
- SNR ≥ 1000 (30 dB) in high radiation scenarios
- Median ΔU during discharge >> drift and noise

**Operational Statistics OP1.2b (Fig. 1.18, 1.19, Tables 1.1, 1.2):**
- 61 functional detectors
- 1182 experiment programs

**Calibration Parameters (Fig. 1.18):**
- Resistance: median 0.987 kΩ, deviation 0.011 kΩ
- Heat capacity: median 0.724 A², deviation 0.0545 A²
- Cooling time: median 110.57 ms, deviation 4.93 ms
- Offset: median 0.204 μV, deviation 31.11 μV
- Small plateaus = individual experiment days
- Collective variations indicate calibration/temperature issues

**Acquisition Performance (Fig. 1.19):**
- Std deviation: median 0.339 μV, deviation 12.586 μV
- Drift: median 0.057 μV/s, deviation 27.621 μV/s
- Median signal: 0.042 mV, deviation 0.032 mV
- Maximum: 1.186 mV, deviation 3.704 mV
- Noise ~2× minimum voltage resolution
- 10 s acquisition → 50 μV baseline offset
- Spikes: water cooling perturbations, power supply issues

**Error Analysis (Table 1.3, Eq. 23):**
- Gaussian error propagation
- s_P_M = 1.599 μW
- Small compared to typical >0.1 mW measurements

**Summary:** SNR > 1000 at high temporal resolution, performs within specifications

### 4. Plasma Radiation Power (Section, lines 546-854)

#### 4.1 Global Power (Subsection, lines 552-637)

**Irradiating Volume:**
- EMC3-EIRENE simulations: r_eff = 1.35 r_a
- Total volume: 1.82 V_LCFS (182%)
- W7-X assumption: V_P,tor = 1.3² V_LCFS = 1.69 V_LCFS
- Volumetric factor f_P = 1.3² (scaling factor for P_rad)

**Radiation Fraction [Eq. 24]:**
```
f_rad = P_rad/P_H
```

**Domain (Fig. 1.20):**
- Must accommodate all LoS
- Outermost channels should yield P_M ≈ 0
- Important for tomographic boundary conditions

**Etendue-Power Relation [Eq. 25, 26]:**
```
P_rad,M = ∭ g_rad(r⃗)/K̃_M(r⃗) dr⃗
K_M = K̃_M · L_M
P_rad,M = P_M/K_M  (chord brightness)
```

**Global Radiation Power [Eq. 27]:**
```
P_rad = P_rad,C = (V_P,tor/V_C) Σ_M (P_M V_M/K_M)
```
- V_C = Σ_M V_M (total LoS volume in camera plane)
- C ∈ {HBC, VBC}

**Volumes and Etendues (Fig. 1.21):**
- All cameras contribute similar LoS volumes
- VBC etendues ~2× larger than HBC (pinhole design)

**Example (Fig. 1.22):**
- XP20181010.36: He beam density control, 5.72 MW ECRH
- P_M(HBC) ≈ 0.5 P_M(VBC) (larger distance)
- P_rad,HBC and P_rad,VBC agree within 5%
- Poloidally asymmetric scenarios: larger deviations

**Accuracy:**
- 5% error for global P_rad (from diagnostic comparisons)
- Potential 25% error from neglected main chamber radiation
- Alternative: calculate volume from measured radial profile boundaries

#### 4.2 Local Power (Subsection, lines 639-779)

**Chord Brightness Profile (lines 644-721):**

**Grid Construction (Fig. 1.23):**
- 2D grid: (r, θ) from magnetic axis or (r, z) cylindrical
- Domain: 1.3² V_LCFS
- Typical: N_r = 20, N_θ = 150
- Radial width: Δr = 1.3r_a/N_r
- Poloidal: Δθ = 2π/N_θ
- Extended ±2.5° toroidally for LoS cone width
- Grid from VMEC flux surfaces projected to bolometer plane

**Voxels and Pixels:**
- Voxel v^(i,j,k): 6-sided polyhedron
- Pixel p^(i,j): collapsed voxels (sum over k)

**Geometrical Contribution [Eq. 28]:**
```
T^(i,j)_M = Σ_k T^(i,j,k)_M = Σ_k (∫_M L^(i,j,k)_M dK̃_M)
```
- T^(i,j)_M: local sensitivity of absorber M to pixel p^(i,j)
- L^(i,j,k)_M: LoS length through voxel v^(i,j,k)
- Convolution of etendue and LoS length
- VBC: ~2× larger T than HBC (larger etendues)
- VBC arrays overlap → further increased local sensitivity

**Effective Radius [Eq. 29]:**
```
r_eff,M = {
  argmin(r_eff^(i,j)) for T^(i,j)_M > 0     (a)
  Σ(T^(i,j)_M r_eff^(i,j))/Σ T^(i,j)_M      (b)
}
```
- Method (a): minimum radius along LoS
- Method (b): weighted by local sensitivity
- Sign convention distinguishes outboard/inboard, upside/downside

**Effective Radius Results (Fig. 1.24):**
- Method (a): nearly linear spectrum
- Method (b): represents most sensitive radial position
- All cameras cover plasma center, but weighted r_eff doesn't show this

**Chord Profile [Eq. 30]:**
```
P_chord,M = P_rad,M = P_M/(Σ_i Σ_j Σ_k T^(i,j,k)_M)
```
- Average power per volume along LoS
- Average brightness along LoS

**Example (Fig. 1.25):**
- XP20180725.44: high mirror config, 1.3 MW ECRH
- Top: combined profiles at t = 3.0 s
- HBC covers entire volume, VBC slightly reduced
- Error bars small for r_eff,M ∈ (-1.0, 1.0)
- Cameras generally agree within LCFS
- Small differences at separatrix
- Bottom: rapid inward transition 3.1-3.35 s

**Radial Profile and Tomography (lines 723-779):**

**Tomographic Challenge:**
- Ill-posed/under-constrained problem
- Free parameters (pixels) >> constraints (LoS)
- Requires regularization and a priori information

**Radon Transform [Eq. 31]:**
```
Rf_L = ∫_L f(x,y)dL
f(r,θ) = ∫₀^π ∫_{-∞}^∞ Rf(r',θ)·h(r-r')dr'dθ
```
- Filtered back-projection formula
- h(r): highpass filter (convolution function)
- Fourier transform: F̂h(ω) = |ω|

**Fourier Domain [Eq. 32]:**
```
f(r,θ) = ∫₀^π F⁻¹(FRf_L(ω)|ω|k(ω))dθ
```
- k(ω): window function (regularization, noise suppression)
- Not suitable for W7-X (ill-posed, can't correct geometry errors)
- Replaced by iterative solvers

**Tikhonov Regularization [Eq. 33]:**
```
T·x⃗ = b̂⃗
η = x⃗^(μ) = (T^T T + μ⁻¹I)⁻¹ T^T b⃗
min_η ||(b⃗ - Tη)^T(b⃗ - Tη) + μ(η^T η - c^(μ))||
χ = b⃗ - b̂⃗
```
- T: geometry/transmission matrix (n×m)
- b̂⃗: measurement vector (n)
- x⃗: emissivity values (m)
- μ > 0: regularization parameter
- I: identity matrix
- χ: iteration error
- Stronger regularization → closer to desired solution, larger error

**W7-X Approach:**
- Minimum Fisher regularization (Chapter 4)
- Currently used with bolometer diagnostic

**Radial and Poloidal Profiles [Eq. 34, 35]:**
```
ĝ_rad(r) = (1/2π)∫₀^(2π) ĝ(r,θ)dθ
ĝ_pol(θ) = (1/f_P r_a)∫₀^(f_P r_a) ĝ(r,θ)dr
```

**Example (Fig. 1.26):**
- XP20180725.44 at t = 3.0 s
- Top-left: radial profile with error bars
- Top-right: 2D distribution with Poincaré overplot
- Bottom-left: poloidal profile with error bars
- Bottom-right: individual poloidal distributions
- Error bars: mathematical penalty + resolution (cell size/2)

#### 4.3 Power Balance (Subsection, lines 781-854)

**Importance:**
- Critical for plasma characterization
- Essential for fusion reactor viability
- Understanding heating and power exhaust processes

**0-D Model Assumptions:**
- Pure plasma: n_e ≈ n_I = n, n_Z << n
- T_e = T_I = T
- Fully ionized, thermodynamic equilibrium
- Internal energy: U_j = (3/2)n_j T_j = (3/2)p_j
- Pressure: p_j = n_j T_j

**Energy Conservation [Eq. 36]:**
```
(3/2)∂p/∂t + (3/2)(∇·p)u⃗ + p∇·u⃗ + ∇·q⃗ = s
```
- s = s_H - s_rad (sources and sinks)
- s_H: input heating
- s_rad: radiation losses

**Global Energy Balance [Eq. 37]:**
```
0 = S_bal = S_H - S_rad - S_div - dW/dt
```
- S_div: convective energy loss to target
- W: plasma stored energy

**Stored Energy:**
- W_kin = (3/2)∫ Σ_j n_j T_j (dV/dr)dr (kinetic)
- W_dia: diamagnetic energy (from flux measurements)
- W_kin neglects impurities → ~25% larger than W_dia
- W_dia more accurate (dedicated diagnostic)

**Power Balance [Eq. 38]:**
```
0 = P_bal = P_ECRH - P_rad - P_div - dW/dt
```

**Error Sources:**
- P_rad: 5% (diagnostic comparison) + potential 25% (main chamber)
- P_ECRH: 10% intrinsic error
- P_div: 10% (IR thermography, THEODOR code)
- Toroidal asymmetries
- Large combined error bars

**Example 1 (Fig. 1.27 - XP20180808.4):**
- P_bal ≈ 0 within error bars
- Excess heating at start
- Radiation peak after shut-off → large negative balance
- Target heat load drops unexplained
- Large error bars throughout

**Example 2 (Fig. 1.28 - XP20180725.44):**
- Same discharge as previous local examples
- Target heat loads < 200 kW
- Delayed divertor heat response
- Rapid P_rad increase to 3.0 s
- P_rad > P_ECRH for 2 s (volumetric estimation error)
- Large P_bal deviations from zero
- Negative P_bal when dW_dia/dt also negative
- P_rad overestimates true loss

**Conclusions:**
- Model works better for steady-state conditions
- Fast transitions poorly described
- Individual assessments (local emissivity, tomography) necessary for asymmetric scenarios

## Key Equations Summary

1. **Wheatstone Bridge:** ΔU/U_ex ≈ ΔR/(2R)
2. **Bolometer Power:** P_bol = (2Rκ)/(U_ex R̂τ)(ΔU + τ dΔU/dt)
3. **Resistance:** R_M = 2(U_cal/(I(∞) - I₀) - R_L - R_C)
4. **Cooling Time:** ΔI(t) = -ΔI(0)[1 - exp(-t/τ_M)]
5. **Heat Capacity:** κ_M = ΔI⁴(0)/(4I(∞)(I(∞) - I₀))
6. **Etendue:** K̃_M = ∬(cos α cos β)/(4πd²) dA_M dA_A
7. **Final Bolometer Equation:** P_M = F_M(dΔŨ_M/dt + f_M ΔŨ_M)
8. **Global Radiation:** P_rad = (V_P,tor/V_C) Σ_M (P_M V_M/K_M)
9. **Chord Profile:** P_chord,M = P_M/(Σ_i Σ_j Σ_k T^(i,j,k)_M)
10. **Radial Profile:** ĝ_rad(r) = (1/2π)∫₀^(2π) ĝ(r,θ)dθ
11. **Power Balance:** P_bal = P_ECRH - P_rad - P_div - dW/dt

## Figures Summary
- Fig 1.1: Detector schematic (layers)
- Fig 1.2: Detector chip and bolometer head assembly
- Fig 1.3: Camera head 3D overview
- Fig 1.4: Lines of sight (HBC, VBC)
- Fig 1.5: Transmission functions (aperture/detector ratios)
- Fig 1.6: Angular relations (etendue)
- Fig 1.7: Etendue maps for detector pairs
- Fig 1.8: Wheatstone bridge measurement circuit
- Fig 1.9: Calibration circuit
- Fig 1.10: Signal example (power stage response)
- Fig 1.11: Ohmic heating stages
- Fig 1.12: (continuation)
- Fig 1.13: Calibration parameters example
- Fig 1.14: Temperature drift example
- Fig 1.15: Pt absorber efficiency
- Fig 1.16: W7-X detector absorption efficiency
- Fig 1.17: Microwave protection (coating, transmission)
- Fig 1.18: OP1.2b calibration statistics (R, κ, τ, offset)
- Fig 1.19: OP1.2b acquisition statistics (σ, drift, median, max)
- Fig 1.20: LoS volume and domain schematic
- Fig 1.21: Volumes V_M and etendues K_M per camera
- Fig 1.22: Power example (P_M and P_rad)
- Fig 1.23: Grid and geometry contribution
- Fig 1.24: Effective radius along LoS
- Fig 1.25: Chord brightness profiles
- Fig 1.26: MFR 2D example (radial, poloidal, 2D map)
- Fig 1.27: Power balance example (XP20180808.4)
- Fig 1.28: Power balance example (XP20180725.44)

## Tables Summary
- Table 1.1: Median and std dev of calibration/acquisition properties
- Table 1.2: Systematic errors for Gaussian propagation
- Table 1.3: (continuation)

## Technical Specifications

**Detector:**
- Absorber: 5 mm², 5 μm Au + 50 nm C coat
- Resistance: ~1 kΩ
- Heat capacity: ~0.8 mW/kΩ
- Cooling time: ~110 ms
- Max temperature: 250°C

**Acquisition:**
- ADC: 16-bit, ±10-80 mV range
- Resolution: 0.31-2.44 μV
- Sample rate: 625-1250 Hz
- SNR: >1000 (30 dB)
- Noise: 0.5-6 μV

**Cameras:**
- Total channels: 128 (61 functional in OP1.2b)
- HBC: 32 channels, 175 mm distance
- VBC: 48 channels (2×24), 84 mm distance
- Toroidal tilt: 68.75°

## Scientific Context
This chapter establishes the foundation for all subsequent radiation measurements and analysis in the thesis. The bolometer diagnostic is the primary tool for:
1. Global radiation power loss measurements (power balance)
2. Local emissivity distributions (transport studies)
3. Real-time feedback control (Chapter 2)
4. Sensitivity analysis (Chapter 3)
5. Tomographic reconstruction (Chapter 4)

The detailed technical description enables understanding of measurement uncertainties, systematic errors, and limitations that affect all subsequent analyses.