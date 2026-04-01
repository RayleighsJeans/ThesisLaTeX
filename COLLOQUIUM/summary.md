# COLLOQUIUM Presentation Summary

## Overview
PhD defense presentation on "Impurity Transport and Radiation at the Stellarator W7-X" focusing on bolometry diagnostics and real-time radiation feedback control.

## Structure

### 1. Motivation (Lines 1-118)
- **Nuclear Fusion Challenge**: Lawson criterion for net energy gain (n_e·T·τ_E ≥ 3×10²¹ keV·s/m³)
- **Wendelstein 7-X**: World's most advanced stellarator, island divertor concept
- **Key Challenge**: Managing heat loads on plasma-facing components during long, high-performance plasma
- **Solution**: Detachment through controlled radiation (f_rad ≥ 90%)
- **Plasma Radiation**: Impurity seeding (He, N₂, Ne, Ar) to enhance edge radiation and cooling
- **Physics**: Bremsstrahlung and line radiation mechanisms, temperature-dependent radiation losses

### 2. Core Bolometer at W7-X (Lines 121-253)
- **Metal Resistor Bolometers**: 
  - Thin gold film absorbers on Si₃N₄ substrate
  - Wheatstone bridge circuit configuration
  - Multicamera system: HBC (32 channels) + VBCl/r (2×24 channels)
  - Spatial resolution: ~5 cm at magnetic axis
- **Performance Characteristics**:
  - Broadband measurement (600 nm to 0.2 nm wavelength range)
  - Near unity absorption efficiency
  - In-situ ohmic heating calibration
  - Sampling: 0.4-6.4 ms, SNR > 1000
  - Gaussian uncertainty: 1.6 μW
- **Applications**: Power balance calculations, tomographic reconstruction, real-time feedback control

### 3. Real-Time Radiation Feedback Control (Lines 255-461)
- **System Architecture**:
  - Integrated data acquisition hardware (NI 6321)
  - PID controller with thermal helium beam gas valves
  - Twin radiation prediction proxies
- **Prediction Methods**:
  - P_pred^(1): Channel selection (3-7 channels, geometric corrections)
  - P_pred^(2): Single channel voltage (minimal overhead, fastest response)
- **Performance**:
  - Minimum acquisition latency: 13.6 ms
  - Total system latency: 150-400 ms (dominated by plasma response)
  - FIFO smoothing adds ~8 ms delay
- **Experimental Achievement (XP20181010.32)**:
  - Duration: 9.2 s with P_ECRH = 6.23 MW
  - Radiation fraction: f_rad ≥ 90% sustained, peaks at 100%
  - Target heat load reduction: factor ≥ 2
  - C²⁺ detachment signature visible at f_rad ~ 50%
  - **Key Result**: First stable, feedback-controlled radiative cooling without plasma disruption

### 4. Line-of-Sight Sensitivity (Lines 463-536)
- **Analysis**: Evaluated 45 discharge pairs from OP1.2b campaign
- **Metrics**: 5 different metrics (linear/weighted deviation, FFT analysis)
- **Optimal Channel Selection**:
  - No single "best" set exists
  - Robust selection achieves ≥ 85% prediction accuracy
  - VBC channels generally outperform HBC for edge sensitivity
  - 3-5 channels sufficient for reliable P_pred
- **Key Finding**: Detectors viewing close to separatrix and SOL most viable for feedback

### 5. Tomography (Lines 538-1071)
- **Minimum Fisher Regularization (MFR)**:
  - Ill-posed problem: 61 measurements → ~4500 pixels
  - Regularization using Fisher information theory
  - Radially Dependent Anisotropy (RDA) weighting
- **Grid Configuration**: 30×150 pixels, domain 1.3² times plasma volume
- **Anisotropy Parameters**:
  - k_ani < 1: favors anisotropy (edge, localized structures)
  - k_ani > 1: favors smooth emissivity (core, flux-surface aligned)
  - Typical: k_core ≈ 2-5, k_edge ≈ 0.3-0.6
- **Benchmarking**:
  - 12+ synthetic emissivity profiles tested
  - Geometry perturbation studies (±2° camera tilts)
  - Detector/aperture segmentation: N ≥ 8 adequate
  - Reconstruction quality ≥ 80% for well-constrained phantoms
- **Quality Metrics**:
  - χ² (chi-squared) for measurement fit
  - ρ_c (correlation coefficient) for profile similarity
  - MSD (mean squared deviation)
  - P_rad,2D vs P_rad comparison
- **Experimental Reconstructions**:
  - Applied to OP1.2b feedback-controlled discharges
  - Reveals radiation moving from core to edge during detachment
  - Resolves localized structures (X-point radiation, MARFEs)
  - Agreement within 10-20% with bolometer sum
- **Power Balance**:
  - 0D energy conservation: P_bal = -P_H + P_rad + P_div + dW/dt
  - P_2D improves balance accuracy and stability
  - Integrated 2D core emissivity nearly satisfies P_bal = 0
  - Viable alternative for quasi-steady-state analysis

### 6. Conclusions (Lines 1159-1215)
**Three Major Achievements**:
1. **Real-Time Radiation Feedback System**:
   - First bolometer radiation feedback at W7-X
   - Stable detachment with f_rad ≥ 85%
   - Target heat load reduction factor ≥ 2
   - Validated 3-5 channel LOS subsets (≥80% accuracy)

2. **Line-of-Sight Optimization**:
   - Systematic sensitivity analysis
   - Separatrix and SOL viewing channels most effective
   - Multiple viable configurations (M ≥ 5)

3. **Tomographic Reconstruction**:
   - Benchmarked MFR algorithm with RDA weighting
   - Extensive phantom testing and parameter variation
   - Reconstruction quality ≥ 80%
   - Successful with experimental data and power balance

### 7. Outlook (Lines 1217-1268)
**System Upgrades**:
- Reduce feedback latency < 10 ms
- Implement machine learning for P_pred/LOS selection
- Per-experiment configuration (K_M, V_M)
- Predictive scaling laws for gas injection

**Modeling Improvements**:
- Integration with EMC3-EIRENE and other codes
- Better parametric optimization (Bayesian methods)
- Validation against spectroscopy

**Tomography Extensions**:
- Larger phantom benchmark set (>50 cases)
- Real-time algorithms (GPU acceleration)
- Automated parameter optimization (grid search, ML)

## Technical Details

### Custom LaTeX Commands Used
- `\ix{text}`: Text subscripts (e.g., `n\ix{e}` → n_e)
- `\diff`: Upright differential (e.g., `\diff t`)
- `\tenpo{n}`: Powers of 10 (e.g., `\tenpo{21}` → 10²¹)

### Key Physics Parameters
- Lawson criterion: n_e·T·τ_E ≥ 3×10²¹ keV·s/m³
- Operating temperature: T ~ 10-100 keV
- Radiation fraction target: f_rad ≥ 90%
- Spatial resolution: ~5 cm at magnetic axis
- Time resolution: 0.8-6.4 ms

### Experimental Campaign
- OP1.2b (2018): 61 functional bolometer channels
- Benchmark discharge XP20181010.32: 9.2 s, 6.23 MW ECRH, 55 MJ total energy
- 45 discharge pairs analyzed for LOS optimization

## Presentation Flow
1. Introduce fusion energy challenge and W7-X stellarator
2. Explain bolometer diagnostic system and capabilities
3. Demonstrate real-time feedback control system and results
4. Present LOS sensitivity analysis and optimization
5. Show tomographic reconstruction methods and validation
6. Conclude with achievements and future directions
7. Backup slides with detailed technical information

## Key Messages
- First successful real-time bolometer feedback at W7-X
- Achieved reactor-relevant high-radiation scenarios (f_rad ≥ 85-90%)
- Comprehensive diagnostic characterization and optimization
- Validated tomographic reconstruction for 2D radiation analysis
- Clear path forward for system improvements and reactor applications

---

## BACKUP SLIDES (Appendix Content - Lines 1324-3007)

### Feedback System Comparisons
- **Dispersion Interferometer Feedback (XP20181016.16)**: Alternative feedback using density measurements
- **C-III Filterscope Feedback (XP20180920.32)**: Spectroscopic feedback using C²⁺ radiation
- Both methods compared against bolometer feedback - bolometer provides most direct radiation measurement

### Bolometer Technical Details

#### Line-of-Sight Geometry
- **Volume per Camera**: V_M calculations for each detector
- **Etendue (K_M)**: Geometric light collection efficiency
  - Formula: K̃_M = ∬(cos(α)cos(β))/(4πd²) dA_M dA_A
  - Accounts for partial shadowing and non-perpendicular incidence
  - HBC: 175 mm aperture-detector distance
  - VBC: 84 mm aperture-detector distance
- **Effective Radius**: r_eff,M calculated from geometry matrix T
- **Transmission Maps**: 2D etendue distribution across detector surface

#### Temperature Drift and Calibration
- **Thermal Interference**: Camera enclosure heating (10 kW/m² loads)
- **Drift**: 50-150 μV/K (composition-dependent)
- **Mitigation**: Linear drift correction, Pt100 monitoring, water cooling
- **Material Properties (Au)**: 
  - Heat capacity: 25 J/(K·mol)
  - Cooling time: 0.13 ms/K
  - Resistivity: 0.008 nΩ·m/K

#### In-Situ Wheatstone Bridge Calibration
- **Method**: Ohmic heating with U_cal = 1.2-2.5 V for 1.6 s per stage
- **Extracted Parameters**: R_M, τ_M, κ_M from exponential decay fit
- **Cable Parameters**: R_L = 10 Ω, R_C = 40 Ω, C_C = 2 nF
- **Quality Criterion**: 3% deviation from reference

#### OP1.2b Campaign Statistics
- **61 functional detectors** across 1182 experiment programs
- **Calibration Stability**:
  - Resistance R_M: 0.987 ± 0.011 Ω
  - Heat capacity κ_M: 0.724 ± 0.055 A²
  - Cooling time τ_M: 110.57 ± 4.93 ms
  - Offset V_off: 0.204 ± 31.11 μV
- **Acquisition Performance**:
  - Noise σ_ΔU: 0.339 ± 12.586 μV
  - Drift V_drift: 0.057 ± 27.621 μV/s
  - SNR > 1000 (30 dB) in high radiation
  - Signal median: 0.042 ± 0.032 mV
  - Signal maximum: 1.186 ± 3.704 mV

#### Bolometer Equation Derivation
- **Wheatstone Bridge**: AC excitation (5 V, kHz) removes 1/f noise
- **Bridge Imbalance**: ΔU/U_ex ≈ ΔR/(2R)
- **Power Balance**: κ(dΔT/dt) = P_bol - κΔT/τ
- **Final Equation**: P_bol = (2Rκ)/(U_ex αRτ)(ΔU + τ dΔU/dt)

#### Measurement Algorithm
- **Stage 1 - Initialization** (T1-60s): Load geometry matrices, configure channels
- **Stage 2 - Calibration** (4s): Offset measurement, two-stage calibration
- **Stage 3 - Measurement** (~T1-5s): Continuous voltage integration, moving average filtering
- **Real-time Feedback**: Parallel analog output via NI 6321, FIFO buffer management
- **Data Storage**: Local HDD backup, W7-X archive upload

### Impurity Transport Modeling (STRAHL)

#### STRAHL Code Basics
- **1D impurity transport simulation** solving radial continuity for each ionization stage
- **Flux-surface averaged** diffusion D* and convection v*
- **Source terms**: Ionization, recombination, charge exchange
- **Numerical method**: Crank-Nicolson implicit scheme

#### Key STRAHL Results
- **Carbon dominates emissivity**: C²⁺/C³⁺ levels 100× higher than oxygen
- **Inward radiation shift**: For f_rad → 100%, peak moves to r ~ 0.95r_a
- **Radiation moves inside separatrix** as detachment develops
- **Forward modeling discrepancy**: Asymmetry less than experiments, suggesting intrinsic geometry effects

#### STRAHL Parameter Variations
- **Radiation fraction**: 90% vs 100% shows dramatic profile changes
- **Transport profiles**: Anomalous diffusion D_⊥ ≈ 0.1 m²/s near separatrix
- **Profile decay length**: Primarily affects SOL
- **Impurity source location**: Affects ion distributions
- **LCFS profile variations**: Core results relatively stable

#### Radiation Fraction Dependence
- **f_rad = 90%**: Peak radiation in SOL
- **f_rad = 100%**: Peak shifts to LCFS/separatrix
- **C³⁺ and C²⁺ most sensitive** to f_rad changes
- **Implications**: LOS sensitivity depends on f_rad, validates feedback design

### Impurity Seeding Models

#### Two-Chamber Model
- **Compartments**: Plasma and wall
- **Equations**: 
  - Ṅ_w = (N_w,lim - N_w)τ_w,p
  - Ṅ_p = Γ_s + N_w τ_w,p - f_w,p N_p - N_p τ_p
- **Parameters**: Particle exchange rates, pumping, recycling

#### Three-Chamber Model
- **Adds SOL compartment** for better edge physics representation
- **Equations include**: SOL-plasma exchange, non-linear coupling g(N_P, N_S)
- **Both models** equally capable of representing feedback measurements
- **Application**: Successfully reproduces XP20180920.49 radiation evolution

### Power Balance Details

#### 0-D Energy Conservation
- **Starting point**: 3D fluid equations integrated over volume
- **Components**:
  - P_ECRH: Input heating (±10% error)
  - P_rad: Radiation loss (±5% error, +25% vessel contribution)
  - P_div: Divertor target load (±10% error)
  - W: Stored energy (W_dia preferred over W_kin)
- **Challenges**: Large error bars, fast transitions poorly described, toroidal asymmetries

### Tomography Advanced Topics

#### Camera Geometry Sensitivity
- **Axisymmetric HBC aperture**: Designed location slightly off-axis
- **Unilateral mirrored HBC**: Half array mirrored, minimal impact (0.5-1% asymmetry reduction)
- **Validates**: Manufacturing tolerances acceptable

#### Segmentation and LOS Cones
- **Detector/aperture splitting**: N ≥ 8 provides adequate resolution
- **Rectangular splitting** at N=2 vs N=8 comparison
- **Full cone vs infinitesimal projection** analysis

#### RDA vs RGS Comparison
- **Relative Gradient Smoothing (RGS)**: Can combine with RDA
- **RGS advantages**: Stronger feature localization, higher local intensities
- **RDA chosen**: Better balance of accuracy and robustness

#### Artificial Camera Concepts
- **VBCm (mirror)**: Conceptual vertical camera for improved coverage
- **MIRh (mirrored horizontal)**: Additional horizontal viewing geometry
- **4-camera system**: Includes MIRh, improves reconstruction quality

#### Edge Case Phantoms
- **Inverted anisotropy**: Bright SOL ring + core anisotropy (k_ani = {3, 20})
- **Homogeneous distribution**: Unit/null test confirms no artificial pattern generation
- **Tests algorithm limits** and robustness

### Line-of-Sight Sensitivity Detailed Analysis

#### Cross-Correlation Metric
- **Formula**: φ(t) = ∫ P_pred(τ)P_rad(t+τ)dτ
- **Results**: Large error bars (up to 40%), distinct maxima at ±0.85r_a
- **Key finding**: X-point channels show poor temporal correlation
- **Emphasizes**: Temporal behavior, sensitive to localized perturbations

#### Mean Deviation Metric
- **Formula**: φ(t) = (P_rad(t) - P_pred(t))²/(T_stop - T_start)
- **Results**: Error bars 20-40%, local maxima at -0.28r_a and 0.6r_a
- **Quality scales** with selection size m
- **Conclusion**: Outermost boundary-viewing LOS unfavorable for feedback

#### FFT Correlation Metric
- **Uses**: Spectral correlation with discrete FFT
- **Cross-spectral density**: Coherence-based metric
- **Results**: Similar patterns to correlation, global maximum at upper inboard X-point
- **Advantages**: Frequency domain analysis, identifies oscillatory behavior

#### Plasma Parameter Correlations
- **Optimal conditions**:
  - Higher P_ECRH (≥ 3.5 MW) → better predictability
  - Optimal 0.4 < f_rad < 0.75
  - Core T_e ~ 1.3 keV ideal
  - Both HBC and VBC cameras in good agreement
- **Validates**: High f_rad scenarios work well with feedback system

### DAQ Latency Testing
- **Laser test results** for various sample times (0.8, 1.6, 3.2 ms)
- **With/without real-time feedback** branch comparison
- **Samples per half period** and sample time distributions
- **Confirms**: Minimum latency 13.6 ms achievable

## Technical Specifications Summary

### Bolometer System
- 128 total channels (61 functional in OP1.2b)
- 3 camera arrays: HBC (32), VBCl (24), VBCr (24)
- Spatial resolution: ~5 cm at magnetic axis
- Time resolution: 0.8-12.8 ms configurable
- SNR > 1000 in high radiation scenarios
- Absolute calibration: in-situ ohmic heating method

### Feedback Control
- Minimum latency: 13.6 ms (acquisition)
- Total system latency: 150-400 ms (including plasma response)
- PID controller with thermal He beam valves
- Two prediction methods: multi-channel and single-channel
- Validated channel subsets: 3-5 channels sufficient for ≥85% accuracy

### Tomographic Reconstruction
- MFR with RDA weighting
- Grid: 30×150 pixels (radial × poloidal)
- Domain: 1.3² times plasma volume
- Anisotropy parameters: k_core ≈ 2-5, k_edge ≈ 0.3-0.6
- Reconstruction quality: ≥80% for well-constrained cases
- Computational time: ~seconds per frame (post-shot analysis)