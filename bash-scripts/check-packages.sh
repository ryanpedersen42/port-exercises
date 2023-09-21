#!/bin/bash
# bash testing for presence

checkAxios() {
    check_axios_presence_deps=`cat package.json | jq .dependencies | jq keys`
    check_axios_presence_dev_deps=`cat package.json | jq .devDependencies | jq keys`

    echo $check_axios_presence_deps
    echo $check_axios_presence_dev_deps

    if [[ $check_axios_presence_deps[@] =~ "axios" ]] || [[ $check_axios_presence_dev_deps[@] =~ "axios" ]];
    then
        axios=true        
    else
        axios=false
    fi

    echo $axios
}

checkLodash() {
    check_lodash_presence_deps=`cat package.json | jq .dependencies | jq keys`
    check_lodash_presence_dev_deps=`cat package.json | jq .devDependencies | jq keys`

    echo $check_lodash_presence_deps
    echo $check_lodash_presence_dev_deps

    if [[ $check_lodash_presence_deps[@] =~ "lodash" ]] || [[ $check_lodash_presence_dev_deps[@] =~ "lodash" ]];
    then
        lodash=true        
    else
        lodash=false
    fi

    echo $axios
    echo $lodash
}

checkAxios
checkLodash