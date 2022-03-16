import dataiku
import pandas as pd
import dataikuapi

# gets parameters from JS
# sends back prediction
@app.route('/scoring_api_call/<path:params>')
def scoring_api_call(params):
    
    # get Parameters from the form
    print('params sent by JS',params)
    params = json.loads(params)
    
    warehouse_found = "0"
    if params.get('warehouse_found')=="true":
        warehouse_found = "1"
        
    public_found = "0"
    if params.get('public_found')=="true":
        public_found = "1"
    
    if params.get('year_built') == "":
        year_built = "1950"
    else :
        year_built=params.get('year_built')

    
    record_to_predict = {
        "id": params.get('id'),
        "floor_area": params.get('floor_area'),
        "year_built": year_built,
        "public_found": public_found,
        "warehouse_found": warehouse_found,
        "State_Factor":params.get('State_Factor')
    }
    
    print('record_to_predict',record_to_predict)
    
    client = dataikuapi.APINodeClient("http://localhost:11300/", "Energy_consumption", "vMPmPc6oc5QsYPmNuQ7C8w7edaQu9HKY")

    prediction = client.predict_record("predict_energy_use_intensity", record_to_predict)
    print("prediction sent back to JS",prediction)
    precise_pred=prediction["result"]["prediction"]
    if precise_pred>=500:
        precise_pred=500
    print("precise pred sent back to JS",precise_pred)

    return json.dumps({"results": precise_pred})

