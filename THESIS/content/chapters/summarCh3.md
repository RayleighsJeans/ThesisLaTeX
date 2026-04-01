# Chapter 3: Feedback Impact and Line of Sight Sensitivity Analysis - Summary

## Overview
Chapter 3 (833 lines) addresses two fundamental questions about the real-time bolometer feedback system: (1) Does an optimal set of lines of sight exist? (2) What dominates LOS selection sensitivity? The chapter employs three approaches: impurity seeding models (two-chamber and three-chamber), extensive LOS sensitivity evaluation using multiple metrics, and STRAHL impurity transport simulations to understand radiation distribution changes during feedback experiments.

## Structure

### 3.1 Introduction (lines 1-15)
- **Two Key Questions**:
  1. Does an optimal LOS set S exist for real-time feedback?
  2. What dominates LOS selection sensitivity?
- **Approach**: Combination of physical models, experimental data analysis, and STRAHL simulations

### 3.2 Impurity Seeding Modelling (lines 16-236)

#### 3.2.1 Two Chamber Model (lines 31-118)
- **Concept**: Gas split into plasma chamber (N_p) and wall chamber (N_w) populations
- **Equations**: First-order differential equations with exchange rates τ
- **Parameter f**: Satisfies equilibrium requirement at threshold population
- **Benchmark**: Parameter variations (Γ_s, N_w,lim, τ_w,p, N_w,0)
- **Application**: Successfully reproduces XP20180920.49 saturation behavior
- **Key Finding**: P_rad ∝ N_p assumption works well

#### 3.2.2 Three Chamber Model (lines 120-236)
- **Extension**: Adds scrape-off layer chamber (N_s) between plasma and wall
- **Source/Sink**: Located in SOL chamber (more realistic)
- **Finite Capacity**: Applied to plasma and wall chambers
- **Benchmark**: Six parameters varied (N_w,lim, N_p,lim, τ_s,p, Γ_s, τ_w,s, τ_s)
- **Application**: Fit to XP20180920.49 with weighting factor f ≈ 11
- **Key Finding**: SOL population dominates (N_s >> N_p, N_w by factor 10)
- **Result**: P_rad ∝ N_p + fN_s with strong SOL contribution

### 3.3 Line of Sight Sensitivity Evaluation (lines 237-443)

#### 3.3.1 Evaluation Framework (lines 241-273)
- **Metric φ**: Quality function in time domain f(t, S, P_rad)
- **Map θ**: Transforms metric to single quality value h(S, P_rad, φ)
- **LOS Collections**: 900 combinations each for m = 3, 5, 7 channels
- **Experiments**: All feedback-controlled discharges from campaign
- **Sensitivity**: Average quality θ̄_n^(m) for channel n in size m combinations

#### 3.3.2 Weighted Deviation Metric (lines 275-332)
- **Definition**: φ(t) = 1 - |P_pred - P_rad|/P_rad (when P_pred < P_rad)
- **Quality**: θ = integral of φ over experiment time
- **HBC Results**:
  - m=3: θ ≈ 0.8, local max at ±0.5r_a
  - m=5: θ ≈ 0.84-0.9, reduced variation
  - m=7: θ ≈ 0.91-0.92, minimal variation
  - Channel 20 (X-point): lowest sensitivity (0.58)
- **VBC Results**:
  - Generally θ > 0.75 for all m
  - No scaling with selection size m
  - Higher uncertainties (up to 20% for some channels)
  - Local max at -0.5r_a and -0.1r_a

#### 3.3.3 Correlation Metric (lines 333-386)
- **Definition**: Cross-correlation integral between P_pred and P_rad
- **Quality**: θ = integral of |φ* - φ| (deviation from self-correlation)
- **Results**:
  - Large error bars (up to 40%)
  - Congruent profiles for different m
  - Local maxima (low sensitivity) at ±0.9r_a (X-points)
  - Opposite conclusions from weighted deviation
  - Emphasizes temporal correlation issues

#### 3.3.4 Mean Deviation Metric (lines 387-442)
- **Definition**: Modified variance φ(t) = (P_rad - P_pred)²/(T_stop - T_start)
- **Quality**: θ = sqrt((T_stop - T_start)/integral of φ)
- **Results**:
  - HBC: θ ≈ 1.2×10⁻⁴ for m=7 (highest quality)
  - VBC: Similar behavior, θ = 1-1.7×10⁻⁴
  - Large error bars (20-40%)
  - Less pronounced extrema than weighted deviation
  - Scales with selection size m

#### 3.3.5 Summary of Sensitivity Analysis
- **Optimal Channels**: At or close to separatrix, viewing magnetic islands/X-points
- **Unfavorable**: Core-only or outermost edge channels (for small m)
- **Selection Size**: m=7 achieves >85% accuracy regardless of specific channels
- **Camera Comparison**: HBC and VBC generally agree on sensitivity patterns

### 3.4 STRAHL Modelling (lines 445-818)

#### 3.4.1 Introduction to STRAHL (lines 450-517)
- **Purpose**: 1D impurity transport and radiation simulation
- **Solves**: Radial continuity equation for each ionization stage
- **Transport**: Anomalous diffusion D* and drift velocity v*
- **Limitations**: Invalid outside LCFS (SOL results unreliable)
- **Input Data**: XP20181010.32 at various f_rad levels
- **Configuration**:
  - Neutral injection: 9×10²⁰ s⁻¹ at r_LCFS + 7.5 cm
  - Decay length: 5 cm outside separatrix
  - Divertor at r_LCFS + 6.5 cm
  - Cubic spline interpolation for stability

#### 3.4.2 Base Model Results (lines 517-558)
- **Impurities**: Carbon and oxygen considered
- **Key Finding**: Oxygen radiation 10¹-10² times smaller than carbon
- **Focus**: Carbon impurities only for further analysis
- **Carbon Emissivity**:
  - f_rad = 33%: P_tot,C ≈ 0.65 kW/m³ in core, 45 kW/m³ in SOL
  - f_rad = 66%: Linear scaling (factor 2 increase)
  - Maximum outside LCFS for both levels
- **Ionization Stages**:
  - C⁶⁺ dominant up to 0.6r_a
  - C⁵⁺, C⁴⁺ increase toward separatrix
  - Lower stages (C³⁺, C²⁺, C⁺, C⁰) in SOL

#### 3.4.3 Parameter Variations (lines 560-718)

**Diffusion Coefficient Variations (lines 586-663)**
- **Radial Shift**: D₁ (outward 0.15 m), D₂ (inward 0.05 m)
  - D₁: Higher C⁴⁺ emissivity, shifted outward to 0.9r_a
  - D₂: Similar to base, slightly reduced
  - C³⁺: Significant SOL emissivity for D₁
  
- **Absolute Value**: D₃ (base), D₁ (much lower)
  - Lower D increases C⁵⁺, C⁴⁺ in core
  - C³⁺, C²⁺ shift toward LCFS
  - Up to 120% increase in maximum P_tot near separatrix
  - **Key Result**: Reduced transport at low T_e increases emissions

**Separatrix Electron Profile Variation (lines 664-718)**
- **Approach**: Reduce T_e,a and n_e,a to 10% of original
- **Results**:
  - Inward shift of all emission profiles (2-5 cm)
  - Significant reduction in P_tot inside and outside LCFS
  - C⁶⁺ abundance increases (lower recombination rate)
  - C³⁺, C⁴⁺ experience largest changes
  - Core emissions negligibly affected
- **Interpretation**: Mimics transition from f_rad = 90% to 100%

#### 3.4.4 Impact on Chord Brightness (lines 719-818)

**Forward Modeling (lines 720-753)**
- **Method**: Extend 1D STRAHL profile poloidally (2π symmetry)
- **Equation**: T·x_sim = b_sim (geometry matrix × emissivity = chord brightness)
- **Experimental vs. STRAHL**:
  - Similar order of magnitude
  - STRAHL shows better separation between f_rad levels
  - STRAHL more symmetric (poloidal invariance assumption)
  - Experimental data shows strong asymmetry
  - f_rad = 100%: Both show inward shift of maxima

**Parameter Variation Impact (lines 755-791)**
- **Separatrix T_e, n_e Reduction**:
  - Halved peak intensity
  - Maxima shift inward to 0.8r_a
  - Supports detachment hypothesis
  
- **Diffusion Variations**:
  - D₂: 50-130% reduction in emissivity
  - D₃: Peaked core profile, no localized features
  - D₁: Similar to base case
  
- **Core vs. SOL Radiation**:
  - f_rad = 33-66%: P_core ≈ P_SOL (50/50 split)
  - f_rad = 90%: P_core increases
  - f_rad = 100%: P_core = 70%, P_SOL = 30% (turnover)
  - Transport variations: Linear decline in P_core for D₃ → D₁

**Key Findings (lines 814-818)**
- Acceptable agreement in absolute intensity
- Strong asymmetry in experimental data not reproduced
- Indicates poloidal asymmetry in actual plasma
- Inward shift at high f_rad confirmed
- Core/SOL turnover supports detachment hypothesis

### 3.5 Conclusions (lines 819-833)
- **Question 1 Answer**: No single optimal LOS set exists, but robust selections of 3-7 channels can achieve ≥85% accuracy. Best channels view separatrix, magnetic islands, X-points. Avoid core-only or outermost edge channels.
- **Question 2 Answer**: Carbon impurities are dominant contributor. Reduction of T_e,a, n_e,a and diffusion at separatrix equally important.
- **Validation**: STRAHL supports experimental detachment observations at high f_rad
- **Limitations**: Forward modeling shows inadequacy in reproducing poloidal asymmetry

## Key Equations

### Two Chamber Model
```
dN_w/dt = (N_w,lim - N_w)τ_w,p
dN_p/dt = Γ_s + N_w·τ_w,p - N_w,lim·τ_w,p·N_p - N_p·τ_p
```

### Three Chamber Model
```
dN_w/dt = (N_w,lim - N_w)τ_w,s
dN_s/dt = Γ_s + (N_p·N_s·τ_s,p)/N_p,lim - N_w,lim·τ_w,s - N_s(τ_s,p + τ_s)
dN_p/dt = N_s·τ_s,p - (N_p·N_s·τ_s,p)/N_p,lim
```

### Evaluation Metrics
```
φ := f(t, S, P_rad): ℕᵐ × ℝ → ℝ     (metric)
θ := h(S, P_rad, φ): ℕᵐ × ℝ → ℝ     (quality map)
```

**Weighted Deviation:**
```
φ(t) = 1 - |P_pred - P_rad|/P_rad   (if P_pred < P_rad)
θ = (1/(T_stop - T_start)) ∫ φ(t) dt
```

**Correlation:**
```
φ(t) = ∫ P_pred(τ)·P_rad(t+τ) dτ
θ = (1/(T_stop - T_start)) ∫ |φ*(t) - φ(t)| dt
```

**Mean Deviation:**
```
φ(t) = (P_rad(t) - P_pred(t))²/(T_stop - T_start)
θ = sqrt((T_stop - T_start)/(∫ φ(t) dt))
```

### LOS Sensitivity
```
θ̄_n^(m) = (1/N^(n,m)) Σ_S θ(S^(m))
N^(n,m) = Σ_S δ_n(S^(m))
δ_n(S) = {1 if n∈S, 0 else}
```

### STRAHL Radial Transport
```
∂n_i,Z/∂t = (1/r)(∂/∂r)[r(D*·∂n_i,Z/∂r - v*·n_i,Z)] + S_i,Z

D* = ⟨D(θ)|∇r|²⟩_FS
v* = ⟨v(θ)|∇r|⟩_FS
```

### Core vs. SOL Radiation
```
P_core = (V_P,tor / Σ_j V_j^core) P_rad,C
P_SOL = (V_P,tor / Σ_j V_j^SOL) P_rad,C
```

### Forward Chord Brightness
```
ĝ_sim(r,θ) ≡ ĝ_sim(r) ⇒ x_sim
T·x_sim = b_sim
```

## Figures Referenced

### Impurity Seeding Models
1. **fig:chamber_expdata**: XP20180920.49 P_rad and PID components (excerpt)
2. **fig:twochamber_schematic**: Two chamber model schematic
3. **fig:twochamber_scan**: Parameter variations (Γ_s, N_w,lim, τ_w,p, N_w,0)
4. **fig:twochamber_twostage**: Two-stage fit to experimental data
5. **fig:threechamber_schematic**: Three chamber model schematic
6. **fig:threechamber_scan**: Parameter variations (6 parameters)
7. **fig:threechamber_twostage**: Three-stage fit to experimental data

### LOS Sensitivity Evaluation
8. **fig:weighted_deviation**: Example metric calculation (XP20181010.32)
9. **fig:results_weighted_deviation**: Average sensitivity for HBC and VBC
10. **fig:correlation**: Example correlation metric
11. **fig:results_correlation**: Average correlation sensitivity
12. **fig:mean_deviation**: Example mean deviation metric
13. **fig:results_mean_deviation**: Average mean deviation sensitivity

### STRAHL Simulations
14. **fig:nete_total_rad_91_92**: Thomson data and total C/O radiation (f_rad = 33%, 66%)
15. **fig:fluid_coeffs**: Standard drift and diffusion profiles
16. **fig:nete_abund_lines_91_92**: Carbon fractional abundances and emissivities
17. **fig:transp_abund_62_66**: Diffusion variations (D₁, D₂) and abundances
18. **fig:rad_ratios_total_62_66**: Relative and absolute radiation (D₁, D₂)
19. **fig:transp_abund_103_104**: Diffusion variations (D₁, D₃) and abundances
20. **fig:rad_ratios_total_103_104**: Relative and absolute radiation (D₁, D₃)
21. **fig:nete_abund_82_90**: Separatrix T_e, n_e variations and abundances
22. **fig:rad_ratios_total_82_90**: Radiation for T_e, n_e variations
23. **fig:chord_forward_exp_vs_STRAHL**: Experimental vs. STRAHL chord brightness
24. **fig:forward_neTe_vs_transport**: Parameter variation chord brightness
25. **fig:core_v_sol_comparisons**: Core vs. SOL radiation distribution

## Technical Specifications

### Two Chamber Model Parameters (XP20180920.49 Fit)
- Γ_s = 0.648 a.u./s (injection rate)
- τ_w,p = 0.1 a.u./s (wall-to-plasma rate)
- N_w,lim = 1.388 a.u. (wall capacity)
- τ_p = 0.436 a.u./s (plasma loss rate)
- N_p,0 = 0.011 a.u. (initial plasma population)
- N_w,0 = 0.075 a.u. (initial wall population)

### Three Chamber Model Parameters (XP20180920.49 Fit)
- τ_s,p = 0.1 a.u./s (SOL-to-plasma rate)
- N_p,lim = 17.9 a.u. (plasma capacity)
- τ_p,s = 14.931 a.u./s (plasma-to-SOL rate)
- Γ_s = 18.08 a.u./s (injection rate)
- N_w,lim = 2.579 a.u. (wall capacity)
- τ_w,s = 2.561 a.u./s (wall-to-SOL rate)
- τ_s = 2.772 a.u./s (SOL loss rate)
- Weighting factor f = 10.957

### LOS Selection Statistics
- **Combinations per size**: ~900 for m = 3, 5, 7
- **HBC Channels**: 30 total (3 subsets of 10)
- **VBC Channels**: Similar structure
- **Experiments**: All feedback-controlled discharges from campaign

### STRAHL Configuration
- **Impurities**: Carbon (primary), Oxygen (negligible)
- **Neutral Injection**: 9×10²⁰ s⁻¹ at r_LCFS + 7.5 cm
- **Injection Energy**: 1 eV
- **Decay Length**: 5 cm outside separatrix
- **Divertor Location**: r_LCFS + 6.5 cm
- **Calculation Boundary**: r_LCFS + 8 cm
- **Interpolation**: Cubic spline for stability
- **Magnetic Configuration**: Standard W7-X
- **Assumptions**: n_e = n_i, T_e = T_i (quasi-neutrality, equilibrium)

## Scientific Context

### Impurity Seeding Physics
- **Saturation Behavior**: Observed in continuous fueling experiments
- **Time Constants**: Multiple plateaus in P_rad evolution
- **Gas Buffering**: Pumping timescale >> transport timescale
- **Wall Retention**: Chemical/kinetic deposition of impurities
- **Critical Concentration**: Maximum sustainable c_imp before collapse

### LOS Sensitivity Patterns
- **Separatrix Channels**: Highest sensitivity for feedback
- **X-Point Channels**: Measure radiation condensation
- **Island Channels**: Capture field-line-connected emissions
- **Core Channels**: Less sensitive for feedback (small m)
- **Edge Channels**: Unfavorable for small selections

### Carbon Impurity Behavior
- **Ionization Stages**: C⁰ through C⁶⁺
- **Dominant Stage**: C⁶⁺ in core (up to 0.6r_a)
- **Transition Region**: C⁵⁺, C⁴⁺ near separatrix
- **SOL Stages**: C³⁺, C²⁺, C⁺, C⁰
- **Radiation Maximum**: Outside LCFS at low f_rad, inside at high f_rad
- **Detachment Indicator**: Inward shift of emission peak

### Transport Physics
- **Anomalous Diffusion**: 10²× larger than neoclassical
- **Turbulent Transport**: Dominant mechanism
- **Diffusivity Profile**: Higher at separatrix, lower in core
- **Convective Drift**: Set to zero (not well understood)
- **Parallel Loss**: τ_|| term in SOL (STRAHL approximation)

### Detachment Signatures
- **Radiation Shift**: From SOL to inside LCFS
- **Core/SOL Ratio**: Turnover at f_rad = 100% (70/30 split)
- **Profile Steepening**: Reduced n_e, T_e at separatrix
- **Emission Condensation**: At X-points and magnetic islands
- **Carbon Stages**: Shift to lower ionization states at LCFS

## LaTeX Patterns

### Custom Commands Used
- `\ix{text}`: Text subscripts extensively (e.g., `N\ix{p}`, `\tau\ix{w,p}`)
- `\diff`: Upright differential in equations
- `\head{text}`: Superscript text (e.g., `Q\head{ion}`, `Q\head{rec}`)
- `\coloneqq`: Definition symbol (≔)
- `\mathrel{\hat{=}}`: Correspondence symbol
- `\oint\ix{FS}`: Flux surface integral
- `\displaystyle\lim`: Display-style limit

### Mathematical Environments
- `empheq[box=\fbox]{align}`: Boxed equations for key definitions
- Extensive use of `\begin{split}` for multi-line equations
- `\nonumber` to suppress equation numbering
- `\label{eq:...}` for cross-referencing

### Figure Environments
- `minipage` for side-by-side figures and captions
- `subcaptionbox{}{}` for subfigures
- `\captionof{figure}` for captions in minipage
- `\parbox` for labeled subfigures (a), (b), etc.

### Special Notation
- Superscripts for ionization: `C^{6+}`, `C^{5+}`, etc.
- Functional notation: `f(t, S, P\ix{rad})`
- Set notation: `S \subset (S\ix{HBC}, S\ix{VBC})`
- Averaging: `\overline{\vartheta}\ix{n}^{(m)}`
- Flux surface average: `\langle ... \rangle\ix{FS}`

## Key Results Summary

### Impurity Seeding Models
- **Two-Chamber**: Successfully reproduces saturation with P_rad ∝ N_p
- **Three-Chamber**: Better physical model, SOL dominates (N_s >> N_p, N_w)
- **Validation**: Both models fit experimental data from XP20180920.49
- **Insight**: Time constants and chamber capacities crucial for understanding feedback response

### LOS Sensitivity Evaluation
- **Optimal Channels**: Separatrix, magnetic islands, X-points
- **Prediction Accuracy**: ≥85% achievable with proper selection
- **Selection Size**: m=7 most robust, m=3 requires careful channel choice
- **Metric Comparison**: Weighted deviation and mean deviation agree; correlation emphasizes temporal issues
- **Camera Agreement**: HBC and VBC results consistent

### STRAHL Simulations
- **Carbon Dominance**: 10¹-10² times more radiation than oxygen
- **Detachment Signature**: Inward shift of emission peak at high f_rad
- **Core/SOL Turnover**: 70/30 split at f_rad = 100%
- **Transport Impact**: Reduced diffusivity increases emissions near LCFS
- **Profile Impact**: Lower T_e,a, n_e,a shifts emissions inward
- **Validation**: Supports experimental detachment observations

### Answers to Key Questions
1. **Optimal LOS Set**: No single best set, but robust selections exist (separatrix, islands, X-points)
2. **Dominant Contributors**: Carbon impurities + reduced T_e,a, n_e,a + transport changes at separatrix

## Connections to Other Chapters
- **Chapter 1**: Bolometer diagnostic system and LOS geometry
- **Chapter 2**: Feedback experiments (XP20181010.32, XP20180920.29, etc.)
- **Chapter 0**: Plasma physics fundamentals (transport, radiation, impurities)
- **Appendix**: Additional STRAHL variations and experimental data (referenced)

## Future Work Implications
- Optimize LOS selection for specific scenarios
- Improve forward modeling to capture poloidal asymmetry
- Extend STRAHL to include SOL transport more accurately
- Investigate oxygen contribution at different conditions
- Develop real-time metrics for feedback quality assessment