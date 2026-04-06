from fastapi import FastAPI, HTTPException
from core.decoder import decode_vin
from core.validator import validate_check_digit
import uvicorn

app = FastAPI(title="VIN Decoder API")

@app.get("/decode/{vin}")
def decode_vehicle(vin: str):
    vin = vin.upper()
    
    if len(vin) != 17:
        raise HTTPException(status_code=400, detail="VIN must be exactly 17 characters long")
        
    is_valid = validate_check_digit(vin)
    
    # if not is_valid:
    #     # Note: Some older or non-standard VINs might fail the check digit. 
    #     # For insurance, you may want to flag it rather than block it entirely.
    #     raise HTTPException(status_code=400, detail="Invalid Check Digit")
        
    result = decode_vin(vin, db_path="vin_database.db")
    
    return {
        "vin": vin,
        "is_valid_check_digit": is_valid,
        "decoded_data": result
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)