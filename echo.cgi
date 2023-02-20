#!/bin/bash
# 文字化け対策
echo "Content-type: text/plain;charset=UTF-8"
# bash CGI独特のおまじない
echo
#POSTメソッドの場合にはread paramで受け取る
read param
echo "$param" | nkgf --url-input

declare -a array=()
mapfile -t array <<< $(echo $param |sed 's|&|\n|g')
declare -p array | nkf --url-input
#for v in "${array[@]}"
#do
#    echo "$v"
#done
echo debug
#echo "${array[@]}"
uid=$(echo "${array[0]}" |awk -F'=' '{print $NF}')
sn=$(echo "${array[1]}" |awk -F'=' '{print $NF}'| nkf --url-input)
gn=$(echo "${array[2]}" |awk -F'=' '{print $NF}'| nkf --url-input)
mail=$(echo "${array[3]}" |awk -F'=' '{print $NF}'| nkf --url-input)

echo "uid is " "${uid}"
echo "sn is" "${sn}"
echo "gn is" "${gn}"
echo "mail is" "${mail}"
echo "今の時刻は $(date)"

./check_args.sh "${uid}" "${sn}" "${gn}" "${mail}" 
