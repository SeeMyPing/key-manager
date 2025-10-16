from scaleway import Client
from scaleway.iam.v1alpha1 import IamV1Alpha1API

class ScalewayManager:
    def __init__(self, access_key, secret_key):
        self.client = Client(access_key=access_key,
                             secret_key=secret_key
                             )
        
    def list_ssh_keys(self, project_id):
        return IamV1Alpha1API(self.client).list_ssh_keys_all(project_id=project_id)
    
    def create_ssh_key(self, project_id, name, public_key):
        return IamV1Alpha1API(self.client).create_ssh_key(
            project_id=project_id,
            name=name,
            public_key=public_key
        )
        
    def delete_ssh_key(self, key_id):
        return  IamV1Alpha1API(self.client).delete_ssh_key(ssh_key_id=key_id)