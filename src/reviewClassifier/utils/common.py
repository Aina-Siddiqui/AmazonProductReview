import os
from box.exceptions import BoxValueError
import yaml
from reviewClassifier.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """Read Yaml file and returns
    Args:
        path_to_yaml(str): Path like input
    Raises:
        ValueError:if yaml file is empty
        e
    Returns:
      ConfigBox:ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create list of directories
    Args:
        path_to_directories(list):list of paths to directories
        ignore_log(bool,optional):ignore if multiple directories to be created.Default to False"""
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")
@ensure_annotations
def get_size(path:Path)->str:
    """
    get size in KB
    Args:
        path of a file
    Returns:
     str: size of the file in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"
