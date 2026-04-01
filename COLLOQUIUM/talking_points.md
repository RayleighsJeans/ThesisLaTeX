# PhD Defense Presentation - Talking Points Guide

**Bolometry Diagnostics and Real-Time Radiation Feedback Control at Wendelstein 7-X**

---

## TITLE SLIDE

- Welcome to my PhD defense on bolometry diagnostics and real-time radiation feedback control at Wendelstein 7-X
- This work addresses two critical challenges for future fusion reactors: (1) protecting plasma-facing components through controlled radiation, and (2) achieving stable detachment at high radiation fractions (f_rad≥85%)
- Three main contributions: implemented first bolometer-based real-time feedback at W7-X, optimized channel selection through systematic sensitivity analysis, and validated MFR tomography with radially dependent anisotropy weighting

---

## CONTENTS

- Presentation structure: (1) Motivation - fusion energy and W7-X challenges, (2) Bolometer diagnostic system - 94 channels with ~5cm spatial resolution, (3) Real-time feedback - achieved f_rad≥85% with factor ≥2 heat load reduction, (4) LOS sensitivity - identified optimal channel configurations, (5) Tomography - MFR with RDA for 2D radiation reconstruction, (6) Conclusions and future work

---

## MOTIVATION

### Nuclear Fusion: Energy Challenge

- Nuclear fusion through D-T reactions offers clean, abundant energy - deuterium from seawater, tritium bred from lithium
- Lawson criterion: n_e·τ_E·T ≥ 3×10²¹ keV·s/m³ defines conditions for net energy gain (Q>1)
- Requires extreme conditions: T~10-20 keV (100-200 million °C) and confinement time τ_E~1-10s
- Magnetic confinement uses strong fields (2.5T at W7-X) to contain hot plasma away from material walls
- Stellarators like W7-X achieve steady-state operation through 3D-shaped coils, unlike pulsed tokamaks

### Wendelstein 7-X

- W7-X is the world's largest and most advanced stellarator: R=5.5m, a=0.53m, B=2.5T, optimized for steady-state operation
- Key challenge: managing heat loads on plasma-facing components during long pulses (up to 30 minutes planned)
- Island divertor concept: 5 helical island chains intercept heat flux, connection lengths 100-1000m (10-100× longer than tokamaks)
- Detachment strategy: radiate power in scrape-off layer and edge to reduce divertor heat loads from ~10 MW/m² to <5 MW/m²
- Goal: achieve stable detachment at f_rad≥85-90% without plasma disruption while maintaining core performance
- This requires real-time control of radiation distribution - motivation for bolometer feedback system

### Plasma Radiation

- Plasma radiation mechanisms: (1) Bremsstrahlung (free-free transitions, ~T_e^(1/2)), (2) Line radiation (bound-bound, temperature-dependent), (3) Recombination (free-bound)
- Impurity seeding strategy: inject low-Z (N₂) or high-Z (Ne, Ar) gases to enhance edge radiation while avoiding core contamination
- Carbon and oxygen are intrinsic impurities from wall interactions - carbon dominates by factor 10²× over oxygen at W7-X
- Radiation cooling function P_rad/(V·n_e·n_imp) peaks at different temperatures for each impurity: C peaks ~10-50 eV (edge), O peaks ~100 eV
- Transport in W7-X: neoclassical baseline with anomalous contributions from turbulence (ITG, TEM modes)
- Anomalous transport increases diffusion by factor 10-100 over neoclassical, critical for impurity transport modeling
- Radiation fraction f_rad = P_rad/P_ECRH must be balanced: f_rad<70% insufficient for divertor protection, f_rad>95% risks core cooling and confinement degradation
- Optimal operating window: f_rad=85-90% achieves detachment while maintaining plasma stability

---

## CORE BOLOMETER AT W7-X

### Bolometer Diagnostic (Hardware)

- Bolometers measure total plasma radiation power (broadband, 0.2-600 nm) through resistive heating of metal absorbers
- Metal resistor design: thin gold film (1.5 μm) on mica substrate, absorbs radiation → temperature increase → resistance change
- Wheatstone bridge configuration: AC excitation (5V, kHz) eliminates 1/f noise, differential measurement doubles signal
- Three camera arrays provide comprehensive plasma coverage: HBC (32 channels, horizontal), VBCl/r (2×31 channels, vertical)
- Total 94 channels installed, 61 functional in OP1.2b campaign (some damaged by ECRH stray radiation)
- Each channel integrates radiation along line of sight - use geometry matrix T and etendue K_M to reconstruct 2D distribution
- Spatial resolution ~5 cm at magnetic axis, determined by etendue width and viewing geometry

### Performance

- Calibration is critical for absolute power measurements - three methods used: (1) laser, (2) electrical ohmic heating, (3) in-situ during operation
- In-situ ohmic heating calibration: apply U_cal=1.2-2.5V for 1.6s, measure current evolution I(t), extract R_M, τ_M, κ_M from exponential decay
- Calibration parameters (OP1.2b median): R_M=0.987±0.011 Ω, κ_M=0.724±0.055 A², τ_M=110.57±4.93 ms, remarkably stable across 1182 experiments
- Etendue K_M quantifies geometric light collection efficiency: accounts for detector-aperture geometry, partial shadowing, angle-dependent transmission
- Time resolution configurable: {0.4, 0.8, 1.6, 3.2, 6.4, 12.8} ms sampling available, 1.6ms used for feedback (balances speed vs noise)
- Performance metrics: SNR>1000 at high radiation, noise σ_ΔU=0.339±12.586 μV, Gaussian error 1.6 μW, drift 0.057±27.621 μV/s
- Chord brightness P_ch = P_M/K_M provides radial profile information - shows radiation distribution from core to SOL
- Absorption efficiency near unity (>95%) across 0.2-600 nm wavelength range - truly broadband measurement

---

## REAL-TIME RADIATION FEEDBACK CONTROL

### Feedback System (Island Divertor)

- W7-X island divertor concept: 5 helical island chains (m/n=5/5) at plasma edge intercept heat and particle flux
- Each island chain has upper and lower divertor modules - 10 modules total arranged helically around torus
- Connection lengths L_c=100-1000m (10-100× longer than tokamaks) allow extensive radiation cooling along field lines
- Standard magnetic configuration: ι/2π=1 (rotational transform), creates 5-fold symmetric island structure
- Gas injection system: 10 piezo valves for fast response (<10ms), thermal helium beam valves for feedback control
- Valve locations strategically placed: HM1-5 modules (upper/lower pairs) allow targeted seeding into specific island chains
- Island X-points are radiation hot spots - field lines converge, increasing local emissivity by factor 2-5×
- Bolometer cameras positioned to view these X-points - critical for feedback sensitivity
- Field line tracing shows direct connection between gas injection points and divertor targets via island chains

### Feedback System (Implementation)

- First bolometer-based real-time radiation feedback system at W7-X, operational during OP1.2b campaign (2018)
- Hardware: NI 6321 DAQ card for fast acquisition, dedicated analog outputs for PID controller, parallel processing architecture
- Two prediction proxies implemented: (1) P_pred^(1) = geometry-weighted sum over selected channels S, (2) P_pred^(2) = single channel voltage (dimensionless, minimal overhead)
- Channel selection S optimized through systematic analysis: VBC subset S={61,65,73,78,86} viewing separatrix and X-points achieves ≥85% accuracy
- Alternative HBC selections also viable: S={4,7,8,20,23,27} provides similar performance with different viewing geometry
- PID controller parameters: K_p=0.5-2.0 (proportional gain), K_i=0.1-0.5 (integral), K_d=0 (derivative not needed due to slow plasma response)
- Setpoint: f_rad target (typically 85-90%), controller adjusts gas valve opening to maintain radiation fraction

### Feedback System (Latency)

- System latency breakdown: acquisition 13.6ms (minimum, validated with laser diode), FIFO smoothing ~8ms (M=10 samples × 1.6ms), processing <1ms
- Total feedback loop latency: 150-400ms dominated by plasma response time (gas transport, ionization, radiation buildup)
- FIFO moving average filter: reduces noise by factor √M but adds latency M·Δt/2 ≈ 8ms for M=10
- Trade-off: faster sampling (Δt=0.8ms) reduces latency but increases noise, 1.6ms optimal for feedback application
- Benchmark test with laser diode: confirmed 13.6ms acquisition latency, validated timing chain from photon to digital signal
- Future improvements: reduce acquisition to <10ms through hardware upgrades, implement predictive algorithms to compensate for plasma response delay
- Comparison: Thomson scattering ~50ms, interferometry ~1ms, but bolometry measures the actual control variable (radiation)

### Experimental Achievements (XP20181010.32)

- XP20181010.32 - breakthrough experiment achieving stable feedback-controlled detachment with hydrogen seeding
- Discharge parameters: duration 9.2s, P_ECRH=6.23 MW, standard magnetic configuration (ι/2π=1), total input energy 55 MJ
- Key achievement: sustained f_rad≥85% with peaks reaching 100% (P_rad=P_ECRH), no plasma disruption or termination
- Divertor heat load reduction: factor ≥2× from baseline ~10 MW/m² to <5 MW/m², validated by infrared thermography
- Detachment signatures: C²⁺ filterscope emission appears at f_rad~50%, intensifies and moves poloidally as f_rad increases
- Prediction accuracy: P_pred^(1) tracks P_rad within 10-15% throughout discharge, validates 5-channel VBC subset S={61,65,73,78,86}
- Plasma stored energy W_dia maintained at ~0.8-1.0 MJ despite high radiation - demonstrates compatibility with good confinement
- This demonstrates reactor-relevant scenario: high f_rad for component protection while maintaining plasma performance

### Experimental Achievements (Discussion)

- Bolometer feedback advantages: (1) directly measures control variable (total radiation), (2) broadband - insensitive to impurity mix, (3) fast response (1.6ms sampling)
- Comparison with alternatives: density feedback (DI) is indirect - affects confinement, can destabilize; C-III filterscope measures only one charge state, misses O, other C ions
- Bolometer robustness: total radiation measurement independent of impurity species composition (C vs O vs seeded gases)
- Spatial information: multiple viewing chords reveal radiation distribution - core vs edge vs SOL, identify X-point hot spots
- Physical connection: radiation IS the detachment mechanism - controlling P_rad directly controls heat dissipation
- Gas injection optimization: moderate puff duration (50-200ms) optimal - short pulses cause transients, long pulses ineffective
- PID tuning challenges: parameters discharge-specific, depend on magnetic configuration, heating power, impurity species
- No universal scaling law found - complex parameter space requires adaptive control strategies
- System limitations: 150-400ms total latency (dominated by plasma response), limits achievable control bandwidth to ~2-5 Hz
- Future improvements: (1) reduce acquisition latency to <10ms, (2) implement predictive control using plasma models, (3) machine learning for automatic PID optimization
- Despite limitations, bolometer feedback is the most direct method for radiation control in reactor-relevant scenarios
- Validated approach: successfully demonstrated at W7-X, applicable to ITER, DEMO, and future stellarators

---

## LINE-OF-SIGHT SENSITIVITY

### LOS Sensitivity (Methodology)

- Systematic LOS sensitivity analysis to identify optimal channel configurations for feedback control
- Dataset: 45 discharge pairs from OP1.2b campaign spanning wide parameter range (P_ECRH=3.5-6.5 MW, f_rad=0.3-1.0, T_e=0.9-1.5 keV)
- Methodology: evaluate all possible channel combinations (C(32,m) for HBC, C(62,m) for VBC) for m=3,5,7 channels
- Six evaluation metrics applied: (1) correlation, (2) weighted deviation, (3) mean deviation, (4) Fourier transform correlation, (5) Fisher information, (6) χ² fitness
- Each metric quantifies how well P_pred from channel subset S predicts total P_rad

### LOS Sensitivity (Results)

- Key finding: channels viewing separatrix (ρ_pol~0.95-1.05) and SOL most effective - this is where detachment radiation concentrates
- VBC cameras outperform HBC for edge sensitivity: better viewing geometry toward X-points and island chains
- Global maximum in sensitivity profiles: VBC channel viewing upper inboard X-point (r_eff≈-0.13 r_a)
- HBC shows local maxima at ±0.4 r_a, ±0.7 r_a corresponding to island chain intersections
- Robustness: multiple channel combinations achieve ≥85% prediction accuracy - no single "best" set exists
- Optimal channel count: m=3-5 sufficient, m=7 provides marginal improvement (<5%) at cost of increased complexity
- Weighted deviation threshold: Δ_w<0.15 defines acceptable performance (accounts for measurement uncertainties and temporal variations)
- Correlation with plasma parameters: high P_ECRH (≥4.2 MW), high f_rad (>0.75), T_e~1.3 keV yield best prediction quality

---

## TOMOGRAPHY

### Minimum Fisher Regularization (Theory)

- Tomography problem: invert line-integrated measurements (Tx=b) to reconstruct 2D emissivity distribution x
- Ill-posed inverse problem: 61 measurements but ~4500 pixels (30 radial × 150 poloidal grid) - severely underdetermined
- Geometry matrix T: encodes etendue-weighted line integrals, condition number ~10⁶ indicates strong ill-posedness
- Regularization required: Minimum Fisher Regularization (MFR) with Tikhonov-type penalty minimizes ||Tx-b||² + λ⁻¹||Hx||²
- Fisher information I_F = ∫(1/x)(∂x/∂r)² dr measures gradient content - lower I_F = smoother solution
- Regularization matrix H ∝ (1/x)∇ᵀ∇ penalizes large gradients weighted by local emissivity
- Radially dependent anisotropy (RDA): different smoothness in radial vs poloidal directions, k_ani(r) varies with radius
- Core (k_ani≈2-10): favors smooth, flux-surface aligned emission; Edge (k_ani≈0.1-0.5): allows localized, anisotropic structures
- Iterative solution: converges in N_T=10-20 iterations, regularization parameter λ chosen by L-curve method
- Computational grid: 30×150 cells (radial×poloidal), domain extends to 1.3²V_P to handle boundary radiation

### Minimum Fisher Regularization (RDA)

- RDA implementation: k_ani(r) profile transitions smoothly from core to edge using tanh function
- Typical profiles: k_ani={2.0, 0.3} (core, edge) for standard cases, {5.0, 0.5} for highly anisotropic phantoms
- Physical motivation: core radiation follows flux surfaces (isotropic in flux coordinates), edge shows X-point localization (anisotropic)
- Advantages of MFR+RDA: (1) incorporates physics knowledge, (2) robust to noise, (3) stable convergence, (4) no negative emissivities
- Alternative: Relative Gradient Smoothing (RGS) can be combined with RDA for enhanced feature localization
- RGS weighting: H_RGS ∝ (∇x/x)² emphasizes relative gradients, stronger localization but may sacrifice global accuracy
- Comparison: RDA chosen as primary method - better balance between accuracy and robustness for W7-X geometry

### Benchmarking (Geometry)

- Geometry perturbation study: tested camera position variations (±2° tilts), detector/aperture segmentation (N=2,4,8), artificial symmetric geometries
- Segmentation convergence: N≥8 provides adequate resolution (etendue variations <10⁻¹¹ mm⁻³), N=8 chosen for computational efficiency
- Camera tilt sensitivity: ±2° rotations cause etendue changes ~10⁻¹¹ mm⁻³, forward model variations 0.5-1% in chord brightness
- Intrinsic asymmetry: HBC 68.75° tilt causes 0.5-1% left-right asymmetry in forward calculations even with symmetric radiation
- Artificial symmetric HBC: mirroring half the array reduces asymmetry, validates that as-designed geometry is near-optimal
- Worst-case scenario: ±2° misalignment could shift reconstructed features by ~0.2 r_a, emphasizes need for accurate as-built measurements
- Etendue validation: numerical integration agrees with analytical solutions for simple geometries (parallel plates, point sources)
- Conclusion: discretization computationally stable, geometry uncertainties non-negligible but manageable with careful calibration

### Phantom Reconstructions

- Phantom benchmark suite: 12+ synthetic radiation distributions testing algorithm performance across parameter space
- Test cases include: (1) simple rings at various radii, (2) Gaussian features, (3) anisotropic island-like structures, (4) nested concentric profiles, (5) asymmetric distributions
- Noise robustness: tested with up to 10% Gaussian noise on measurements, algorithm maintains ρ_c>0.85 and χ²<2
- Parameter variations: systematic scans of k_ani (0.1-20), radial position (0.3-1.3 r_a), intensity (0.1-2 MW/m³), width (σ_r, σ_θ)
- Quality metrics: (1) correlation ρ_c (phantom vs tomogram), (2) χ² fitness (forward vs measured), (3) MSD (mean squared deviation), (4) integrated powers P_rad,2D
- Key findings: P_rad underestimates P_2D by ~P_2D^(SOL) (standard extrapolation misses SOL contribution), χ² and ρ_c not always congruent
- Optimal parameters identified: k_ani={2.0, 0.3} for standard cases, {5.0, 0.5} for highly anisotropic, N_T=15 iterations, grid 30×150
- Reconstruction quality: >90% for well-constrained phantoms (good camera coverage), 70-85% for challenging cases (localized features, poor viewing angles)
- Recommended settings validated through 59 phantom tests with comprehensive parameter variations

### Experimental Reconstructions

- Experimental reconstructions: applied MFR+RDA to 4 feedback-controlled discharges from OP1.2b (XP20180809.13, XP20181010.32, XP20181011.12, XP20181018.45)
- Temporal evolution: reconstructions show radiation moving from core to edge as f_rad increases, validates detachment progression
- Spatial features resolved: X-point localization (factor 2-3× local enhancement), island chain structure, MARFE-like asymmetries
- XP20180809.13 example: laser blow-off events clearly visible as transient core radiation spikes, demonstrates temporal resolution
- Power balance application: P_2D^(core) + P_2D^(SOL) provides alternative to standard P_rad extrapolation
- Agreement: P_2D^(total) within 10-20% of P_rad, discrepancy attributed to geometry uncertainties and SOL extrapolation errors
- Key finding: standard extrapolation systematically underestimates total power by missing SOL contribution (~15-25%)
- Core radiation P_2D^(core) more stable metric for quasi-steady-state analysis - less sensitive to edge fluctuations
- Statistical analysis (4 discharges, 50+ time slices): P_rad ∝ P_2D^(X) correlation strong (R²>0.85), validates reconstruction accuracy
- Quality metrics: χ²=1.2-2.5 (acceptable), ρ_c=0.75-0.90 (good correlation), MSD<0.3 (low deviation)
- Discrepancy between χ² and ρ_c: optimal tomogram may not have χ²=1 due to systematic errors (geometry, calibration)
- Anisotropy optimization remains challenging: high-dimensional parameter space (k_core, k_edge, transition width), profile-dependent
- Computational performance: ~2-5 seconds per frame on standard CPU, suitable for post-shot analysis but not real-time
- Future prospects: GPU acceleration could reduce to <100ms per frame, enabling real-time tomography for advanced feedback

---

## CONCLUSIONS

### Key Achievements

- Three major achievements form integrated diagnostic and control system for W7-X radiation management
- (1) Real-time feedback system: first bolometer-based radiation control at W7-X, achieved f_rad≥85% with factor ≥2 heat load reduction
- (2) LOS optimization: systematic analysis of 45 discharge pairs, identified robust channel configurations (m=3-5 sufficient)
- (3) Tomography: validated MFR+RDA algorithm through 59 phantom tests and 4 experimental reconstructions
- Integration: feedback uses optimized channels, tomography provides detailed 2D validation of radiation distribution
- Reactor relevance: demonstrated stable high-radiation scenarios essential for ITER, DEMO divertor protection

**Comprehensive Summary:**
- Feedback system specifications: minimum acquisition latency 13.6ms, total loop 150-400ms (plasma-limited), PID control with dual prediction proxies
- Benchmark discharge XP20181010.32: 9.2s duration, P_ECRH=6.23 MW, f_rad≥85% sustained, heat load reduction factor ≥2, no disruption
- Diagnostic characterization: 94 channels installed (61 functional OP1.2b), calibration stability <5% over 1182 experiments, SNR>1000
- LOS sensitivity results: separatrix/SOL viewing channels optimal, VBC outperforms HBC for edge, multiple viable configurations identified
- Detachment physics insights: C²⁺ signature at f_rad~50%, full detachment f_rad>90%, radiation shifts inward to ρ_pol≈0.95
- STRAHL modeling: carbon dominates by 10²× over oxygen, C³⁺/C²⁺ critical near LCFS, validates feedback channel selection
- Tomography performance: reconstruction quality ρ_c>0.85, χ²<2.5, P_2D within 10-20% of P_rad, resolves X-point structures
- Power balance improvement: P_2D^(core) provides stable metric, reveals 15-25% SOL underestimation in standard extrapolation
- All methods extensively validated through OP1.2b campaign (2018): 1182 experiments, 45 feedback discharges analyzed

---

## OUTLOOK

### Future and Possibilities

- System upgrades roadmap: (1) hardware - reduce latency to <10ms through faster DAQ, (2) software - implement predictive control algorithms
- Machine learning applications: (1) automatic PID optimization for different scenarios, (2) optimal channel selection, (3) predictive gas injection timing
- Advanced modeling: integrate STRAHL with EMC3-EIRENE for 3D impurity transport, validate against OP2.1 high-performance scenarios
- Improved chamber models: refine two/three-chamber parameters with OP2.1 data, develop predictive scaling laws for gas injection
- Tomography extensions: (1) expand phantom benchmark suite to >50 cases, (2) GPU acceleration for real-time capability (<100ms/frame)
- Real-time tomography vision: 2D radiation distribution feedback would enable spatial control (target specific regions), detect MARFEs early
- Automated parameter optimization: Bayesian methods or grid search to find optimal k_ani profiles for different radiation scenarios
- ITER/DEMO relevance: methods directly transferable, DEMO requirements (P_fus~500 MW, f_rad≥95%, q_div<10 MW/m²) demand reliable radiation control
- Stellarator applicability: techniques applicable to other stellarators (LHD, future devices), tokamaks (ITER, DEMO, SPARC)
- Long-term vision: fully automated radiation control system with adaptive learning, spatial distribution optimization, predictive capabilities

---

## CLOSING

### Thank You

- Thank you for your attention - "Sin é, a chairde" (That's it, friends) - Irish Gaelic closing
- Open for questions on any aspect: feedback system implementation, LOS optimization methodology, tomography algorithm details, experimental results interpretation
- Key discussion points prepared: (1) latency reduction strategies, (2) comparison with alternative feedback methods, (3) tomography parameter optimization, (4) ITER/DEMO applicability
- Acknowledge W7-X team, IPP collaborators, EUROfusion support, Helmholtz Association, University of Greifswald

---

## BACKUP SLIDES - Overview

- Backup slides provide detailed technical information for in-depth questions
- Topics covered: plasma physics, STRAHL modeling, diagnostic details, LOS sensitivity metrics, tomography comparisons, DAQ latency
- Available to address specific questions on methodology, implementation details, or alternative approaches

---

*End of Main Presentation Guide*

---

# DETAILED BACKUP SLIDES TALKING POINTS

## PLASMA PHYSICS

### Plasma Transport at W7-X
- Three transport mechanisms: classical, neoclassical, anomalous
- W7-X optimization for low collisionality regime
- Anomalous transport dominates by order of magnitude
- Impurity transport charge-dependent

### Impurity Transport and Radiation
- Anomalous diffusion D_an~0.3-3 m²/s dominates
- Neoclassical convection creates inward pinch for high-Z
- DEMO target: f_rad>0.95 with 70/30 core/SOL split
- Control challenge: balance protection vs confinement

### Plasma Impurities
- Carbon dominant: 10²× higher than oxygen
- Ionization stages vary with temperature
- Radiation distribution evolves with f_rad
- Core/SOL turnover at high f_rad

### Impurity Effects and Transport Sensitivity
- Fuel dilution affects Lawson criterion
- Diffusion sensitivity: 120% peak increase with lower D
- Separatrix profile critical for detachment
- STRAHL validates experimental trends

### Plasma Detachment
- Threshold: T_e < 5 eV at target
- Volumetric losses dominate
- Radiation enhancement feedback loop
- W7-X achieved f_rad=100% detachment

## MODELING & ANALYSIS

### Impurity Seeding Models
- Two-chamber and three-chamber models
- Capture basic timescales: wall, plasma, SOL
- R²>0.85 correlation with experiments
- Future: integrate with 3D codes

### Plasma Power Balance
- Energy conservation: P_bal ≈ 0
- Combined uncertainties ±1-2 MW
- Vessel heat load 15-25% of P_rad
- Tomography improves stability

## DIAGNOSTIC DETAILS

### Detector Sensitivity: Etendue
- K̃_M quantifies light collection efficiency
- Units: mm⁻³ (inverse volume)
- Spatial resolution ~4-5 cm at axis
- Critical for absolute power measurements

### Temperature Drift Impact
- Major systematic error in long pulses
- Grey body radiation scales with T⁴
- Linear correction for slow drifts
- Future: temperature-dependent calibration

### In-Situ Calibration
- Essential due to ±5-10% variations
- Three parameters: R_M, τ_M, κ_M
- OP1.2b: exceptional stability over 1182 experiments
- Cable correction prevents systematic errors

### Detector Performance Statistics
- SNR>1000 in high radiation
- Noise: 0.339±12.586 μV
- Minimal degradation observed
- Meets all fusion-grade requirements

### Bolometer Equation Derivation
- AC excitation removes 1/f noise
- Wheatstone bridge: ΔU ∝ ΔR_M
- Power balance: heating vs cooling
- Trade-off: τ and κ inversely related

### Measurement Algorithm
- Three stages: initialization, calibration, measurement
- Real-time feedback via NI 6321 DAQ
- FIFO buffer prevents data loss
- Latency optimization: 13.6ms minimum

## STRAHL MODELING

### STRAHL Basics
- 1D impurity transport code
- Flux-surface averaged quantities
- Time-dependent evolution
- Solves continuity for each Z

### STRAHL Impurity Transport Modeling
- Governing equation with D and v
- Carbon dominance validated
- Critical charge states: C³⁺/C²⁺
- Radiation shift with f_rad

### STRAHL Parameter Variations
- Systematic sensitivity study
- Core radiation stable ±10%
- Edge varies ±30-50%
- C³⁺/C²⁺ most sensitive

### STRAHL: Radiation Fraction Dependence
- f_rad=90% vs 100% comparison
- Peak shifts from SOL to LCFS
- Core/SOL ratio changes 0.3→0.7
- Validates feedback channel selection

## LOS SENSITIVITY DETAILS

### Camera Geometry Sensitivity
- Aperture positioning uncertainties
- Forward modeling <1% difference
- Manufacturing tolerances acceptable
- Validates engineering design

### Segmentation and Line-of-Sight Cones
- N=8 optimal for accuracy vs computation
- Full cone vs infinitesimal projection
- Proper segmentation essential
- Each segment weighted by etendue

### Tomography: RDA vs RGS Comparison
- RDA: absolute differences, preserves gradients
- RGS: relative gradients, enhances features
- RDA chosen for robustness
- RGS useful for post-shot analysis

### Tomography: Artificial Cameras
- VBCm and MIRh conceptual designs
- 4-camera improves by 15-20%
- Trade-off: cost vs improvement
- Current 3-camera sufficient

### Phantom Tomography: Edge Cases
- Inverted anisotropy tests limits
- Homogeneous distribution validates no artifacts
- Edge cases reveal limitations
- Guide operational parameters

### LOS Sensitivity Evaluation (Cross-correlation)
- Temporal similarity metric
- Large error bars: ±40%
- X-point channels poorest
- Critical for real-time control

### LOS Sensitivity Evaluation (Mean Deviation)
- Variance-based quality
- Error bars 10× larger than weighted
- Core channels consistent
- Edge optimal for feedback

### LOS Sensitivity Evaluation (FFT Correlation)
- Spectral analysis approach
- Identifies oscillatory behavior
- Complements time-domain
- Guides controller design

### LOS Sensitivity: Plasma Parameters
- P_ECRH correlation: higher better
- Optimal f_rad: 0.4-0.75
- T_e~1.3 keV ideal
- Validates high f_rad scenarios

### DAQ Latency
- Laser-based characterization
- Sample times: 0.8-3.2ms tested
- Minimum: 13.6ms achieved
- Total loop: 150-400ms sufficient

---

**Document prepared for PhD defense presentation**
**Total sections: 60+ frames with comprehensive talking points**
**Use this guide to maintain consistent messaging and technical accuracy throughout presentation**