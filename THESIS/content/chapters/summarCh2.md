# Chapter 2: Plasma Radiation Feedback Control - Summary

## Overview
Chapter 2 (572 lines) presents the development, implementation, and experimental validation of a real-time radiation feedback control system for achieving stable plasma detachment at Wendelstein 7-X. The chapter describes the motivation for radiative power exhaust, the technical implementation of the feedback system, benchmark testing, and experimental results from the OP1.2b campaign.

## Structure

### 2.1 Introduction and Motivation (lines 1-100)
- **Detachment Physics**: Need for power exhaust management in fusion reactors
- **Impurity Seeding**: Low-Z to medium-Z impurities for radiative cooling
- **W7-X Configuration**: OP1.2b with boronization, island divertor
- **Diagnostic Systems**: Thermal helium beam, dispersion interferometry, filterscopes, ECE

### 2.2 Real-Time Radiation Feedback System (lines 100-200)
- **Hardware**: NI 6321 DAQ system
- **Software**: LabVIEW algorithm for real-time processing
- **Latency Benchmark**: 13.6 ms minimum system latency
- **PID Controller**: Proportional-integral-derivative control setup
- **Gas Valves**: Thermal gas injection system (AEH31, AEH51 ports)

### 2.3 Acquisition Timing Benchmarks (lines 200-293)
- **Laser Test Setup**: Diode laser at 7 mW, 1 Hz square wave
- **Sample Time Analysis**: Testing Δt = 0.8, 1.0, 1.6, 3.2 ms
- **Without Feedback**: 6.25% timing error for Δt < 1.6 ms
- **With Feedback**: Linear increase in sample time (0.01 ms/s) for Δt < 1.6 ms
- **PC Load Test**: No effect from 80% CPU load on acquisition timing
- **Conclusion**: Feedback not applicable for Δt < 1.6 ms

### 2.4 Experimental Achievements (lines 294-468)

#### 2.4.1 Initial Results - XP20180920.29 (lines 299-355)
- **Configuration**: 2 MW ECRH (X2-mode), 1.3 s duration (terminated early)
- **Channel Selection**: S = {0, 3, 7, 14, 16} from HBC
- **Setpoint**: f_rad = 90%
- **Result**: Radiative collapse - prediction underestimated P_rad
- **Issue**: P_pred^(1) did not adequately represent true P_rad
- **Consequence**: Overshoot to f_rad > 95%, density collapse, early termination
- **Lesson**: Need optimized channel selection for radiation profile

#### 2.4.2 Application Progress - XP20180920.31 (lines 356-397)
- **Configuration**: 2.9 MW ECRH (X2-mode), 10 s duration
- **Channel Selection**: Same as XP20180920.29
- **Improvement**: Variable K_p = f(e(t))
- **Result**: Achieved f_rad > 50% but with oscillations
- **Issue**: Prediction underestimated P_rad by ~10%
- **PID Components**: Dominated by K_p, conservative K_i
- **Conclusion**: Unable to maintain stable f_rad > 80%

#### 2.4.3 Successful Detachment - XP20181010.32 (lines 399-468)
- **Configuration**: 6.23 MW ECRH (O2-mode), 9.2 s, 55 MJ total
- **Channel Selection**: S = {65, 78, 61, 73, 86} - VBC only
- **Key Innovation**: VBC channels viewing magnetic islands and X-points
- **Achievement**: Stable detachment with f_rad > 90%
- **Target Heat Load**: Reduced by factor > 2
- **Plasma Performance**: No degradation of W_dia or core n_e
- **Radiation Distribution**: Inward shift, condensation at X-points
- **Emissivity**: Up to 400 kW/m³ in magnetic islands
- **Issue**: Oscillations due to feedback latency and K_x parameters
- **Validation**: Filterscope C-III measurements confirm detachment

### 2.5 Comparison to Other Feedback Methods (lines 469-563)

#### 2.5.1 Electron Density Feedback - XP20181016.16 (lines 474-524)
- **Configuration**: 5 MW ECRH (O2-mode), 21 s duration
- **Process Variable**: Line-integrated n_e from dispersion interferometer
- **Setpoint**: n_e ramp around 1.1×10²⁰ m⁻³
- **Result**: f_rad > 80%, P_div reduced by 50%
- **Advantage**: Lower latency, smoother control without oscillations
- **Disadvantage**: Requires prior exploration of n_e setpoint

#### 2.5.2 C-III Radiation Feedback - XP20180920.32 (lines 525-563)
- **Configuration**: 3 MW ECRH (X2-mode), 9.5 s duration
- **Process Variable**: C²⁺ line radiation from filterscopes (AEI30)
- **Goal**: Localize radiation above target, shift ionization front
- **Result**: f_rad ~ 70%, smoother control
- **Advantage**: Much lower latency, higher temporal resolution
- **Limitation**: Lower maximum f_rad compared to radiation feedback
- **Observation**: C²⁺ detachment from target at f_rad > 70%

### 2.6 Conclusions (lines 564-572)
- **System Validation**: Real-time radiation feedback achieves stable detachment
- **Latency**: 13.6 ms system + ~10Δt/2 FIFO smoothing + 200-400 ms plasma response
- **Optimal Sample Time**: Δt ≥ 1.6 ms required
- **Channel Selection**: VBC channels viewing islands/X-points most effective
- **PID Optimization**: K_x parameters need further tuning for steady-state
- **Comparison**: Higher latency than n_e or C-III feedback, but no prior calibration needed
- **Future Work**: Blind absorber setup to separate plasma and measurement latencies

## Key Equations

### Radiation Prediction Proxies
```
P_pred^(1) = Σ(i∈S) a_i ΔŨ_i     [Eq. prediction]
P_pred^(2) = a_7 ΔŨ_7             [Eq. prediction2]
```
Where S is subset of detector channels, a_i are calibration coefficients

### Expected Sample Count
```
N = 0.5 s / Δt ± 1
```

### Radiation Fraction
```
f_rad = P_rad / P_ECRH           [Eq. fraction]
```

## Figures Referenced

### Benchmark and System Performance
1. **fig:woRTF_0.8ms**: Laser test without feedback (Δt = 0.8 ms)
2. **fig:woRTF_1.6_3.2ms**: Laser test without feedback (Δt = 1.6, 3.2 ms)
3. **fig:wRTF_0.8ms**: Laser test with feedback (Δt = 0.8 ms)
4. **fig:wRTF_1.0_1.6ms**: Laser test with feedback (Δt = 1.0, 1.6 ms)
5. **fig:woRTF_load**: Laser test with 80% CPU load

### XP20180920.29 (Initial Failure)
6. **fig:20180920.29_channels**: Channel selection (HBC subset)
7. **fig:20180920.29_PDF**: Time traces (power, P_rad, PID, n_e, T_e, f_rad)
8. **fig:20180920.29_CP**: Chord brightness profiles (2D contours + snapshots)

### XP20180920.31 (Progress)
9. **fig:20180920.31_PDF**: Time traces
10. **fig:20180920.31_CP**: Chord brightness profiles

### XP20181010.32 (Successful Detachment)
11. **fig:20181010.32_channels**: Channel selection (VBC subset)
12. **fig:20181010.32_PDF**: Time traces including divertor heat loads
13. **fig:20181010.32_balance**: Power balance
14. **fig:20181010.32_CP**: Chord brightness profiles

### XP20181016.16 (Density Feedback)
15. **fig:20181016.16_PDF**: Time traces
16. **fig:20181016.16_balance**: Power balance
17. **fig:20181016.16_CP**: Chord brightness profiles

### XP20180920.32 (C-III Feedback)
18. **fig:20180920.32_PDF**: Time traces
19. **fig:20180920.32_cIII**: C²⁺ spatial-temporal evolution (comparison with XP20181010.32)

## Technical Specifications

### Real-Time System
- **Hardware**: National Instruments NI 6321 DAQ
- **Software**: LabVIEW algorithm with FIFO smoothing
- **Minimum Latency**: 13.6 ms (for Δt = 1.6 ms)
- **Sample Time Range**: 0.8 - 3.2 ms tested
- **Optimal Sample Time**: ≥ 1.6 ms
- **FIFO Array**: M = 10 samples for smoothing
- **Additional Latency**: ~M·Δt/2 from FIFO + 200-400 ms plasma response

### Gas Injection System
- **Type**: Thermal gas valves (fast acting)
- **Locations**: AEH31 (HM3), AEH51 (HM5)
- **Gas**: Hydrogen (working gas)
- **Pressure**: 50-750 mbar
- **Flow Rate**: ~6×10¹⁸ atoms/s

### PID Controller
- **Components**: K_p (proportional), K_i (integral), K_d (differential)
- **Innovations**: Variable K_p = f(e(t)) in XP20180920.31
- **Challenge**: Balancing responsiveness vs. oscillations
- **Optimization**: Ongoing for steady-state operation

### Diagnostic Systems Used
1. **Bolometry**: HBC and VBC cameras for P_rad
2. **Dispersion Interferometry**: Line-integrated n_e
3. **Thomson Scattering**: Local n_e and T_e profiles
4. **ECE**: Electron temperature
5. **Filterscopes**: C²⁺ line radiation (465.0 nm)
6. **Thermal Helium Beam**: Edge n_e and T_e
7. **Divertor Thermography**: Target heat loads P_div

## Scientific Context

### Detachment Physics
- **Goal**: Reduce target heat load by radiative cooling in SOL
- **Method**: Impurity seeding (hydrogen in these experiments)
- **Target**: f_rad > 80-90% for stable detachment
- **Mechanism**: Radiation condensation at X-points and magnetic islands
- **Indicators**: 
  - Reduced P_div (factor > 2)
  - Inward shift of radiation profile
  - Steepening of n_e and T_e profiles
  - C²⁺ detachment from target

### W7-X OP1.2b Configuration
- **Magnetic Configuration**: Standard field, ι = 5/5 island chain
- **Divertor**: Island divertor
- **Wall Conditioning**: Boronization (reduced O, C influx by factor 6)
- **Heating**: ECRH (X2-mode or O2-mode, 2-6 MW)
- **Working Gas**: Hydrogen
- **Toroidal Current**: 0.9-2 kA (counter-clockwise)

### Radiation Distribution
- **Low f_rad (<50%)**: Radiation inside LCFS, hollow profile
- **Medium f_rad (50-80%)**: Shift towards separatrix
- **High f_rad (>80%)**: Condensation at X-points and magnetic islands
- **Peak Emissivity**: Up to 400 kW/m³ in islands (XP20181010.32)
- **Asymmetry**: Strong up/down and in/out asymmetries
- **Connection**: Radiation follows magnetic field lines to gas valves

### Plasma Response
- **Latency**: 200-400 ms between gas injection and radiation response
- **Density**: Core n_e stable, edge n_e decreases at high f_rad
- **Temperature**: T_e inversely coupled to f_rad
- **Profile Changes**: Steepening at f_rad > 70%
- **Energy Confinement**: W_dia stable until f_rad > 80%

## LaTeX Patterns

### Custom Commands Used
- `\ix{text}`: Text subscripts (e.g., `P\ix{rad}`, `n\ix{e}`, `T\ix{e}`)
- `\diff`: Upright differential (e.g., `\diff P\ix{pred}^{\left(1\right)}/\diff t`)
- `\tenpo{n}`: Powers of 10 (not used in this chapter)
- `\SIrange{min}{max}{unit}`: Range with units
- `\SI{value}{unit}`: Single value with units
- `\cref{label}`: Cross-reference with automatic type
- `\autoref{label}`: Automatic reference type

### Figure Environments
- Extensive use of `subfigure` for multi-panel plots
- `\captionsetup{width=.45\textwidth}` for narrow captions
- `minipage` for side-by-side caption and figure
- Consistent structure: power/energy, P_rad, PID control, plasma parameters

### Mathematical Notation
- Superscripts for predictions: `P\ix{pred}^{\left(1\right)}`, `P\ix{pred}^{\left(2\right)}`
- Process value: `u\ix{PV}\left(t\right)`
- PID components: `K\ix{p}`, `K\ix{i}`, `K\ix{d}`
- Time-dependent functions: `y\left(t\right)`, `e\left(t\right)`
- Detector signals: `\Delta\widetilde{U}_{i}`, `\widetilde{U}\ix{M}`

### Citation Style
- `\cite{Author2020}` for references
- Multiple citations: `\cite{Feng2016,Feng2005,Thomsen2004}`

## Key Results Summary

### Successful Detachment (XP20181010.32)
- **Radiation Fraction**: f_rad > 90% maintained
- **Target Heat Load**: Reduced by factor > 2
- **Plasma Performance**: W_dia stable, core n_e stable
- **Radiation Profile**: Inward shift, X-point condensation
- **Peak Emissivity**: 400 kW/m³ in magnetic islands
- **Control Quality**: Oscillations present but manageable

### Comparison of Feedback Methods
| Method | Latency | f_rad | Control Quality | Calibration |
|--------|---------|-------|-----------------|-------------|
| P_rad | High (~400 ms) | >90% | Oscillations | None needed |
| n_e | Medium | >80% | Smooth | Requires exploration |
| C-III | Low | ~70% | Very smooth | None needed |

### Lessons Learned
1. **Channel Selection Critical**: VBC channels viewing islands/X-points most effective
2. **Latency Challenge**: Combined system + plasma latency ~400-500 ms
3. **Sample Time**: Must use Δt ≥ 1.6 ms for stable acquisition
4. **PID Tuning**: K_x optimization ongoing, differential component helpful
5. **Prediction Accuracy**: P_pred^(1) with VBC subset adequate for control
6. **Plasma Physics**: Radiation condensation at X-points confirmed at high f_rad

## Connections to Other Chapters
- **Chapter 1**: Bolometer diagnostic system used for P_rad measurements
- **Chapter 3**: Tomographic reconstruction of radiation profiles (referenced)
- **Chapter 0**: Plasma physics fundamentals (transport, radiation, detachment)
- **Appendix**: Likely contains additional experimental data or technical details

## Future Work Mentioned
- Optimize PID parameters (K_x) for steady-state operation
- Implement blind absorber setup to separate plasma and measurement latencies
- Explore differential component K_d more thoroughly
- Test feedback with varying heating power (not constant P_ECRH)
- Long-term steady-state experiments in future campaigns
- Explore parameter space of plasma response to gas injections