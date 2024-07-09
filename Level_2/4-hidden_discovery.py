if __name__ == "__main__":
    import importlib.util
    import sys
    
    hidden_4_path = "Level_2.hidden_4"
    
    spec = importlib.util.spec_from_file_location(hidden_4_path, hidden_4_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    
    names = dir(hidden_4)
    
    filtered_names = [name for name in names if not name.startswith("__")]
    
    for name in filtered_names:
        print(name)
    
    