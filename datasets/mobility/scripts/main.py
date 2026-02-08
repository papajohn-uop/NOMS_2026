# main.py
import common.context as ctx
from preparation.parse_data_folder import get_data_folder_structure
from preparation.parse_data_folder import get_data_folder_structure
from get_timestamps import get_timestamp_list
import common.help_functions as hf
import models.data_model as dm
from pprint import pprint
from gnb import gnb_main as gnb_main
import json

'''
The FLOW:

Create data set from ue_get metrics for gnb
use this to get more detailed information about the gnb


'''

def create_dataset_entry(exp_ctx: ctx.ExpContext):
    dsentr=exp_ctx.DSENTR
    gnb=exp_ctx.CURRENT_GNB_NAME
    #cretae a gnbmetric obkect
    ds_gnb_entry_obj=dm.GNBEntryMetric(gnb_id=gnb, metrics=list(),cell_metrics=dict())
    dsentr.gnb_metrics[gnb]=ds_gnb_entry_obj
    # for cell in exp_ctx.CELLS:
    for cell in exp_ctx.GNBs[gnb].cells:
        if exp_ctx.CELLS[cell].gnbId==gnb:
            # print(gnb, cell)
            #create teh cell metric obkect
            ds_cell_metric_obj=dm.CellEntryMetrics(
                    cell_id=cell, 
                    metrics=list(),
                    ue_metrics=list())    
            for metric in exp_ctx.CELLS[cell].metrics:
                    # Create the Metric object
                metric_base_obj = dm.metric_base(metric_name=metric, metric_value=exp_ctx.CELLS[cell].metrics[metric])
                ds_cell_metric_obj.metrics.append(metric_base_obj)
                # dsentr.gnb_metrics[gnb].cell_metrics.append(ds_cell_metric_obj)
                dsentr.gnb_metrics[gnb].cell_metrics[cell]=(ds_cell_metric_obj)

            # # #lets work on UEs
            for ue in exp_ctx.CELLS[cell].ues:
            # for ue in cell.ues:
                if gnb==exp_ctx.UEs[ue].gnbId:
                    if cell==exp_ctx.UEs[ue].cellId:
                                #cretae the ue metric object
                        ue_metric_obj=dm.UE_metric(
                                gnb_id=gnb,
                                cell_id=cell,
                                ue_id=ue,
                                metrics=list()
                            )
                        for metric in exp_ctx.UEs[ue].metrics:
        
                            #cretae the ue metric object
                            metric_base_obj = dm.metric_base(metric_name=metric, metric_value=exp_ctx.UEs[ue].metrics[metric])
                            ue_metric_obj.metrics.append(metric_base_obj)
            # dsentr.gnb_metrics[gnb].cell_metrics.ue_metrics.append(ue_metric_obj)
            dsentr.gnb_metrics[gnb].cell_metrics[cell].ue_metrics.append(ue_metric_obj)
    exp_ctx=add_metdata(exp_ctx)
    return exp_ctx


def add_metdata(exp_ctx):
    #create metadtata entry for the dataset
    meta_data_entry=dm.MetadataEntry(
        metadata_name="gnb_id",
        metadata_value=exp_ctx.CURRENT_GNB_NAME)
    if meta_data_entry not in exp_ctx.DATASET.dataset_metadata:
        exp_ctx.DATASET.dataset_metadata.append(meta_data_entry)
    meta_data_entry_test_name=dm.MetadataEntry(
        metadata_name="test_name",
        metadata_value=exp_ctx.TEST_NAME)
    if meta_data_entry_test_name not in exp_ctx.DATASET.dataset_metadata:
        exp_ctx.DATASET.dataset_metadata.append(meta_data_entry_test_name)
    return exp_ctx

    
def work_with_gnb(exp_ctx: ctx.ExpContext):
    exp_ctx.file_path=f"./Data/actual_mobility_1/gnb/{exp_ctx.CURRENT_GNB_NAME}/ue_get/"
    exp_ctx.add_attribute("file_name",f"{exp_ctx.CURRENT_GNB_NAME}.gnb_ue_get." + timestamp)
    exp_ctx.add_attribute("file_to_read", exp_ctx.file_path+exp_ctx.file_name)
    exp_ctx.add_attribute("data", None)

    gnb_obj=dm.gNB(id=exp_ctx.CURRENT_GNB_NAME,cells=dict())   
    exp_ctx.GNBs[gnb_obj.id]=gnb_obj     

    exp_ctx=gnb_main.gnb_ue_get(exp_ctx)
    return exp_ctx

if __name__ == "__main__":
    exp_ctx =ctx.ExpContext()
    exp_ctx=gnb_main.gnb_main(exp_ctx)

    #create a dataset  object
    dataset = dm.Dataset(dataset_id="AI_HO",
            dataset_name="AI_HO",
            dataset_description=f"Dataset for AI handover",
            dataset_metadata=list(),
    )    
    exp_ctx.add_attribute("DATASET",dataset)
    #start wogkin with ue_get from gnb 202
    timestamps_exp1=get_timestamp_list("data/actual_mobility_1/gnb/202/ue_get")
    timestamps_exp2=get_timestamp_list("data/actual_mobility_2/gnb/202/ue_get")
    timestamps_exp3=get_timestamp_list("data/actual_mobility_3/gnb/202/ue_get")
    for timestamp in    timestamps_exp1:
        dsentr=dm.DatasetEntry(
            dataset_entry_id=timestamp,  
        )
        exp_ctx.add_attribute("DSENTR",dsentr)
        #get metrics for ue from ue_get 202
        # we need to create the gnbs and cell before hand
        #at thispoint we can assume that we know part of the data needed for each gnb
        exp_ctx.CURRENT_GNB_NAME="202"
        exp_ctx.TEST_NAME="ACTUAL_MOBILITY_1"
        exp_ctx=work_with_gnb(exp_ctx)
        exp_ctx=create_dataset_entry(exp_ctx)


        #get metrics for ue from ue_get 203
        # we need to create the gnbs and cell before hand
        #at thispoint we can assume that we know part of the data needed for each gnb
        exp_ctx.CURRENT_GNB_NAME="203"
        exp_ctx.TEST_NAME="ACTUAL_MOBILITY_1"
        exp_ctx=work_with_gnb(exp_ctx)
        exp_ctx=create_dataset_entry(exp_ctx)
        
        
        
        exp_ctx.DATASET.entries[timestamp]=dsentr

    # exp_ctx.DATASET.test_name="ds"
    for metric in exp_ctx.UE_GET_UE_METRICS:
        # exp_ctx.DATASET.ue_metrics_metadata.append(exp_ctx.UE_GET_UE_METRICS[metric])
        exp_ctx.DATASET.ue_metrics_metadata.append(exp_ctx.UE_GET_UE_METRICS[metric])
    filename=f"dataset_{exp_ctx.TEST_NAME}.json"
    # Save the dataset JSON to a text file
    with open(filename, "w") as f:
        json.dump(dataset.dict(), f, indent=4)

    print("Dataset saved to dataset.json")
    print(len(dataset.entries))
    # exp_ctx.print_context()
    print(exp_ctx.DATASET.model_dump_json(indent=4))
    # print(dataset.model_dump_json(indent=4))