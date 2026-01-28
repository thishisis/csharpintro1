def add_setting(d, kv):
    k, v = kv
    k=k.lower()
    v=v.lower()
    if(d.get(k, None)!= None):
        return f"Setting '{k}' already exists! Cannot add a new setting with this name."
    else:
        d[k]=v
        return f"Setting '{k}' added with value '{v}' successfully!"
    
def update_setting(d, kv):
    k, v = kv
    k=k.lower()
    v=v.lower()
    if(d.get(k, None)== None):
        return f"Setting '{k}' does not exist! Cannot update a non-existing setting."
    else:
        d[k]=v
        return f"Setting '{k}' updated to '{v}' successfully!"
    
def delete_setting(d, k):
    k=k.lower()
    if(d.get(k, None)== None):
        return f"Setting not found!"
    else:
        del d[k]
        return f"Setting '{k}' deleted successfully!"

def view_settings(d):
    if(len(d)==0):
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for k, v in d.items():
            result += f"{k.capitalize()}: {v}\n"
        return result

if __name__ == "__main__":
    test_settings = {}
    print(add_setting(test_settings, ("Theme", "Dark")))
    print(add_setting(test_settings, ("FontSize", "14")))