import os
import yaml

from app.ScalewayManager import ScalewayManager
from app.KeyManager import KeyManager

ACCESS_KEY = os.getenv("SCW_ACCESS_KEY")
SECRET_KEY = os.getenv("SCW_SECRET_KEY")

def main():
    if not ACCESS_KEY or not SECRET_KEY:
        raise ValueError("SCW_ACCESS_KEY and SCW_SECRET_KEY must be set in environment variables.")
    print("Access Key and Secret Key are set.") 
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    KeyManager(ScalewayManager(ACCESS_KEY, SECRET_KEY)).sync_keys(config)

if __name__ == "__main__":
    main()