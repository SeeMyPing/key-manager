from .ScalewayManager import ScalewayManager

class KeyManager:
    def __init__(self, scaleway_manager):
        self.scaleway_manager = scaleway_manager

    def sync_keys(self, config):
        for project in config.get("projects", []):
            project_id = project["id"]
            print(f"Syncing keys for project: {project['name']} (ID: {project_id})")
            existing_keys = self.scaleway_manager.list_ssh_keys(project_id)
            existing_key_names = {key.name: key for key in existing_keys}

            for key_cfg in project.get("keys", []):
                key_name = key_cfg["name"]
                key_type = key_cfg["type"]
                if key_name not in existing_key_names:
                    public_key_path = f"keys/{key_name}.{key_type}"
                    try:
                        with open(public_key_path, "r") as pk_file:
                            public_key = pk_file.read().strip()
                        self.scaleway_manager.create_ssh_key(project_id, key_name, public_key)
                        print(f"Created SSH key '{key_name}' in project '{project['name']}'")
                    except FileNotFoundError:
                        print(f"Public key file '{public_key_path}' not found. Skipping key '{key_name}'.")
                else:
                    print(f"SSH key '{key_name}' already exists in project '{project['name']}'")
            for existing_key in existing_keys:
                if existing_key.name not in [k["name"] for k in project.get("keys", [])]:
                    self.scaleway_manager.delete_ssh_key(existing_key.id)
                    print(f"Deleted SSH key '{existing_key.name}' from project '{project['name']}'")