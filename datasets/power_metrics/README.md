# Power Metrics Data

This folder contains power metrics data collected from three experiments/tests of the 5G testbed. Each test has three versions of the data with different levels of processing.

The data were gathered through a Prometheus that is sued in the testbed to keep this information.

## Folder Structure

```
power_metrics/
├── test1/
│   ├── power_metrics_test1.json
│   ├── power_metrics_test1_MODIFIED.json
│   └── power_metrics_test1_MODIFIED_NO_UE_DETAILS.json
├── test2/
│   ├── power_metrics_test2.json
│   ├── power_metrics_test2_MODIFIED.json
│   └── power_metrics_test2_MODIFIED_NO_UE_DETAILS.json
├── test3/
│   ├── power_metrics_test3.json
│   ├── power_metrics_test3_MODIFIED.json
│   └── power_metrics_test3_MODIFIED_NO_UE_DETAILS.json
└── README.md
```

## File Versions and Differences

### 1. **Original Version** (`power_metrics_test[N].json`)
- **Content**: Raw data exported directly from the 5G testbed monitoring system
- **Size**: Largest of the three versions (contains all details)
- **Use case**: Complete dataset with all metrics and measurements; useful for comprehensive analysis
- **Includes**: All metrics including cell downlink bitrate, energy consumption data, and UE (User Equipment) details

### 2. **Modified Version** (`power_metrics_test[N]_MODIFIED.json`)
- **Content**: Cleaned and preprocessed version of the original data
- **Changes Made**: 
  - Data normalization and formatting improvements
  - Removal of erroneous or inconsistent entries
  - Standardization of metric structures
  - Temporal alignment and synchronization of measurements
- **Size**: Similar or slightly smaller than original (minor cleanup)
- **Use case**: Recommended for machine learning model training and data analysis where data quality matters
- **Includes**: All UE (User Equipment) details preserved

### 3. **Modified No UE Details Version** (`power_metrics_test[N]_MODIFIED_NO_UE_DETAILS.json`)
- **Content**: Processed version with User Equipment (UE) details removed
- **Changes Made**: 
  - All modifications from the MODIFIED version
  - **Removal of UE-specific metadata** (individual device information, per-device metrics)
  - Retention of aggregated cell-level metrics
- **Size**: Significantly smaller (~18% of MODIFIED version) - reduced file size due to removed UE details
- **Use case**: 
  - Privacy-preserving version (no individual device tracking)
  - Faster processing and analysis at cell/base station level
  - Compliance with privacy regulations when sharing data
  - Focus on network-wide metrics rather than device-level performance
- **Includes**: Cell-level metrics (downlink bitrate, etc.) but without individual UE information

## Recommendations

| Use Case | Recommended File |
|----------|------------------|
| Complete analysis with all details | `power_metrics_test[N]_MODIFIED.json` |
| Machine Learning & AI Model Training | `power_metrics_test[N]_MODIFIED.json` |
| Privacy-preserving analysis | `power_metrics_test[N]_MODIFIED_NO_UE_DETAILS.json` |
| Faster processing/visualization | `power_metrics_test[N]_MODIFIED_NO_UE_DETAILS.json` |
| Comparison with other datasets | `power_metrics_test[N]_MODIFIED.json` |
| Publication/sharing with external parties | `power_metrics_test[N]_MODIFIED_NO_UE_DETAILS.json` |

## Data Format

All files follow JSON format with the following structure:
```json
{
    "status": "success",
    "data": {
        "resultType": "matrix",
        "result": [
            {
                "metric": {
                    "__name__": "metric_name",
                    "name": "cell_identifier"
                },
                "values": [
                    [timestamp, "value"],
                    [timestamp, "value"],
                    ...
                ]
            }
        ]
    }
}
```

## Test Descriptions

- **Test 1**: First round of power metrics collection
- **Test 2**: Second round of power metrics collection
- **Test 3**: Third round of power metrics collection

Each test captures power consumption characteristics of 5G base stations under various traffic conditions and handover scenarios.
