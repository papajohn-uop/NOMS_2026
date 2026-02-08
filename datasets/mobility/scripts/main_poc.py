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

Start gathering data
    GNBS
        Create gNBs

            Add congifguraion
            Add metrics
    Creates PDNS
    Create UEs
    Create Cells
    Create CoreNetwork
    Create DatasetEntry
    Create Dataset


'''







if __name__ == "__main__":
    timestamps=get_timestamp_list("data/actual_mobility_1/gnb/202/config_get")

    exp_ctx =ctx.ExpContext()
    exp_ctx=gnb_main.gnb_main(exp_ctx)

    #create a dataset  object
    dataset = dm.Dataset(dataset_id="AI_HO")    
    # dataset.gNBs = exp_ctx.GNBs


    # Start working on a simple gnb
    for timestamp in    timestamps:
        # print("**************1")
        # #Read config of gnb 202
        exp_ctx.file_path="./Data/actual_mobility_1/gnb/202/config_get/"
        exp_ctx.add_attribute("file_name","202.gnb_config_get." + timestamp)
        exp_ctx.add_attribute("file_to_read", exp_ctx.file_path+exp_ctx.file_name)
        exp_ctx.add_attribute("data", None)
        #create gnbs (and cells) by get config ws
        exp_ctx=gnb_main.gnb_get_config(exp_ctx)
        
        #get_metrics for the cells from stats 202
        exp_ctx.file_path="./Data/actual_mobility_1/gnb/202/stats/"
        exp_ctx.add_attribute("file_name","202.gnb_stats." + timestamp)
        exp_ctx.add_attribute("file_to_read", exp_ctx.file_path+exp_ctx.file_name)
        exp_ctx.add_attribute("data", None)
        exp_ctx=gnb_main.gnb_stats(exp_ctx)


        #get metrics for ue from ue_get 202
        exp_ctx.file_path="./Data/actual_mobility_1/gnb/202/ue_get/"
        exp_ctx.add_attribute("file_name","202.gnb_ue_get." + timestamp)
        exp_ctx.add_attribute("file_to_read", exp_ctx.file_path+exp_ctx.file_name)
        exp_ctx.add_attribute("data", None)
        exp_ctx=gnb_main.gnb_ue_get(exp_ctx)

        # # #Read config of gnb 203
        exp_ctx.file_path="./Data/actual_mobility_1/gnb/203/config_get/"
        exp_ctx.add_attribute("file_name","203.gnb_config_get." + timestamp)
        exp_ctx.add_attribute("file_to_read", exp_ctx.file_path+exp_ctx.file_name)
        exp_ctx.add_attribute("data", None)
        #create gnbs
        exp_ctx=gnb_main.gnb_get_config(exp_ctx)
        #get_metrics for the cells from stats 203
        exp_ctx.file_path="./Data/actual_mobility_1/gnb/203/stats/"
        exp_ctx.add_attribute("file_name","203.gnb_stats." + timestamp)
        exp_ctx.add_attribute("file_to_read", exp_ctx.file_path+exp_ctx.file_name)
        exp_ctx.add_attribute("data", None)
        exp_ctx=gnb_main.gnb_stats(exp_ctx)

        #get metrics for ue from ue_get 203
        exp_ctx.file_path="./Data/actual_mobility_1/gnb/203/ue_get/"
        exp_ctx.add_attribute("file_name","203.gnb_ue_get." + timestamp)
        exp_ctx.add_attribute("file_to_read", exp_ctx.file_path+exp_ctx.file_name)
        exp_ctx.add_attribute("data", None)
        exp_ctx=gnb_main.gnb_ue_get(exp_ctx)

        # exp_ctx.print_context()
        #create a datasetentry  object
        dsentr=dm.DatasetEntry(dataset_entry_id=timestamp,  )
        #create a DatasetEntryMetric  object
        for gnb in exp_ctx.GNBs:
            #cretae a gnbmetric obkect
            ds_gnb_entry_obj=dm.GNBEntryMetric(gnb_id=gnb, metrics=list(),cell_metrics=list())
            dsentr.gnb_metrics[gnb]=ds_gnb_entry_obj
            # for cell in exp_ctx.CELLS:
            for cell in exp_ctx.GNBs[gnb].cells:
                if exp_ctx.CELLS[cell].gnbId==gnb:
                    # print(gnb, cell)
                    #create teh cell metric obkect
                    ds_cell_metric_obg=dm.CellEntryMetrics(
                            cell_id=cell, 
                            metrics=list())    
                    for metric in exp_ctx.CELLS[cell].metrics:
                        #create the metric_base object
                         # Create the Metric object
                        metric_base_obj = dm.metric_base(metric_name=metric, metric_value=exp_ctx.CELLS[cell].metrics[metric])
                        ds_cell_metric_obg.metrics.append(metric_base_obj)
                    # dsentr.gnb_metrics[gnb].cell_metrics.append(ds_cell_metric_obg)
                    # #lets work on UEs
  
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
                                    # print("papa",gnb,cell, ue, metric, exp_ctx.UEs[ue].metrics[metric])
                                    #cretae the ue metric object
                                    metric_base_obj = dm.metric_base(metric_name=metric, metric_value=exp_ctx.UEs[ue].metrics[metric])
                                    ue_metric_obj.metrics.append(metric_base_obj)
                                # print(ue_metric_obj)
                                    # print(exp_ctx.UEs[ue].metrics)
                                ds_cell_metric_obg.ue_metrics.append(ue_metric_obj)
                    dsentr.gnb_metrics[gnb].cell_metrics.append(ds_cell_metric_obg)
                    #                  

                dataset.entries[timestamp]=dsentr
        # break

    print(dataset.model_dump_json(indent=4))
    # exp_ctx.print_context()
