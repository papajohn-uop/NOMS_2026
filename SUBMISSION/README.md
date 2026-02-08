# AI-fuelled Adaptive Handovers and Energy-aware Mechanisms in 5G Cellular Networks

**NOMS 2026 Submission #17668**

## Overview

This repository contains the submission and supporting materials for a paper on AI-driven mobility management and energy efficiency in 5G networks.

## Authors

- Panagiotis Papaioannou (University of Patras)
- Ioannis Pastellas
- Sofia Karagiorgou
- Christos Tranoris (University of Patras)
- Spyridon Denazis (University of Patras)

## Abstract

5G networks introduce complex challenges in mobility management and energy consumption, including more frequent handovers as users move between cells, network congestion, service disruptions, increased power consumption due to higher path loss, and the need for beamforming. This work performs an experimental validation on optimal mobility management and energy consumption efficiency in 5G networks fuelled by Artificial Intelligence (AI) models. To achieve this, we conducted two real-world experiments in a 5G testbed, assessing the: (i) dynamics of handovers (HOs) between gNodeBs (gNBs) within a single operator network; and (ii) energy consumption characteristics of 5G base stations under various traffic conditions. To advance location-aware and energy-saving intelligence in 5G networks, we leverage adaptive AI-fuelled policy-enforcement mechanisms by harvesting traffic data from the 5G testbed and learning patterns for optimal energy consumption and mild handover events. The results of this work demonstrate promising insight for network optimization.

## Repository Structure

```
NOMS_2026/
├── SUBMISSION/                        # Paper submission package (this README)
│   ├── README.md
│   ├── NOMS 2026 - JEMS - Submission 17668.pdf
│   └── NOMS_reviews.rtf
├── datasets/                          # Processed and raw datasets from the testbed
│   ├── mobility/                      # Mobility experiments (all tests involve UE mobility)
│   │   ├── README.md
│   │   ├── raw_data/
│   │   ├── test_actual_mobility_1/
│   │   ├── test_iperf_dl_test_1/
│   │   └── test_iperf_dl_test_2/
│   └── power_metrics/                 # Energy/power metrics experiments
│       ├── README.md
│       ├── test1/
│       ├── test2/
│       └── test3/
└── binaries/                          # Binaries and auxiliary artifacts (if any)
```

## Folder Descriptions

### SUBMISSION/
Submission package and metadata:
- **README.md** - This overview
- **NOMS 2026 - JEMS - Submission 17668.pdf** - Main paper
- **NOMS_reviews.rtf** - Reviewer comments and feedback

### datasets/
Processed and raw datasets from the 5G testbed:
- **mobility/** - Mobility experiments (all tests involve UE mobility between gNodeB 202 and 203)
- **power_metrics/** - Energy/power measurements and processed variants

### binaries/
Auxiliary artifacts (binaries, tools, or models if present).

## Submission Details

- **Venue**: NOMS 2026
- **Submission ID**: 17668
- **Type**: Experimental Validation / Research Paper

## Key Contributions

- Experimental validation on real-world 5G testbed
- Assessment of handover dynamics between gNodeBs
- Energy consumption analysis under various traffic conditions
- AI-fuelled adaptive policy-enforcement mechanisms
- Traffic pattern learning for optimal energy consumption

## Repository Usage

This repository is organized to maintain all submission-related materials, reviews, and documentation in a structured manner.

---

*Last updated: February 2026*
