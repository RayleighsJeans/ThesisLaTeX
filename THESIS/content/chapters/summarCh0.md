# Chapter 0: Introduction - Summary

## Overview
Introduction chapter establishing the motivation for fusion research, describing the W7-X stellarator, and providing foundational plasma physics concepts relevant to the thesis work on radiation diagnostics and impurity transport.

## Structure and Content

### 1. Nuclear Fusion (Section, lines 8-21)
**Key Concepts:**
- DT fusion reaction: D + T → He⁴(3.5 MeV) + n(14.1 MeV) [Eq. 1]
- Superiority of DT fusion at achievable plasma temperatures (~20 keV)
- Deuterium abundant in water, Tritium bred from Lithium blanket
- Minimal radioactive waste compared to fission

**Thesis Focus:**
- Properties of radiation in W7-X stellarator
- Intrinsic and extrinsic impurities
- Transport effects on plasma performance
- Multicamera metal resistor bolometer diagnostic

### 2. Wendelstein 7-X (Section, lines 22-42)
**Machine Specifications:**
- Major radius: 5.5 m, Minor radius: 0.53 m
- Volume: 30 m³
- Maximum B-field: 3 T
- Heating power: 14 MW
- Target: 30 min discharge at 10 MW (continuous operation)

**Design Features:**
- 5-fold modular symmetry
- 70 superconducting magnets (50 non-planar + 20 planar coils)
- Optimized for: small magnetic islands, MHD stability, reduced neoclassical transport, minimized bootstrap current
- Island divertor concept (not toroidally symmetric)
- Operates at ι = 5/6, 5/5 (standard), 5/4 resonances

**Divertor Configuration:**
- Cross-section varies: triangular ↔ bean-shaped
- Natural magnetic islands at edge (ι ≈ 1)
- One divertor pair per field period at bean-shaped cross-sections
- Heat flux up to 10 MW/m²
- Inertially cooled (no water cooling in discussed experiments)

**Figure References:**
- Fig. 0.1: W7-X cutaway showing coils, plasma, cryostat
- Fig. 0.2: LCFS flux tube and cross-sections at triangle/bean planes (bolometer at 108° toroidally)

### 3. Plasma Physics (Section, lines 44-102)

#### 3.1 Lawson Criterion (lines 46-52)
**Triple Product:** n_e T τ_E ≥ [complex expression with f_tot, σ_DT, f_H, E_α, L_Z] [Eq. 2]
- Energy confinement time τ_E measures energy loss rate
- Impurities affect through dilution (f_H, f_tot) and radiation (L_Z)
- Magnetic confinement via Lorentz force → gyro-motion along field lines

#### 3.2 Power Balance (lines 52-54)
**Steady-state:** P_α + P_h = P_n + P_rad^core + P_SOL
- P_rad^core = P_brems + P_line
- High-Z impurity seeding increases core radiation → reduces P_SOL
- DEMO target: f_rad = P_rad/P_αH > 0.95 (70% from core, rest from SOL)

**Challenges:**
- Impurity dilution increases with higher Z
- Core accumulation due to transport
- Risk of radiative collapse at oversaturation
- Divertor radiation benefits: reduced sputtering, broadened heat flux, density increase near target

#### 3.3 Transport (Subsection, lines 55-102)

**Classical Transport (lines 59-61):**
- Coulomb collisions → diffusive/convective transport
- Particle displacement ~ Larmor radius r_L
- Diffusion D scales as 1/B²
- Fastest equilibration on flux surfaces

**Neoclassical Transport (lines 63-91):**
- Fokker-Planck equation with collisionality operator [Eq. 3]
- Accounts for: ∇B drifts, curvature drifts, trapped particles, banana orbits
- Radial flux: Γ_q = -D_neo ∇n_q + v_neo n_q
- Convection ∝ charge q, includes temperature screening (H_x parameter)

**Transport Regimes (Fig. 0.3):**
1. **Banana regime** (low ν): Trapped particles, D_⊥ dominant, W7-X optimized to reduce this
2. **Electron-root** (low ν, T_e >> T_i): Reduced transport ∝ √ν, radial E-field for ambipolarity
3. **Ion-root** (higher ν): Reversed E-field, ∝ 1/ν
4. **Pfirsch-Schlüter** (high ν): D_PS ∝ D_classical, geometry irrelevant

**Stellarator vs Tokamak:**
- Stellarators: 1-2 orders of magnitude higher neoclassical transport (broken symmetry)
- W7-X optimized to reduce this in low collisionality scenarios

**Anomalous Transport (lines 92-101):**
- Exceeds neoclassical by order of magnitude
- Caused by turbulence from micro-instabilities (ITG, ETG)
- Scales with heating power and machine size (contradicts neo/classical)
- Spatial/temporal scales: < cm, < ms
- Usually D_neo << D_an, so neoclassical diffusion negligible
- Exception: high-Z impurities where charge-dependent neoclassical convection matters

**Integrated Impurity Flux:**
Γ_q = -(D_neo,q + D_an,q)∇n_q + (v_neo,q + v_an,q)n_q = -D_q ∇n_q + v_q n_q

### 4. Plasma Radiation (Subsection, lines 103-144)

#### 4.1 Bremsstrahlung (lines 114-126)
**Power Loss:** P_brems = c_b n_e √T_e Σ_i n_i <Z̄_i>² = c_b n_e² √T_e Z_eff [Eq. 4]
- c_b = 5×10⁻⁴³ MW·m³/√keV
- Z_eff = 1 for pure DT plasma
- Z_eff ≠ 1 with impurities

**Quantum Expression:** p_brems(v,ν) with Kramers-Gaunt factor g_ff [Eq. 5]

**Other Radiation:**
- Synchrotron (magnetobremsstrahlung): Negligible at current W7-X operations
- Line radiation: Important at edge/SOL for hydrogenic plasma
- Recombination radiation: Edge/SOL contribution

#### 4.2 Radiation Effects (lines 127-128)
**Beneficial (moderate edge/SOL):**
- Reduces heat flux to wall/target
- Improves heat load control
- No core performance degradation

**Detrimental (strong core):**
- Flattened T and p profiles
- Weakened turbulence suppression
- Lower stored energy
- f_rad > 90%: Risk of radiative collapse

#### 4.3 Impurity Radiation (lines 129-144)
**Total Radiation:** P_rad = Σ_Z n_e n_Z L_Z
- L_Z: Cooling rate (power lost per unit volume)
- High-Z: Radiate in hot core (Fig. 0.4 shows T_e dependence)
- Low-Z: Radiate at edge

**Processes:**
1. Line radiation: Electron impact excitation → spontaneous photon emission
2. Bremsstrahlung: Increases with ionization level (high-Z, large cross-sections)

**Example - Carbon:**
- Low charge states: E_exc ~ 5-10 eV → radiate in SOL/edge
- High charge states: E_exc, E_ion ≳ 300 eV → radiate in core

**Corona Approximation (core):**
- Ionization/recombination dominate charge state balance
- k^ion_{Z-1} n_{Z-1} + k^rec_{Z+1} n_{Z+1} = (k^ion_Z + k^rec_Z) n_Z
- Rate coefficients k^ion, k^rec = f(T_e)

**Edge Transport Effects:**
- Low-Z ions diffuse to hot regions before ionizing (strong anomalous transport)
- Transport increases cooling rates, less T_e sensitive than corona
- Localized sources (beams, valves): 3D time-dependent transport, nested shells of charge states

### 5. Impurities (Subsection, lines 145-164)

#### 5.1 Intrinsic Impurities (lines 149-152)
**Helium:**
- Must be removed (fuel dilution)
- Long confinement time (> τ_E)
- Fast He nuclei needed for core heating until thermalization
- Thermal He from: gas valves, wall implantation during glow discharges

**Wall Material (O, C, heavy elements):**
- Eroded by impinging ions
- Accelerated in plasma sheath E-field
- Erosion depends on T_e, T_i
- Large heat fluxes → sublimation, arcing, dust production
- Macroscopic particles → large ionization cascades → increased P_rad

#### 5.2 Extrinsic Impurities (lines 154-157)
**Purpose:** Control localized heat fluxes at edge via radiative cooling
- Low-Z: He, Ne, N₂
- High-Z: S, Ar
- Essential for reactor-grade devices (95% fusion power must be exhausted in edge/SOL)

**Example - ASDEX Upgrade:**
- Nitrogen seeding: 1-3% core concentration achieves radiative cooling

#### 5.3 Detachment (lines 161-164)
**Definition:** Edge plasma where:
- Large heat fraction dissipated by radiation (usually low-Z)
- Particle flux to target significantly reduced

**W7-X Island Divertor Performance:**
- Intrinsic carbon removes most edge power
- Radiation layer outside confinement region
- Negligible core energy loss
- Integrated/maximum heat loads reduced by factor 10
- Particle flux reduced by factor 4 at f_rad ≥ 50%
- No strong volume recombination observed

**Critical Thresholds:**
- f_rad ~ 80%: Divertor neutral pressure increases beyond recycling flux
- f_rad ≳ 80%: ~10% loss of stored energy, n_e increases, T_e decreases at core-edge

**Historical Context:**
- Stable controlled detachment not achieved in previous Wendelstein machines
- Critical for W7-X: heat load reduction and reactor longevity

**MARFE (Multi-Faceted Radiation From Edge):**
- Toroidal strings of high density, high radiation plasma
- Occur during detachment near divertors and X-points
- Can be avoided with He/Ne seeding (f_rad = 95% in edge/SOL without MARFEs)

## Key Equations
1. DT Fusion: D + T → He⁴(3.5 MeV) + n(14.1 MeV)
2. Lawson Criterion: n_e T τ_E ≥ [function of f_tot, σ_DT, f_H, E_α, L_Z]
3. Fokker-Planck: ∂f_x/∂t + v·∇f_x + (Z_x e/m_x)(E + v×B)·∇_v f_x = collision terms + S_x
4. Bremsstrahlung: P_brems = c_b n_e² √T_e Z_eff
5. Quantum Bremsstrahlung: p_brems(v,ν) with Kramers-Gaunt factor

## Figures
- Fig. 0.1: W7-X cutaway rendering
- Fig. 0.2: LCFS flux tube and cross-sections (bolometer at 108°)
- Fig. 0.3: Neoclassical transport regimes vs collisionality
- Fig. 0.4: Radiation power vs T_e for different impurities

## Custom LaTeX Commands Used
- `\ix{text}`: Text subscripts (n\ix{e} → n_e)
- `\tenpo{n}`: Powers of 10
- `\diff`: Upright differential d
- `\SIrange{min}{max}{unit}`: Range with units
- `\cref{label}`: Cross-references

## References to Other Chapters
- Thesis focuses on bolometer diagnostic (multicamera metal resistor)
- Radiation properties, impurity transport, plasma performance at W7-X
- Next sections introduce core concepts for investigations

## Scientific Context
This introduction establishes the foundation for understanding:
1. Why radiation control is critical for fusion reactors
2. How W7-X's unique stellarator design addresses transport challenges
3. The role of impurities in both beneficial (edge cooling) and detrimental (core accumulation) scenarios
4. The importance of detachment for reactor-relevant operation
5. The need for precise radiation diagnostics (bolometry) to study these phenomena