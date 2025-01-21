#!/bin/bash

is_hifi_core_less_64mb(){
	job_name=$1
	flag="false"
	export CORES_LIST_HIFI_CORE_LESS_64MB=("hifi4_ss_spfpu_7" "hifils_bt_iot_spfpu_c0" "hifi3z_ss_spfu_nn_dm128")
	arraylength=${#CORES_LIST_HIFI_CORE_LESS_64MB[@]}

	for (( data=0; data<${arraylength}; i++ ));
	do
		if [ "$job_name" == "${CORES_LIST_HIFI_CORE_LESS_64MB[$i]}" ]
		then
			flag="true"
			break
		else
			flag="false"
		fi
	done
	echo $flag
 


}
read -p "Enter a core list name: " name
is_hifi_core_less_64mb $name
