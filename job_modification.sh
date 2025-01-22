#this script performing modification in xml files
file=$(cat job_list.txt)
for line in $file; do
  #Performing a sed operation change the values of read_delay and write_delay
  sed -i 's/read_delay = 100/read_delay = 150/' "$line.xml"
  sed -i 's/write_delay = 10/write-delay = 50/' "$line.xml"

  #Print the values of in_checks variable from the .xml files
  #It will print value of in_checks from all the files.
  sed -n '/export in_checks=/,/["'a\-z\_\\\n'"]$/p' "$line.xml"
  echo

  #Perform a sed operation to replace the value of <assignedNode> with "TenIvp - Dummy"
  sed -i 's/<assignedNode>.*<\/assignedNode>/<assignedNode>TenIvp - Dummy<\/assignedNode>/' "$line.xml"

  #Adding network configuration below of "${WORKSPACE}/change_network.cfg"
  sed -i "/${WORKSPACE}\/change_network.cfg/a \[extraXNNCargs.TinyBert_ONNX] \n--mapper_extra == -enable-index-placeholder=true" "$line.xml"

  #Find files that are modified less than 5 days ago and display only .xml files using grep command
  find ./ -type f -mtime -5 | grep "\.xml$"
done