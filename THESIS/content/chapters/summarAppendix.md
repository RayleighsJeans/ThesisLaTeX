# Appendix Summary

## Overview
The appendix contains three major chapters providing detailed technical documentation:
- **Appendix A**: Complete bolometer measurement algorithm (pseudocode)
- **Appendix B**: Extended LOS sensitivity analysis and STRAHL modeling details
- **Appendix C**: Additional MFR tomography validation and geometry studies

Total: 575 lines covering algorithmic implementation, extended analysis methods, and supplementary reconstruction tests.

---

## Appendix A: Measurement Algorithm (Lines 2-111)

### Algorithm Structure
Three-part pseudocode for complete bolometer system operation:

**Part 1: Initialization and Feedback Loop (Lines 4-38)**
- Trigger: T1 - 60s before plasma
- Load geometry matrices: K_M, V_M from standard geometry file
- Initialize NI® 6321 two-channel analog output
- Parallel feedback loop: continuously output P_pred^(1) and P_pred^(2) to FIFO

**Part 2: Calibration Procedure (Lines 42-70)**
- Mode register: ±80 mV full range
- Filter: 0.4 ms sample time
- V_off: 10s offset measurement
- Two-stage calibration (measurement + reference absorber):
  - 10,000 samples over 4s
  - Extract R, τ, κ from samples 2000-6000
  - κ: linear resistance change from ohmic heating
- Switch to individual range (10 mV, 20 mV)
- Initialize FIFOs: |S|×(M+2) array for channels, (M+1) for reference

**Part 3: Measurement and Data Storage (Lines 74-110)**
- Main loop: N+1000 samples (skip first 1000)
- For each sample i > 1000:
  - Integrate ΔU^(i) over Δt
  - Store in circular FIFO (mod M)
  - Calculate M-sample moving average
  - Compute derivative: d(ΔŨ)/dt
  - Calculate P_pred^(1) using Eq. 2.4 (K_M, V_M, derivatives)
  - Calculate P_pred^(2) using Eq. 2.5 (reference channel)
- Upload to HDD and W7-X archive: P_pred^(1,2), ΔU, κ, τ, R, calibration currents

### Key Parameters
- **Inputs**: Δt, ranges, S (channel selection), c (reference), N (samples), M (averaging window), V_M, K_M
- **Outputs (runtime)**: P_pred^(1), P_pred^(2)
- **Outputs (post)**: calibration data, κ, τ, R, ΔU, P_pred^(n)

---

## Appendix B: Feedback Evaluation and STRAHL (Lines 112-299)

### B.1: Fourier Transform Correlation (Lines 116-183)

**Mathematical Framework:**
```
γ_i = F(∫ P_rad(t-τ) dτ)(ω)
γ_j = F(∫ P_pred(t-τ) dτ)(ω)
g_{i,j}(ω) = (1/T) ∫ γ_i(ω) γ_j(ω-ν) dν

φ(ω) = √(|g_{i,j}²|/|γ_i γ_j|)
ϑ = ∫ φ(ω) dω
```

**Implementation:**
- Uses NumPy DFFT (Discrete Fast Fourier Transform)
- Spectral domain: [0, N/(2Δt)]
- φ(ω): coherence-like metric (spectral power per frequency)
- ϑ: integrated prediction quality (a.u.)

**Results (Figure 3.A.2):**
- HBC: Global maximum at 0.38r_a (upper inboard X-point)
- VBC: Global maximum at -0.13r_a (same X-point region)
- Quality range: 2-6×10⁴ a.u.
- Local maxima: -0.4r_a, 0.7r_a (HBC); -0.75r_a, -0.35r_a, 0.65r_a (VBC)
- m=7 provides highest quality for VBC
- Spectral correlation confirms X-point sensitivity from correlation metric

**Key Finding:** Shift of HBC global maximum from -0.85r_a (correlation) to 0.38r_a (FT correlation) indicates spectral sensitivity differs from absolute value sensitivity.

### B.2: Plasma Parameter Sensitivity (Lines 184-258)

**Mapping Function:**
```
ϑ := f(S, φ*, plasma parameters): ℕ^m × ℝ^n → ℝ
```

**Parameters Analyzed (Figure 3.A.3):**
1. **P_ECRH** (microwave heating): 3.6-4.2 MW
2. **f_rad** (radiation fraction): 0.1-0.8+
3. **T_e,out** (core electron temperature): 0.9-1.3 keV

**Correlation Results:**
- **Gap in ϑ**: 0.3-0.5 a.u. (negligible plasma parameters)
- **High P_ECRH** (≥4.2 MW) → high ϑ (0.5-0.85 a.u.)
- **High f_rad** (>0.75) → improved ϑ around 0.75 a.u.
- **High T_e** (∼1.3 keV) → best ϑ at <0.4 a.u. for r<0.4r_a
- **Optimal conditions**: P_ECRH ≥ 3.5 MW, T_e ∼ 1.3 keV, f_rad > 0.75

**Conclusion:** Optimal LOS sets exist for given plasma parameters. Discharge configurations identified for positive correlation with real-time prediction quality.

### B.3: STRAHL Experimental Data (Lines 261-299)

**Extended Results for f_rad = 90% and 100% (Figure 3.A.4-5):**

**Fractional Abundances (edge/SOL):**
- C^6+: Declines to separatrix, 10-25% at divertor
- C^5+: Local max near LCFS, 5-25% at boundary
- C^3+: Shifts from 1.15r_a (90%) to 0.975r_a (100%)
- C^2+: Peak moves from 1.12r_a (90%) to just inside LCFS (100%)

**Emissivity Changes (90% → 100%):**
- P_3+: Peak shifts inward by ~5 cm, from 50 kW/m³ (SOL) to sharper max at 0.975r_a
- P_2+: Starts increasing at LCFS instead of beyond
- P_4+, P_5+: Greatly increased inside separatrix
- Total: Shifts from SOL-dominated (80 kW/m³) to LCFS-centered

**Physical Interpretation:**
- Small T_e changes (6 eV, ~10%) → 2× SOL emissivity increase
- 10% higher f_rad → drastic profile changes (quantitative + qualitative)
- Only f_rad = 100% results relevant for feedback LOS sensitivity
- Critical for modeling (controlled) detachment processes

### B.4: STRAHL Parameter Variations (Lines 300-381)

**B.4.1: Decay Length Variation (λ = 5 cm vs 2 cm)**

**Kinetic Profiles (Figure 3.A.6):**
- λ = 2 cm: n_e drops faster in SOL
- T_e: minimal change
- Core profiles: unchanged

**Fractional Abundances:**
- SOL increases: C^6+ (+12%), C^5+ (+5%), C^4+ (+2%)
- SOL decreases: C^3+ (-6%), C^2+ (-10%), C^1+ (to 5%)
- Profiles flat/continuous outside LCFS to 1.1r_a

**Emissivities (Figure 3.A.7):**
- λ = 2 cm: C^1+ compressed radially (peak closer to LCFS, 20% vs 30%)
- C^2+: No second local max, linear drop
- C^3+: Contracted toward separatrix, sharp decline before 1.15r_a
- C^5+, C^4+: +7 kW/m³ in local max
- C^3+, C^2+: +10-30 kW/m³ inside LCFS
- P_tot: Core increments 5-30 kW/m³, SOL second max lost

**Conclusion:** Edge decay length greatly impacts SOL emissivity shape/height and indirectly affects core absolute values. No systematic radial shifts in core.

**B.4.2: Radial Source Variation (S at r_a vs r_a + 7.5 cm)**

**Fractional Abundances (Figure 3.A.8):**
- S → r_a: SOL increases C^6+ (+7%), C^5+, C^4+ at boundary
- C^2+, C^1+: Decrease 11% → 4%, 15% → 1%
- C atom: Missing step at divertor

**Emissivities:**
- S → r_a: Results nearly identical to λ = 2 cm case
- Core: Equal within negligible variations
- SOL: Steady decay from LCFS to zero before 1.15r_a
- C atoms: Up to 5 kW/m³ just inside core
- P_tot: Similar to reduced λ, less steep SOL drop

**Conclusion:** Source at LCFS yields similar core emissivity as reduced decay length. Higher C^6+ population (ionized at higher T_e/n_e, transported outward). Lower ion stages greatly decreased. No radial displacements found.

---

## Appendix C: Two-Dimensional Inversion (Lines 382-575)

### C.1: Camera Geometry Perturbations (Lines 384-433)

**C.1.1: Unilateral Mirroring (Channels 16-32)**

**Transformation:**
- Mirror plane: spanned by LOS fan normal and channel 15 direction
- Ch. 32 → mirror of Ch. 1 (rotated 53°)
- Ch. 31 → mirror of Ch. 2 (rotated 53° - angle(1,2))
- Etendue variation: <10^-13 mm^-3 (2 orders lower than before)

**Forward Model Results (Figure 4.A.1):**
- Variance between left/right halves: 0.5-1%
- Profiles from intrinsically symmetric geometry + radiation
- Asymmetry source: 68.75° LOS fan tilt
- Conclusion: Change 10^-2× smaller than segmentation variations → almost no forward calculation variation

**C.1.2: Artificial Symmetric Camera (Figure 4.A.2)**

**Construction:**
- Averaged absorber size, shape, spacing from original HBCm
- 32 identical detectors, upright, centered, equidistant
- Parallel centered aperture viewing plasma

**Etendue Variation:**
- Magnitude: ~10^-11 to 10^-16 mm^-3
- Local maxima: outboard side (closest to pinhole)
- Weaker poloidal structuring than before
- Individual LOS characteristics visible from aperture

**Forward Profiles:**
- f_rad = 1: Max ~240 kW/m³ (slightly reduced)
- Lower f_rad: Local extremes +50% intensity, further outside/beyond LCFS
- Overall shape: very similar

**Conclusion:** Small T changes (same order as segmentation) can significantly affect measurements/reconstructions. As-designed HBC local sensitivity very close to theoretical ideal geometry.

### C.2: Minimum Fisher Regularization (Lines 434-531)

**C.2.1: Relative Gradient Smoothing (RGS) (Lines 436-456)**

**Mathematical Framework:**
```
K → x^T H_RGS x ∝ (∇g/g)²

n = 0: W_RGS^(0) = 1
n ≥ 1: W_RGS^(n) = (1/g_i^(n))²
H_RGS^(n) = ∇_r^T W_RGS^(n) ∇_r + ∇̃_θ^T W_RGS^(n) ∇̃_θ
```

**Concept:** Regularizing weight becomes inverse square of emission profile (1/g).

**C.2.2: RDA vs RGS Comparison (Lines 457-506)**

**Phantom Setup (Figure 4.A.3-4):**
- Nested anisotropic structures: core (0.7r_a) + ring (r_a)
- Both asymmetric, same orientation (θ_0 = 0°)
- Core max: 2.5 MW/m³, ring: 50% of that
- σ_r = 0.25r_a, σ_θ = π/4
- k_ani = {0.3, 0.3} for both methods

**Results:**
- **1D profiles**: Minor/negligible differences
  - Within confidence intervals
  - Deviations similar to k_ani variations
  - Contradicting trends (some improve, some regress)
- **2D distributions**: RGS+RDA favored
  - Stronger separation core/SOL
  - Shorter poloidal decay lengths
  - Better total brightness/max match
  - More prominent localization
  - Drawback: Loss of less intense nearby structures

**Conclusion:** RGS+RDA doesn't justify unrestricted use over standard RDA based on 1D metrics alone. 2D subjective quality favors RGS+RDA for feature localization, but at cost of smoother extended structures.

**C.2.3: Inverted Anisotropic Phantom (Lines 507-531)**

**Configuration (Figure 4.A.5):**
- Reversed from previous: bright core (0.7r_a, 8 spots, 1.2 MW/m³) + smooth SOL ring (1.1r_a, 1 MW/m³)
- k_ani = {0.3, 0.2} (reversed profile)
- Challenge: SOL sensitivity may obfuscate core structure

**Results:**
- **Reconstruction quality**: Greater discrepancies than inverted case
- **Focus shift**: Majority brightness in SOL/edge (due to reversed k_ani)
- **Core features**: Max in similar locations, greatly decreased resolution
- **Missing features**: Vertically above VBC (unfavorable SOL/core integration ratio)
- **Metrics improved**: Better radial/forward match, P_rad,2D vs P_rad, χ²
- **Conclusion**: Experimentally measured distributions with this orientation more difficult to reconstruct for localized features

### C.3: Accessory Phantom Tomographies (Lines 532-575)

**C.3.1: Homogeneous Phantom (Figure 4.A.6)**
- Entire domain: 1 MW/m³ uniform
- k_ani = {1, 1} (equal weighting)
- Purpose: Baseline test for algorithm behavior

**C.3.2: Eight-Island Phantom (Figure 4.A.7)**
- Bright core ring (1.1r_a) + 8 island structures in edge
- k_ani = {2, 0.1} (support given profile)
- Similar to 6-island case but different configuration

---

## Key Equations

### Fourier Transform Correlation
```
γ_i = F(∫_{-∞}^∞ P_rad(t-τ) dτ)(ω)
γ_j = F(∫_{-∞}^∞ P_pred(t-τ) dτ)(ω)
g_{i,j}(ω) = (1/T) ∫_{-∞}^∞ γ_i(ω) γ_j(ω-ν) dν

φ(ω) = √(|g_{i,j}²|/|γ_i γ_j|)
ϑ = ∫_{-∞}^∞ φ(ω) dω
```

### Parameter Sensitivity Map
```
ϑ := f(S, φ*, plasma parameters): ℕ^m × ℝ^n → ℝ
```

### RGS Functional
```
K → x^T H_RGS x ∝ (∇g/g)²
W_RGS^(n) = (1/g_i^(n))²
H_RGS^(n) = ∇_r^T W_RGS^(n) ∇_r + ∇̃_θ^T W_RGS^(n) ∇̃_θ
```

---

## Figures

### Appendix A (Algorithm)
- **Algorithm 1 (3 parts)**: Complete bolometer measurement pseudocode

### Appendix B (Feedback/STRAHL)
- **Figure 3.A.1**: FT correlation example (m=3, HBC)
- **Figure 3.A.2**: FT correlation sensitivity (HBC, VBC, m=3,5,7)
- **Figure 3.A.3**: Parameter analysis (P_ECRH, f_rad, T_e vs ϑ)
- **Figure 3.A.4**: STRAHL f_rad=90%,100% (n_e, T_e, abundances)
- **Figure 3.A.5**: STRAHL f_rad=90%,100% (emissivities)
- **Figure 3.A.6**: Decay length variation (λ=5cm vs 2cm, profiles + abundances)
- **Figure 3.A.7**: Decay length variation (emissivities)
- **Figure 3.A.8**: Source variation (r_a vs r_a+7.5cm, abundances + emissivities)

### Appendix C (MFR)
- **Figure 4.A.1**: Unilateral mirroring (etendue + forward profiles)
- **Figure 4.A.2**: Artificial symmetric camera (etendue + forward profiles)
- **Figure 4.A.3**: RDA vs RGS comparison (2D tomograms)
- **Figure 4.A.4**: RDA vs RGS comparison (1D profiles)
- **Figure 4.A.5**: Inverted phantom (2D + 1D)
- **Figure 4.A.6**: Homogeneous phantom
- **Figure 4.A.7**: Eight-island phantom

Total: 15 figures

---

## Technical Specifications

### Algorithm Parameters
- **Timing**: T1 - 60s initialization
- **Calibration**: 10,000 samples over 4s, extract from samples 2000-6000
- **Voltage ranges**: ±80 mV (calibration), 10/20 mV (measurement)
- **Sample time**: 0.4 ms (calibration), Δt (measurement)
- **Offset**: 10s measurement
- **FIFO sizes**: |S|×(M+2) for channels, (M+1) for reference
- **Hardware**: NI® 6321 two-channel analog output

### FT Correlation
- **Spectral domain**: [0, N/(2Δt)]
- **Quality range**: 2-6×10⁴ a.u.
- **Implementation**: NumPy DFFT

### Optimal Plasma Parameters
- **P_ECRH**: ≥3.5 MW (best: 4.2 MW)
- **f_rad**: >0.75 (optimal around 0.75-0.85)
- **T_e**: ~1.3 keV

### STRAHL Variations
- **Decay lengths**: 5 cm (island), 2 cm (open field lines)
- **Source locations**: r_a, r_a + 7.5 cm (divertor)
- **f_rad levels**: 33%, 66%, 90%, 100%

### Geometry Perturbations
- **Etendue variations**: 10^-13 mm^-3 (mirroring), 10^-11 to 10^-16 mm^-3 (artificial)
- **HBC tilt**: 68.75°
- **Opening angle**: 53°

---

## Scientific Context

### Algorithm Implementation
- Complete real-time feedback system from initialization to data archival
- Parallel analog output during measurement
- Two-stage calibration with ohmic heating characterization
- Moving average filtering (M samples) with derivative calculation
- Dual prediction methods: geometry-based (P_pred^(1)) and reference-based (P_pred^(2))

### LOS Sensitivity Extensions
- **Fourier domain analysis**: Complements time-domain correlation
- **Spectral vs absolute sensitivity**: Different optimal LOS locations
- **X-point dominance**: Confirmed in both time and frequency domains
- **Parameter space mapping**: Identifies optimal discharge configurations

### STRAHL Physical Insights
- **Edge sensitivity**: Small T_e/n_e changes → large emissivity variations
- **Detachment modeling**: f_rad=100% results critical for feedback scenarios
- **Transport effects**: Decay length and source location impact SOL profiles
- **Carbon dominance**: 10²× oxygen emissions, C^3+/C^2+ critical near LCFS

### MFR Validation
- **Geometry robustness**: As-designed HBC close to ideal
- **Asymmetry sources**: 68.75° tilt causes 0.5-1% left/right variance
- **RGS trade-offs**: Better localization vs loss of extended structures
- **Orientation effects**: Inside-out phantoms more challenging to reconstruct

---

## LaTeX Patterns

### Algorithm Environment
```latex
\begin{algorithm}[H]
\SetKwInOut{Input}{input}\SetKwInOut{Output}{output}
\IncMargin{1em}
\SetAlgoLined
\KwResult{...}
\Input{...}
\Output{...}
\tcp{comments}
\While{condition}{...}
\For{...}{...}
\If{...}{...}
\caption{...}\label{...}
\end{algorithm}
```

### Multi-part Algorithm
- `\addtocounter{algocf}{-1}` to continue same algorithm number
- `\vdots` for continuation indicator

### Figure Layouts
- `\parbox` for custom column headers
- `\makebox[\textwidth][c]{...}` for oversized figures
- `\subcaptionbox{}{}` for subfigures with captions

### Math Notation
- `\coloneqq` for definitions
- `\mathcal{F}(\cdot)` for Fourier transform
- `\vert ... \vert` for absolute values
- `\tenpo{n}` for 10^n

---

## Connections to Main Chapters

### To Chapter 2 (Feedback)
- Algorithm provides complete implementation details for feedback system
- Parameter sensitivity identifies optimal discharge configurations
- Validates real-time calculation methods (P_pred^(1,2))

### To Chapter 3 (LOS Sensitivity)
- FT correlation extends time-domain analysis to frequency domain
- Parameter mapping confirms optimal LOS sets exist
- STRAHL variations validate edge sensitivity findings
- Confirms X-point dominance in spectral domain

### To Chapter 4 (MFR)
- Geometry perturbations validate reconstruction robustness
- RDA vs RGS comparison justifies chosen method
- Accessory phantoms extend validation test suite
- Confirms as-designed geometry near-optimal

### To Chapter 5 (Conclusions)
- Algorithm enables real-time feedback (key achievement)
- Parameter analysis guides future experiment planning
- Geometry studies support camera design decisions
- STRAHL results inform detachment control strategies

---

## Summary

The appendix provides essential technical documentation completing the thesis:

1. **Algorithm**: Full pseudocode for bolometer measurement and feedback system, from initialization through calibration to real-time prediction and data archival.

2. **Extended Analysis**: Fourier transform correlation metric validates time-domain findings, plasma parameter sensitivity mapping identifies optimal discharge configurations, and detailed STRAHL parameter variations confirm edge physics understanding.

3. **MFR Validation**: Geometry perturbation studies prove reconstruction robustness, RDA vs RGS comparison justifies method choice, and accessory phantoms extend validation coverage.

**Key Contributions:**
- Complete implementation reference for feedback system
- Frequency-domain confirmation of X-point sensitivity
- Optimal parameter space: P_ECRH ≥ 3.5 MW, f_rad > 0.75, T_e ~ 1.3 keV
- STRAHL edge sensitivity: small T_e changes → 2× emissivity variations
- Geometry validation: as-designed HBC near-ideal, 68.75° tilt causes <1% asymmetry
- RGS trade-off: better localization at cost of extended structure resolution

The appendix transforms the main chapters' findings into actionable technical documentation for future experiments and system development.