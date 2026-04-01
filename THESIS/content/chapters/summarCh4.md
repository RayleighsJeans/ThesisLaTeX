# Chapter 4: Two-dimensional Radiation Inversion - Summary

**File:** `THESIS/content/chapters/chapter4.tex` (1281 lines)

## Overview

Chapter 4 presents the development, benchmarking, and application of a **Minimum Fisher Regularisation (MFR)** tomographic reconstruction algorithm with **Radially Dependent Anisotropy (RDA)** for reconstructing 2D radiation profiles from line-integrated bolometer measurements at W7-X. This is the most technically complex chapter, covering mathematical framework, extensive phantom testing, geometry sensitivity analysis, and experimental data reconstruction.

---

## Structure

### 4.1 Introduction to Tomographic Inversion (lines 1-200)
- **Ill-posed inverse problem**: Reconstruct 2D emissivity g(r,θ) from line-integrated measurements b
- **Tikhonov regularization**: min[½χ² + x^T·H·x] to handle ill-conditioned matrix T
- **Laplace operator regularization**: Second-order gradient minimization for smoothness
- **Minimum Fisher Regularisation (MFR)**: Main algorithm
  - Fisher information: I_F = ∫(1/g)(∂g/∂r)² dr
  - Cramér-Rao bound for optimal estimation
  - Iterative scheme: x^(n+1) = (T^T·T + μH^(n))^(-1)·T^T·b
  - Weighting: W^(n) = 1/g^(n-1)
  - SuperLU for matrix inversion
  - Convergence: χ²_min, σ_min criteria

### 4.2 Radially Dependent Anisotropy (RDA) (lines 1-200)
- **Anisotropy factor k_ani**: Varies poloidal smoothness (core vs. edge)
- **Parameters**:
  - k_core, k_edge: Control smoothness levels
  - N_T (threshold): Radial transition location
  - N_S (width): Transition smoothness
- **Modified operator**: H_ani^(n) with k_ani(r) weighting
- **Transition function**: Uses arctan for smooth radial variation
- k > 1: Smooth, isotropic profiles
- k < 1: Localized, anisotropic features

### 4.3 Camera Geometry Sensitivity (lines 201-367)
- **Absorber/aperture segmentation methods**:
  - Rectangular subdivision
  - Delaunay triangulation
  - N subdivisions (tested N = 2, 4, 8)
- **Discrete etendue calculation**: T_M^(i,j) with geometric factors
- **LOS cone volume**: 3D sensitivity distribution
- **Comparison results**: N > 4 sufficient, N = 8 standard
- **Variance**: ~10^-11 to 10^-14 mm³ (negligible for reconstruction)

### 4.4 Line-of-Sight Geometry Perturbations (lines 206-367)
- **Centered aperture test**: HBC shifted to z=0
  - Asymmetry persists (not source of observed asymmetry)
  - Etendue variations ~10^-11 mm³
- **Virtual horizontal camera**: Fully upright, centered geometry
  - Produces perfectly symmetric forward profiles
  - Confirms geometry causes intrinsic asymmetry
- **Aperture displacement**: ±2° tilt tests
  - Measured: 0.5-1.5 mm displacement after OP1.2b
  - Significant impact on chord brightness profiles
  - Radial shifts of ±0.5 r_a in peak locations
  - χ² degradation: 0.513 and 0.394 (vs. ~1.0 ideal)

### 4.5 Additional Artificial Cameras (lines 339-367)
- **MIRh (Mirrored Horizontal)**: 15 channels, inboard side
  - Covers full poloidal cross-section
  - Tilted 68.75° toroidally
  - Improves reconstruction of complex phantoms
  - Adds N×(N_HBC + N_VBCr) new intersections

### 4.6 Phantom Radiation Profiles (lines 368-894)

#### 4.6.1 Evaluation Tools (lines 371-425)
- **Mean Square Deviation (MSD)**: m_var = √[(x-x_phan)(x-x_phan)^T]/||x_phan|| · A_p^T
- **Integrated MSD**: M_var = ||m_var||
- **Pixel area**: Heron's formula for triangulated mesh
- **2D integrated power**: P_rad,2D = x^T · A_p = 2πR_maj Σ x^(i,j) A_p^(i,j)
- **Fitness factor**: χ² = (1/N_ch)||( b_phan - b_tom)σ^(-1)||
- **Error model**: σ^(n) = 0.025·max(b)·random sample from N(0, 0.5)
- **Pearson correlation coefficient**: ρ_c for linear correlation assessment

#### 4.6.2 Symmetrical Ring in SOL (lines 427-476)
- **Phantom**: Gaussian ring at r_a, σ_r = 0.25r_a, P_max = 1 MW/m³
- **k_ani = {2, 0.5}**: Smooth core, anisotropic edge
- **Results**: 
  - Asymmetric reconstruction (lower inboard bias)
  - Radial broadening in tomogram
  - MSD: 2-2.5% along separatrix
  - Good P_rad agreement (<0.4% error)
  - χ² close to unity

#### 4.6.3 Anisotropic Ring Combinations (lines 477-597)
- **SOL ring + 180° core anisotropy**:
  - Ring at r_a + core spot at 0.7r_a (150% intensity)
  - k_ani = {0.3, 0.3}: Balanced anisotropy, better core localization
  - k_ani = {1.5, 0.25}: Hyper-localized spots, worse overall
  - Conclusion: Geometry-dependent, LOS coverage critical

- **SOL ring + 270° core anisotropy**:
  - Rotated 90° clockwise
  - Similar challenges, improved fitness for some k_ani
  - χ² and MSD not always aligned with subjective quality

- **Key findings**:
  - Opposite-to-aperture features harder to reconstruct
  - k_core > 1 > k_edge: Anisotropies lost, translated to SOL
  - 1 > k_core = k_edge: Enables core localization, loses smoothness
  - Need tailored k_ani for each distribution type

#### 4.6.4 Experimentally Motivated Phantoms (lines 599-644)
- **6 island-like spots + core ring**:
  - Up-down symmetric, 1.1r_a, σ_θ = π/12
  - k_ani = {2, 0.1}: Best results, distinct SOL spots
  - Asymmetry in reconstruction (geometry bias)
  - P_rad agreement excellent (<0.5%)

- **k_ani parameter variation** (lines 645-678):
  - Tested: {2, 0.3}, {20, 0.3}, {2, 0.6}
  - Optimal ratio: 10:1 to 50:1 (k_core:k_edge)
  - Recommended: k_core = 2-10, k_edge = 0.01-0.5

- **Artificial camera support** (lines 679-703):
  - MIRh addition improves SOL localization
  - Adds robustness to T matrix (lower condition number)
  - Qualitative improvement, quantitative metrics similar

#### 4.6.5 Geometry Error Propagation (lines 704-751)
- **±1° tilt tests** with ring at 1.1r_a:
  - +1° tilt: χ² = 0.513, asymmetric profiles
  - -1° tilt: χ² = 0.394, radial shift 0.06r_a
  - P_rad deviations ≥10% in worst case
  - Difficult to detect from tomogram alone
  - Cumulative errors non-negligible

#### 4.6.6 Reconstructive Limits (lines 752-894)
- **Isotropic ring scans**:
  - k_core scan [0.65-1.0]: Optimal ~0.9-0.95
  - k_edge scan [1.25-1.8]: Optimal ~1.45
  - χ², ρ_c, MSD largely in agreement
  - Computational cost: N×N-2N reconstructions for full scan

- **Radial position scans**:
  - Single ring: Best at 0.9-1.1r_a (near LCFS)
  - Double rings: Uniform quality except threshold at 0.8r_a
  - SOL deviation peaks at small ring separations

- **Anisotropic island chain scan**:
  - 5 islands at 1.1r_a, k_edge varied [0.1-6]
  - Contradictory: Larger k_edge yields better χ², ρ_c
  - Core variance dominates total error (dark center effect)
  - k_edge = 0.25: Local optimum
  - Delicate tuning required for anisotropic distributions

- **Composite phantoms** (bright spots):
  - Inboard (R=4.75m): Optimal k_core ~0.95
  - Outboard (R=5.75m): Optimal k_core ~0.87
  - Multiple erroneous peaks for k_core < 0.75
  - Asymmetric optimization around optimum
  - Geometry-dependent (inboard vs. outboard)

- **Recommended settings**: k_ani = {2.0, 0.3}, N_T = 15, N_S = 2

### 4.7 Phantom Statistics (lines 895-913)
- **Dataset**: All phantom reconstructions with MSD < ∫g
- **FWHM location**: Good agreement, grouped near 1:1 line
- **FWHM width**: Phantom consistently larger (tomogram sharper)
- **P_rad comparison**: Excellent congruence (σ = 0.2 MW)
- **P_2D comparison**: Good agreement (σ = 0.7 MW), more outliers
- **MSD vs. χ²**: Distinct line at χ² = 1, spread at MSD < 0.5%
- **MSD vs. ρ_c**: Linear decrease, vanishes at ρ_c = 1
- **χ² vs. ρ_c**: Separated by 1:1 line, tight groupings
- **P_rad vs. P_2D,core**: Linear fits, HBC and VBC similar slopes
  - P_rad slightly overestimates core (at high power)
- **P_rad vs. P_2D,tot**: Worse correlation, P_rad underestimates total
  - Gap suggests profile-specific models needed

### 4.8 Experimental Data Tomography (lines 914-1207)

#### 4.8.1 XP20180725.44 (lines 918-1008)
- **Configuration**: KJM (high mirror), k_ani = {2, 0.25}, N_T = 15, N_S = 2
- **Grid**: 1.25r_a domain, 20×150 pixels
- **Time series** (3.05-3.65s):
  - Smooth ring along LCFS, shifts radially inward
  - Peak at 3.4s: Smallest profile (0.2r_a), highest intensity
  - Hollow core structure throughout
  - Correlates with n_e increase, T_e centralization
  - No SOL radiation at peak
- **Conclusions**: Plausible, qualitative agreement with plasma parameters

#### 4.8.2 XP20180809.13 (lines 1009-1074)
- **Configuration**: Standard, k_ani = {2, 0.5}, N_T = 14, N_S = 2
- **Grid**: 1.35r_a domain, 30×150 pixels
- **Scenario**: Laser Blow-Off (LBO) impurity injection events
- **Time series** (1.8-2.8s):
  - Before LBO: Smooth ring, lower inboard maximum
  - During LBO (2.15-2.2s): Contraction, centralization
  - After LBO: Equilibration, similar to initial
  - Constant profile inside LCFS during peak
- **Physics**: 
  - Impurity ionization → core transport
  - Reversible process
  - Low f_rad (<0.25) except during events
- **Conclusions**: Demonstrates impurity transport dynamics

#### 4.8.3 XP20181010.32 (lines 1075-1138)
- **Configuration**: Standard, k_ani = {2, 0.35}, N_T = 13, N_S = 2
- **Grid**: 1.35r_a domain, 30×150 pixels
- **Scenario**: Real-time radiation feedback (prime example)
- **Time series** (0.65-3.05s):
  - 0.65s (f_rad=0.33): Concentrated lower inboard spot
  - 1.7s (f_rad=0.40): Maximum shifts to lower outboard island
  - 1.8s (f_rad=0.45): Global max at upper central X-point
  - 2.2s (f_rad=0.66): Singular confined spot (upper islands)
  - 2.95s (f_rad=0.95): Multiple features, lower outboard max
  - 3.05s (f_rad=0.90): Similar to 2.95s, less condensed
- **Key observations**:
  - Radiation condenses at magnetic island intersections
  - Up to 80% f_rad: Counter-clockwise shift (lower → upper)
  - Above 80% f_rad: Reverses (upper → lower outboard)
  - Oscillates with feedback valve opening/closing
  - Emission "pushed out" to LCFS/SOL at high f_rad
- **Implications**: 
  - Difficult to select optimal LOS for P_pred
  - Location-dependent over/underestimation
  - Need balanced set covering all features

#### 4.8.4 XP20181011.12 (lines 1139-1207)
- **Configuration**: KJM, k_ani = {2, 0.35}, N_T = 14, N_S = 2
- **Grid**: 1.35r_a domain, 20×150 pixels
- **Scenario**: ECRH step-downs + LBO injections
- **Time series** (1.4-5.7s):
  - 1.4s: Even distribution, lower inboard X-point maximum
  - 2.7s: Inboard max increases, shifts toward X-point
  - 5.65s: Maximum expands to separatrix
  - 5.7s: Pushed outward to island edge
- **Physics**:
  - Post-boronization (improved performance)
  - Condensation at lower inboard X-point
  - Contraction with power reduction + LBO
  - Inward shift at high f_rad, outward beyond threshold
- **Conclusions**: 
  - Resolves single-cell variations
  - Consistent with previous experiments
  - k_ani = {2, 0.35} generalizes well

### 4.9 Experimental Statistics (lines 1209-1231)
- **Selection**: χ² < 1000 (sensible reconstructions)
- **P_rad comparison**: On par with phantom results
  - Strong agreement between forward/backward
  - Testament to MFR optimization
- **P_rad vs. P_2D,core**: 
  - Improved linear fits vs. phantoms
  - Both cameras: Same prediction function
  - P_rad underestimates by ~P_SOL amount
- **P_rad vs. P_2D,tot**:
  - P_tot consistently larger
  - Slight camera differences in fit
- **Conclusions**: 
  - Qualitatively and quantitatively promising
  - Limited by reduced assessable parameters
  - Core integral better represents confined radiation

### 4.10 Power Balance Applications (lines 1232-1275)

#### 4.10.1 XP20181010.32 Power Balance
- **Standard P_bal**: Fails to equalize, large oscillations
- **P_bal,core^tom**: Much improved match, P_bal → 0
  - Reduced oscillations from feedback
  - Better agreement with premise
- **P_bal,tot^tom**: Similar to P_rad, greater deviation
- **At high f_rad**: P_bal,tot increases, P_bal,core remains near zero
- **Conclusion**: Core integral better for power balance

#### 4.10.2 XP20180725.44 Power Balance
- **P_bal,core^tom**: Close to or below P_rad balance
  - Trend: 0 to -1.5 MW → -0.5 to -1.8 MW
  - Variation ~2× standard P_bal reduction
- **P_bal,tot^tom**: Significant separation from core
- **k_ani variations**: Produce quantitative differences
- **After collapse**: No SOL emission (r > r_a)
- **Conclusion**: 
  - Core integral valid estimator
  - Less impacted by fast transitions
  - Worse match than XP20181010.32 (due to profile shape)

### 4.11 Conclusions (lines 1276-1281)
- **Geometry robustness**: Significant against perturbations
  - N = 8 triangulation adequate
  - Unknown in-situ errors non-negligible but indistinguishable
- **Artificial cameras**: MIRh improves complex phantom reconstruction
- **STRAHL asymmetry**: Intrinsic in symmetric HBC design
- **Benchmark results**:
  - Ideal k_ani exists for each distribution
  - k < 1: Localized; k > 1: Smooth (as designed)
  - χ² = 1 not always optimal (quality measures diverge)
  - Experimentally motivated phantoms most challenging
- **Statistical findings**:
  - Core P_2D slightly overrepresented by P_rad
  - Total P_2D significantly overestimated
  - Recommended: k_ani = {2, 0.3}, N_T = 15, grid 30×150, 1.3²V_P
- **Experimental application**:
  - Adequate, robust results
  - Nearly identical statistics to phantoms
  - Core integral more stable for power balance
  - Alternative for small interval inspections
- **Overall**: Formally benchmarked, reliable results, multidimensional optimization challenging

---

## Key Equations

### Tikhonov Regularization
```
min[½χ² + x^T·H·x]
χ² = ||Tx - b||²
```

### MFR Iteration
```
x^(n+1) = (T^T·T + μH^(n))^(-1)·T^T·b
W^(n) = 1/g^(n-1)
H^(n) = D^T·W^(n)·D
```

### Fisher Information
```
I_F = ∫(1/g)(∂g/∂r)² dr
```

### RDA Anisotropy Factor
```
k_ani^(i) = k_edge + (k_core - k_edge)·½[1 + arctan((N_T - i)/N_S)]
```

### Discrete Etendue
```
T_M^(i,j) = Σ_k Σ_{p,q} L^(i,j,k)_{p,q} · (cosα·cosβ)/(2πd²) · dA_M · dA_A
```

### Mean Square Deviation
```
m_var = √[(x-x_phan)(x-x_phan)^T]/||x_phan|| · A_p^T
M_var = ||m_var||
```

### 2D Integrated Power
```
P_rad,2D = x^T · A_p = 2πR_maj Σ_{i,j} x^(i,j) A_p^(i,j)
```

### Fitness Factor
```
χ² = (1/N_ch)||(b_phan - b_tom)σ^(-1)||
```

### Pearson Correlation
```
ρ_c = E[(x - E(x))(y - E(y))] / (σ_x σ_y)
```

### Heron's Formula (Pixel Area)
```
A(△XYZ) = √[p(p-a)(p-b)(p-c)]
p = ½(a + b + c)
```

---

## Figures (59 total)

### Geometry and Sensitivity
1. **fig:2Detendues_comparison_splitting**: Etendue variations for N=2,4,8 and triangulation vs. rectangular
2. **fig:geometry_change_centered**: Centered HBC geometry comparison
3. **fig:forward_intSTRAHL_centered**: Forward profiles with centered geometry
4. **fig:geometry_change_artificial**: Virtual upright HBC geometry
5. **fig:geometry_forward_symmetric**: Symmetric forward profiles
6. **fig:geometry_change_tilted**: ±2° tilted geometries
7. **fig:emiss_change_tilted**: Etendue changes for tilted geometries
8. **fig:chord_change_tilted**: Forward profiles with tilted geometries
9. **fig:geometry_newcam_mirh**: MIRh artificial camera geometry

### Phantom Reconstructions - Simple
10. **fig:phantom_fsring_example**: Symmetrical ring at r_a (phantom, tomogram, MSD)
11. **fig:phantom_fsring_example_profiles**: Radial and chordal profiles for ring
12. **fig:phantom_fsring_asym_180deg_2D**: SOL ring + 180° core anisotropy (2 k_ani sets)
13. **fig:phantom_fsring_asym_180deg_profiles**: Profiles for 180° anisotropy
14. **fig:phantom_fsring_asym_270deg_2D**: SOL ring + 270° core anisotropy (2 k_ani sets)
15. **fig:phantom_fsring_asym_270deg_profiles**: Profiles for 270° anisotropy

### Phantom Reconstructions - Complex
16. **fig:phantom_islands_6_fsring_ani3**: 6 island spots + core ring
17. **fig:phantom_islands_6_fsring_ani3_profiles**: Profiles for island phantom
18. **fig:phantom_islands_6_fsring_kanivar**: k_ani variations (3 sets)
19. **fig:phantom_islands_6_fsring_ARTm**: With MIRh artificial camera
20. **fig:phantom_islands_6_fsring_ARTm_profiles**: Profiles with MIRh

### Geometry Error Propagation
21. **fig:phantom_fsring_tilt_1deg**: +1° tilt reconstruction
22. **fig:phantom_fsring_tilt_-1deg**: -1° tilt reconstruction

### Reconstructive Limits - Scans
23. **fig:phantom_scans_fsring_kani_coreEdge**: k_core and k_edge scans (isotropic ring)
24. **fig:phantom_scans_fsring_doubleRings**: Single and double ring radius scans
25. **fig:phantom_scans_sym5_kani_edge**: Island chain k_edge scan
26. **fig:phantom_bright_spots_ani**: Bright spot phantoms (inboard/outboard)
27. **fig:phantom_scans_xx75_kani_core**: Bright spot k_core scans

### Phantom Statistics
28. **fig:tomo_phantom_statistics**: Collected phantom reconstruction statistics (9 subplots)

### Experimental Data - XP20180725.44
29. **fig:20180725.44_PDF**: Central plasma parameters
30. **fig:tomo_20180725.44_times**: Tomograms at 6 time points (3.05-3.65s)

### Experimental Data - XP20180809.13
31. **fig:20180809.13_PDF**: Central plasma parameters
32. **fig:tomo_20180809.13_times**: Tomograms at 4 time points (1.8-2.8s)

### Experimental Data - XP20181010.32
33. **fig:tomo_20181010.32_times**: Tomograms at 6 time points (0.65-3.05s)

### Experimental Data - XP20181011.12
34. **fig:20181011.12_PDF**: Central plasma parameters
35. **fig:tomo_20181011.12_times**: Tomograms at 4 time points (1.4-5.7s)

### Experimental Statistics
36. **fig:tomo_experiment_statistics**: Collected experimental reconstruction statistics (3 subplots)
37. **fig:tomo_experiment_20181010032_balance**: Power balance for XP20181010.32
38. **fig:tomo_experiment_201810725044_balance**: Power balance for XP20180725.44

---

## Tables

None explicitly numbered, but extensive parameter sets documented throughout.

---

## Technical Specifications

### Grid Configurations
- **Standard**: 30×20×150 (φ×θ×r), 1.3²V_P domain
- **High resolution**: 30×20×150, 1.35r_a domain
- **KJM configuration**: 20×150 (2D), 1.25r_a domain

### Recommended MFR Parameters
- **k_core**: 2.0 a.u.
- **k_edge**: 0.3 a.u.
- **N_T**: 15 (transition threshold)
- **N_S**: 2 (transition width)
- **Segmentation**: N = 8 (Delaunay triangulation)

### Computational Settings
- **Matrix solver**: SuperLU
- **Convergence**: χ²_min, σ_min criteria
- **Error model**: 1-2.5% of max(b), Gaussian distributed

### Quality Metrics
- **Fitness**: χ² ≈ 1 (target)
- **Correlation**: ρ_c → 1 (target)
- **MSD**: <0.5% (good), <2.5% (acceptable)
- **Power agreement**: P_rad vs. P_2D within 0.2-0.7 MW

---

## Scientific Context

### Tomographic Reconstruction Challenges
1. **Ill-posed problem**: More unknowns than measurements
2. **Regularization necessity**: Smooth vs. localized trade-off
3. **Geometry sensitivity**: LOS coverage determines quality
4. **Parameter optimization**: Multidimensional, distribution-dependent
5. **Quality assessment**: Multiple metrics, not always aligned

### Physics Insights from Tomography
1. **Radiation localization**: Condenses at magnetic island intersections
2. **Feedback dynamics**: Reversible shifts with f_rad oscillations
3. **Impurity transport**: LBO events show core penetration and ejection
4. **Power balance**: Core integral more stable than total
5. **Geometry bias**: Intrinsic asymmetry from camera orientation

### W7-X Specific Findings
1. **Optimal f_rad range**: 80-95% for detachment
2. **Critical locations**: X-points, magnetic islands, LCFS
3. **Feedback challenges**: LOS selection for P_pred difficult
4. **Boronization impact**: Improved performance, different profiles
5. **Configuration dependence**: Standard vs. KJM differences

---

## LaTeX Patterns and Custom Commands

### Subscript/Superscript Notation
- `\ix{text}`: Text subscripts (e.g., `P\ix{rad}` → P_rad)
- `\head{text}`: Text superscripts
- `n\ix{e}`, `T\ix{e}`: Electron density, temperature
- `r\ix{a}`, `r\ix{0}`: Minor radius, reference radius
- `k\ix{core}`, `k\ix{edge}`: Anisotropy coefficients
- `N\ix{T}`, `N\ix{S}`: Transition parameters
- `P\ix{rad}`, `P\ix{2D}`: Radiation powers
- `f\ix{rad}`: Radiation fraction
- `\chi\ix{2}`: Chi-squared
- `\rho\ix{c}`: Pearson coefficient

### Mathematical Operators
- `\diff`: Upright differential d
- `\coloneqq`: Definition symbol
- `\mathrel{\hat{=}}`: Correspondence symbol
- `\pmb{}`: Bold math symbols
- `\oint\ix{FS}`: Flux surface integral
- `\Theta\ix{N}`: Heaviside step function

### Special Notation
- `\tenpo{n}`: Powers of 10 (10^n)
- `\SIrange{min}{max}{unit}`: Range with units
- `\SI{value}{unit}`: Single value with unit
- `\arbitraryunit`: Arbitrary units (a.u.)

### Figure References
- `\cref{label}`: Contextual reference (Figure, Equation, etc.)
- `\autoref{label}`: Automatic reference type

### Emphasis
- `\textit{text}`: Italics for terms
- `\textbf{text}`: Bold for emphasis
- `\textcolor{color}{text}`: Colored text (red for modified geometry)

---

## Connections to Other Chapters

### From Chapter 1 (Bolometry)
- Uses HBC, VBCl, VBCr camera specifications
- Applies etendue calculations from Chapter 1
- Builds on LOS geometry definitions
- Extends single-channel analysis to 2D reconstruction

### From Chapter 2 (Feedback Control)
- Analyzes XP20181010.32 (prime feedback example)
- Explains P_pred LOS selection challenges
- Shows radiation distribution during feedback
- Validates feedback impact on emissivity profiles

### From Chapter 3 (LOS Sensitivity)
- Uses STRAHL radiation profiles for forward modeling
- Applies sensitivity analysis to tomography
- Confirms carbon dominance in reconstructions
- Extends 1D analysis to 2D distributions

### To Chapter 5 (Conclusions)
- Provides validated tomography tool for future work
- Establishes MFR as reliable diagnostic method
- Identifies areas for improvement (artificial cameras)
- Demonstrates power balance applications

---

## Key Takeaways

1. **MFR with RDA successfully reconstructs 2D radiation profiles** from W7-X bolometer data
2. **Optimal parameters exist but are distribution-dependent**: k_ani = {2, 0.3} is good starting point
3. **Geometry matters critically**: Unknown errors non-negligible, artificial cameras help
4. **Quality metrics diverge**: χ² = 1 not always optimal, need multiple assessments
5. **Experimental validation successful**: Statistics match phantom benchmarks
6. **Physics insights gained**: Radiation localization, feedback dynamics, impurity transport
7. **Power balance improved**: Core integral more stable than P_rad alone
8. **Challenges remain**: Multidimensional optimization, LOS selection for feedback
9. **Future work identified**: Continuous tomography, optimized sampling, camera extensions
10. **Method is production-ready**: Formally benchmarked, reliable, applicable to W7-X operations

---

**Total lines analyzed**: 1281 (complete chapter)
**Complexity**: Highest in thesis (mathematical framework + extensive testing + experimental application)
**Status**: Complete, comprehensive tomographic reconstruction methodology established