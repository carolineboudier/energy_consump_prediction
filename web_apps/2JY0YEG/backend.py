import dataiku
import pandas as pd

import dataikuapi

@app.route('/scoring_api_call/<path:params>')
def scoring_api_call(params):
    
    # get Parameters from the form
    print(params)
    # print(params) --> {'claimAmount': '5435','claimDate': '2019-11-27T00:00:00.000Z','claimDept': '77','claimExpert': '1','contractID': '333333','litigationFlag': '1'}
    params = json.loads(params)
    
    warehouse_found = "0"
    if params.get('warehouse_found')=="true":
        warehouse_found = "1"
        
    public_found = "0"
    if params.get('public_found')=="true":
        public_found = "1"
    
    #if params.get('claimDate') == "":
    #    claimDate = "2019-09-01T00:00:00.000Z"
   # else :
    #    claimDate = params.get('claimDate') + 'T00:00:00.000Z'
    year_built=1921
    
  #  record_to_predict = {
   #     "id": params.get('id'),
    #    "floor_area": params.get('floor_area'),
     #   "year_built": year_built,
      ## "public_found": public_found,
        #"State_factor": params.get('State_factor')[:2]
    #}
    
    record_to_predict = {
        "id": params.get('id'),
        "floor_area": params.get('floor_area'),
        "year_built": year_built,
        "public_found": public_found,
        "warehouse_found": warehouse_found,
        "State_Factor":params.get('State_Factor'),
        "code_dep": params.get('claimDept')[:2]
    }


   #"features": {
   #   "public_found": false,
  #    "warehouse_found": false,
 #     "floor_area": 590869,
 #     "year_built": 2001,
 #     "id": 74002
#   }




    record_to_predict = {
      "public_found": 0,
      "warehouse_found": 0,
      "floor_area": 590869,
      "year_built": 2001,
      "id": 74002}
    
    client = dataikuapi.APINodeClient("http://localhost:11300/", "Energy_consumption", "vMPmPc6oc5QsYPmNuQ7C8w7edaQu9HKY")

    prediction = client.predict_record("predict_energy_use_intensity", record_to_predict)

    return json.dumps({"results": prediction})

