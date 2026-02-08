# Mobility Datasets

This folder contains **mobility test datasets** and analysis scripts from 5G testbed experiments. All tests focus on User Equipment (UE) mobility behavior during different scenarios:

- **Actual Mobility Tests**: Real-world UE movements between gNodeBs
- **iPerf Downlink Tests**: Controlled throughput measurement while UE is mobile (two test rounds)

## Folder Structure

```
mobility/
├── dataset.json                          # Main aggregated dataset (all mobility tests combined)
├── test_actual_mobility_1/               # Mobility Test 1: Real UE movement scenarios
│   ├── dataset_ACTUAL_MOBILITY_1.json
│   ├── dataset_ACTUAL_MOBILITY_1_GNB_202.json
│   └── dataset_ACTUAL_MOBILITY_1_GNB_203.json
├── test_iperf_dl_test_1/                 # Mobility Test 2: Throughput measurement during mobility (Round 1)
│   ├── dataset_IPERF_DL_TEST_1_GNB_202.json
│   └── dataset_IPERF_DL_TEST_1_GNB_203.json
├── test_iperf_dl_test_2/                 # Mobility Test 3: Throughput measurement during mobility (Round 2)
│   ├── dataset_IPERF_DL_TEST_2_GNB_202.json
│   └── dataset_IPERF_DL_TEST_2_GNB_203.json
├── scripts/                              # Data processing and analysis utilities
│   ├── main.py
│   ├── main_poc.py
│   ├── main_two_datasets.py
│   ├── main_two_datasets_iperf_test.py
│   ├── get_timestamps.py
│   └── sanity.py
└── README.md
```

## Mobility Tests Overview

All tests in this dataset measure User Equipment (UE) mobility performance as devices move between 5G gNodeBs (base stations). The three test categories explore different aspects of mobility behavior:

### Test 1: Actual Mobility (test_actual_mobility_1/)
**Scenario**: Real-world natural UE movement between base stations

Real-world User Equipment (UE) mobility where devices organically move and trigger handovers between gNodeBs.

| File | Description |
|------|-------------|
| `dataset_ACTUAL_MOBILITY_1.json` | Complete test data (all gNodeBs) |
| `dataset_ACTUAL_MOBILITY_1_GNB_202.json` | Data filtered for gNodeB 202 |
| `dataset_ACTUAL_MOBILITY_1_GNB_203.json` | Data filtered for gNodeB 203 |

**Characteristics**:
- Natural movement patterns and handover triggers
- Real signal strength variations and path loss
- Organic traffic conditions during mobility

**Use Cases**:
- Handover detection and performance analysis
- Real-world signal strength characterization
- Path loss modeling during movement
- Natural mobility behavior insights

### Test 2: iPerf Downlink Test 1 (test_iperf_dl_test_1/)
**Scenario**: UE mobility with controlled maximum downlink throughput testing (Round 1)

Controlled throughput measurement using iPerf traffic generator as UE moves between base stations. First round validates baseline performance.

| File | Description |
|------|-------------|
| `dataset_IPERF_DL_TEST_1_GNB_202.json` | gNodeB 202 results |
| `dataset_IPERF_DL_TEST_1_GNB_203.json` | gNodeB 203 results |

**Characteristics**:
- Maximum downlink load via iPerf
- Precise throughput measurement during mobility
- Consistent traffic pattern for fair comparison
- UE moving between cells under sustained load

**Use Cases**:
- Throughput capacity during handovers
- Network resilience under loaded mobility
- Base station performance comparison
- Handover impact on active data transfer

### Test 3: iPerf Downlink Test 2 (test_iperf_dl_test_2/)
**Scenario**: UE mobility with controlled maximum downlink throughput testing (Round 2)

Second round of iPerf testing during mobility for validation and consistency verification.

| File | Description |
|------|-------------|
| `dataset_IPERF_DL_TEST_2_GNB_202.json` | gNodeB 202 results |
| `dataset_IPERF_DL_TEST_2_GNB_203.json` | gNodeB 203 results |

**Characteristics**:
- Repeat of Test 2 for consistency verification
- Identifies test-to-test variability
- Same conditions as Test 1 for reproducibility
- UE moving between cells under load

**Use Cases**:
- Test reproducibility and reliability
- Seasonal/temporal variation detection
- Network stability assessment
- Confidence in capacity planning decisions

### Main Dataset
- **dataset.json**: Aggregated dataset combining data from all three mobility tests. Use for comprehensive cross-scenario analysis.

| File | Description |
|------|-------------|
| `dataset_IPERF_DL_TEST_1_GNB_202.json` | iPerf DL test 1 on gNodeB 202 |
| `dataset_IPERF_DL_TEST_1_GNB_203.json` | iPerf DL test 1 on gNodeB 203 |
| `dataset_IPERF_DL_TEST_2_GNB_202.json` | iPerf DL test 2 on gNodeB 202 |
| `dataset_IPERF_DL_TEST_2_GNB_203.json` | iPerf DL test 2 on gNodeB 203 |

**Use Cases**:
- Benchmark maximum downlink throughput per gNodeB
- Identify network bottlenecks under high load
- Compare performance consistency across tests
- Verify gNodeB capacity and resource allocation

## Scripts

### Primary Analysis Scripts

**`main.py`**
- Main data processing and analysis script
- Loads and processes raw mobility datasets
- Generates summary statistics and insights
- Output: Processed metrics for visualization and further analysis

**`main_two_datasets.py`**
- Comparative analysis script for two mobility datasets
- Useful for comparing different test runs or scenarios
- Performs cross-dataset validation and correlation analysis

**`main_two_datasets_iperf_test.py`**
- Comparative analysis script for iPerf test datasets
- Compares performance across different gNodeBs or test runs
- Identifies throughput variations and consistency

### Utility Scripts

**`main_poc.py`**
- Proof-of-concept script for data exploration
- Quick analysis and visualization examples
- Starting point for custom analysis

**`get_timestamps.py`**
- Extracts and processes timestamp information from datasets
- Synchronizes timing across different data sources
- Useful for temporal alignment and correlation

**`sanity.py`**
- Data validation and quality checking script
- Verifies dataset integrity and completeness
- Identifies missing or anomalous values
- Essential to run before processing datasets

## Data Format

All JSON files follow a consistent structure containing measurement timeseries:

```json
{
    "timestamps": [timestamp1, timestamp2, ...],
    "measurements": {
        "metric_name": [value1, value2, ...],
        "another_metric": [value1, value2, ...],
        ...
    },
    "metadata": {
        "gnb_id": "202 or 203",
        "test_type": "ACTUAL_MOBILITY_1 or IPERF_DL_TEST_1/2",
        "duration": duration_in_seconds,
        "sampling_interval": sampling_interval_in_seconds
    }
}
```

### Common Metrics

| Metric | Description |
|--------|-------------|
| `dl_bitrate` | Downlink bitrate (bps) |
| `ul_bitrate` | Uplink bitrate (bps) |
| `rsrp` | Reference Signal Received Power (dBm) |
| `rsrq` | Reference Signal Received Quality (dB) |
| `sinr` | Signal-to-Interference-plus-Noise Ratio (dB) |
| `latency` | Round-trip latency (ms) |
| `packet_loss` | Packet loss ratio (%) |
| `ue_position` | UE coordinates (x, y, z) for mobility tests |

## Recommended Usage

### For Handover Analysis
```
Start with: actual_mobility_tests/dataset_ACTUAL_MOBILITY_1.json
Process with: main.py or main_two_datasets.py
Analyze: Signal strength variations, latency spikes, throughput drops
```

### For Capacity Planning
```
Start with: iperf_tests/dataset_IPERF_DL_TEST_[1-2]_GNB_[202-203].json
Process with: main_two_datasets_iperf_test.py
Analyze: Maximum throughput, load distribution, gNodeB utilization
```

### For Data Quality Assurance
```
Always run: sanity.py first
Check: Data completeness, timestamp continuity, value ranges
```

## Quick Start

1. **Validate data integrity**:
   ```bash
   python scripts/sanity.py
   ```

2. **Process and analyze**:
   ```bash
   python scripts/main.py                              # Single dataset analysis
   python scripts/main_two_datasets.py                 # Compare two datasets
   python scripts/main_two_datasets_iperf_test.py     # Compare iPerf tests
   ```

3. **Extract specific information**:
   ```bash
   python scripts/get_timestamps.py dataset.json
   ```

## File Sizes and Metadata

- **Actual Mobility Tests**: Complete movement trajectories and signal measurements
- **iPerf Tests**: High-frequency throughput and latency measurements
- **GNB-specific files**: Filtered subsets for individual base station analysis

Aggregate dataset sizes vary based on sampling frequency and test duration. Refer to metadata within JSON files for specific details.
