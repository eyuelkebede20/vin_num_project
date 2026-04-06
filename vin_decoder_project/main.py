from core.decoder import decode_vin
from core.validator import validate_check_digit

def main():
    vin = "JT1L0EE9007150490" 
    
    is_valid = validate_check_digit(vin)
    print(f"Check Digit Valid: {is_valid}")
    
    if is_valid:
        result = decode_vin(vin, db_path="vin_database.db")
        print(result)

if __name__ == "__main__":
    main()